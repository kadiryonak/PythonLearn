
# ============================================================
# RAG İÇİN TEXT CHUNKING (Metin Parçalama)
# ============================================================
"""
RAG (Retrieval Augmented Generation) için metin parçalama kritiktir.
Büyük dokümanları küçük parçalara (chunks) bölerek:
1. Embedding oluşturma
2. Vector DB'de saklama
3. Similarity search ile ilgili parçaları bulma
işlemleri yapılır.
"""

from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    TokenTextSplitter
)

# Örnek uzun metin
sample_text = """
Yapay Zeka ve Makine Öğrenmesi

Yapay zeka (AI), makinelerin insan benzeri zeka göstermesini sağlayan bir bilgisayar bilimi dalıdır. 
Yapay zeka, problem çözme, öğrenme, planlama ve dil anlama gibi yetenekleri kapsar.

Makine öğrenmesi (ML), yapay zekanın bir alt dalıdır. ML sistemleri, verilerden öğrenerek 
tahminler yapar ve kararlar alır. Denetimli öğrenme, denetimsiz öğrenme ve pekiştirmeli 
öğrenme olmak üzere üç ana türü vardır.

Derin öğrenme (Deep Learning), yapay sinir ağları kullanan bir makine öğrenmesi türüdür.
Çok katmanlı sinir ağları sayesinde karmaşık örüntüleri öğrenebilir. Görüntü tanıma, 
doğal dil işleme ve ses tanıma gibi alanlarda çığır açıcı sonuçlar elde edilmiştir.

Doğal Dil İşleme (NLP), bilgisayarların insan dilini anlaması ve üretmesi üzerine çalışır.
Chatbotlar, çeviri sistemleri ve metin özetleme bu alanın uygulama örnekleridir.

Transformers mimarisi, NLP alanında devrim yarattı. BERT, GPT ve T5 gibi modeller
bu mimariye dayanır ve çeşitli dil görevlerinde üstün performans sergiler.
"""

print("\n" + "="*60)
print("RAG İÇİN TEXT CHUNKING ÖRNEKLERİ")
print("="*60)

# -------------------------------------------------------------
# 1. CHARACTER TEXT SPLITTER (Karakter Bazlı Bölme)
# -------------------------------------------------------------
print("\n" + "-"*50)
print("1. CHARACTER TEXT SPLITTER")
print("-"*50)

char_splitter = CharacterTextSplitter(
    separator="\n\n",      # Paragraflardan böl
    chunk_size=200,        # Her chunk max 200 karakter
    chunk_overlap=20,      # Chunk'lar arası 20 karakter örtüşme
    length_function=len    # Uzunluk ölçümü: karakter sayısı
)

char_chunks = char_splitter.split_text(sample_text)

print(f"Toplam chunk sayısı: {len(char_chunks)}")
for i, chunk in enumerate(char_chunks):
    print(f"\n[Chunk {i+1}] ({len(chunk)} karakter)")
    print(f"'{chunk[:80]}...'")  # İlk 80 karakter

# -------------------------------------------------------------
# 2. RECURSIVE CHARACTER TEXT SPLITTER (Önerilen Yöntem)
# -------------------------------------------------------------
print("\n" + "-"*50)
print("2. RECURSIVE CHARACTER TEXT SPLITTER (EN İYİSİ)")
print("-"*50)

"""
RecursiveCharacterTextSplitter, metni hiyerarşik olarak böler:
1. Önce paragraflardan (\n\n)
2. Sonra satırlardan (\n)
3. Sonra cümlelerden (. veya boşluk)
4. En son karakterlerden

Bu sayede anlamlı bölümler korunur.
"""

recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    separators=["\n\n", "\n", ". ", " ", ""],  # Öncelik sırası
    length_function=len
)

recursive_chunks = recursive_splitter.split_text(sample_text)

print(f"Toplam chunk sayısı: {len(recursive_chunks)}")
for i, chunk in enumerate(recursive_chunks):
    print(f"\n[Chunk {i+1}] ({len(chunk)} karakter)")
    print(f"'{chunk[:100]}...'")

# -------------------------------------------------------------
# 3. TOKEN BASED SPLITTER (Token Bazlı Bölme)
# -------------------------------------------------------------
print("\n" + "-"*50)
print("3. TOKEN TEXT SPLITTER")
print("-"*50)

"""
Token bazlı bölme, LLM'lerin token limitlerini dikkate alır.
Örnek: GPT-4 = 8K token, Claude = 100K token
Embedding modelleri genellikle 512 token kabul eder.
"""

try:
    token_splitter = TokenTextSplitter(
        chunk_size=100,      # 100 token
        chunk_overlap=20     # 20 token örtüşme
    )
    token_chunks = token_splitter.split_text(sample_text)
    print(f"Token bazlı chunk sayısı: {len(token_chunks)}")
except Exception as e:
    print(f"Token splitter için tiktoken gerekli: {e}")
    print("pip install tiktoken")

# -------------------------------------------------------------
# 4. OVERLAP NEDİR? (Örtüşme)
# -------------------------------------------------------------
print("\n" + "-"*50)
print("4. CHUNK OVERLAP (ÖRTÜŞME) NEDİR?")
print("-"*50)

"""
Overlap, bir chunk'ın son kısmının, sonraki chunk'ın başında 
tekrar etmesidir. Bu sayede:
1. Cümle ortasından bölünme riski azalır
2. Bağlam kaybı önlenir
3. Similarity search daha iyi çalışır

Örnek:
Chunk 1: "Yapay zeka makinelerin insan benzeri"
Chunk 2: "insan benzeri zeka göstermesini sağlar"
         ^^^^^^^^^^^^^^^
         Overlap kısmı (15 karakter)
"""

# Overlap'sız vs Overlap'lı karşılaştırma
no_overlap = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
with_overlap = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=30)

text = "Yapay zeka günümüzün en önemli teknolojisidir. Makine öğrenmesi yapay zekanın alt dalıdır."

print("\nOverlap=0:")
for i, c in enumerate(no_overlap.split_text(text)):
    print(f"  Chunk {i+1}: '{c}'")

print("\nOverlap=30:")
for i, c in enumerate(with_overlap.split_text(text)):
    print(f"  Chunk {i+1}: '{c}'")

# -------------------------------------------------------------
# 5. CHUNK SIZE SEÇİMİ REHBERİ
# -------------------------------------------------------------
print("\n" + "-"*50)
print("5. CHUNK SIZE NASIL SEÇİLİR?")
print("-"*50)

print("""
╔══════════════════════════════════════════════════════════════╗
║  KULLANIM ALANI          │  ÖNERİLEN CHUNK SIZE              ║
╠══════════════════════════════════════════════════════════════╣
║  Soru-Cevap (Q&A)        │  256 - 512 karakter               ║
║  Doküman Arama           │  512 - 1024 karakter              ║
║  Özetleme                │  1024 - 2048 karakter             ║
║  Kod Analizi             │  Fonksiyon/sınıf bazlı            ║
║  Chat Geçmişi            │  Mesaj bazlı                      ║
╠══════════════════════════════════════════════════════════════╣
║  OVERLAP KURALI: chunk_size * 0.1 - 0.2 (10-20%)             ║
╚══════════════════════════════════════════════════════════════╝
""")

# -------------------------------------------------------------
# 6. DOCUMENT LOADER İLE CHUNKING
# -------------------------------------------------------------
print("-"*50)
print("6. DOCUMENT'LARDAN CHUNKING")
print("-"*50)

from langchain.schema import Document

# Document nesnesi oluştur (gerçekte PDF, TXT vs. okunur)
documents = [
    Document(
        page_content="Yapay zeka günümüzde çok önemlidir.",
        metadata={"source": "ai.txt", "page": 1}
    ),
    Document(
        page_content="Makine öğrenmesi verileri analiz eder.",
        metadata={"source": "ml.txt", "page": 1}
    )
]

# Document'ları chunk'la
doc_splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=10)
split_docs = doc_splitter.split_documents(documents)

print(f"Orijinal doküman sayısı: {len(documents)}")
print(f"Chunk'lanmış doküman sayısı: {len(split_docs)}")
for doc in split_docs:
    print(f"  - '{doc.page_content}' | Kaynak: {doc.metadata['source']}")

# -------------------------------------------------------------
# 7. TAM RAG PİPELINE ÖRNEĞİ (Özet)
# -------------------------------------------------------------
print("\n" + "-"*50)
print("7. RAG PIPELINE ÖZETİ")
print("-"*50)

print("""
RAG PIPELINE ADIMLARI:
═══════════════════════════════════════════════════════════════

1. LOAD (Yükle)
   └── PDF, TXT, Web sayfası, DB'den veri çek
   
2. SPLIT (Parçala) ← ŞU AN BURASI
   └── RecursiveCharacterTextSplitter ile chunk'la
   
3. EMBED (Gömme)
   └── Her chunk'ı vector'e dönüştür (OpenAI, HuggingFace)
   
4. STORE (Sakla)
   └── Vector DB'ye kaydet (Chroma, Pinecone, FAISS)
   
5. RETRIEVE (Getir)
   └── Kullanıcı sorusuna en benzer chunk'ları bul
   
6. GENERATE (Üret)
   └── LLM'e chunk'ları + soruyu ver, cevap üret

═══════════════════════════════════════════════════════════════
""")

print("="*60)
print("RAG CHUNKING EĞİTİMİ TAMAMLANDI!")
print("="*60)