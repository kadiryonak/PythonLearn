"""
RAG EMBEDDING EĞİTİMİ
=====================
Bu dosyada RAG (Retrieval Augmented Generation) sisteminin
en kritik bileşeni olan EMBEDDING'leri öğreneceğiz.

EMBEDDING NEDİR?
- Metin/kelime/cümleleri sayısal vektörlere dönüştürme
- Benzer anlamlar → Benzer vektörler
- Vector DB'de arama yapabilmek için gerekli

PIPELINE:
Text → Chunking → EMBEDDING → Vector DB → Similarity Search → LLM
"""

import os
from dotenv import load_dotenv
load_dotenv()

# ============================================================
# ÖRNEK METİN - YAPAY ZEKA VE TEKNOLOJİ ANSİKLOPEDİSİ
# ============================================================

sample_text = """
YAPAY ZEKA VE TEKNOLOJİ ANSİKLOPEDİSİ
=====================================

BÖLÜM 1: YAPAY ZEKANIN TARİHÇESİ
--------------------------------

Yapay zeka kavramı ilk olarak 1956 yılında Dartmouth Konferansı'nda ortaya atıldı. 
John McCarthy, Marvin Minsky, Claude Shannon ve Nathaniel Rochester gibi öncüler, 
makinelerin insan gibi düşünebileceği fikrini savundular. Bu konferans, yapay zeka 
araştırmalarının resmi başlangıcı olarak kabul edilir.

1960'larda ilk uzman sistemler geliştirildi. ELIZA, doğal dil işleme alanındaki 
ilk programlardan biriydi ve basit bir terapist simülasyonu yapıyordu. 
DENDRAL ise kimyasal bileşikleri analiz eden ilk uzman sistemdi.

1970'ler ve 1980'ler "Yapay Zeka Kışı" olarak adlandırıldı. Aşırı beklentiler 
karşılanmayınca fonlar kesildi ve araştırmalar yavaşladı. Ancak 1990'larda 
makine öğrenmesi tekniklerindeki ilerlemeler yeni bir dönem başlattı.

2000'lerde internet ve büyük veri çağı, yapay zeka araştırmalarını hızlandırdı. 
Google, Facebook ve Amazon gibi şirketler, büyük veri setleri üzerinde 
makine öğrenmesi algoritmalarını kullanmaya başladı.

2012 yılında AlexNet, ImageNet yarışmasını kazanarak derin öğrenme devrimini 
başlattı. Bu olay, modern yapay zeka çağının başlangıcı olarak görülür.

BÖLÜM 2: MAKİNE ÖĞRENMESİ TÜRLERİ
---------------------------------

DENETİMLİ ÖĞRENME (SUPERVISED LEARNING):
Etiketli verilerle eğitim yapılır. Model, girdi ve çıktı arasındaki 
ilişkiyi öğrenir. Örnek: Spam filtreleme, kredi riski değerlendirme, 
hastalık teşhisi. Regresyon ve sınıflandırma problemleri bu kategoriye girer.

DENETİMSİZ ÖĞRENME (UNSUPERVISED LEARNING):
Etiketsiz verilerle çalışır. Model, verideki gizli örüntüleri keşfeder.
Örnek: Müşteri segmentasyonu, anomali tespiti, boyut indirgeme.
K-means kümeleme, PCA ve otomatik kodlayıcılar bu yöntemler arasındadır.

PEKİŞTİRMELİ ÖĞRENME (REINFORCEMENT LEARNING):
Ajan, çevreyle etkileşerek ödül maksimizasyonu yapar. Deneme-yanılma 
yoluyla optimal stratejiyi öğrenir. Örnek: Oyun oynama (AlphaGo, Atari),
robotik, otonom araçlar, algoritmik ticaret.

YARI DENETİMLİ ÖĞRENME (SEMI-SUPERVISED LEARNING):
Az miktarda etiketli veri ve çok miktarda etiketsiz veri kullanılır.
Etiketleme maliyeti yüksek olduğunda tercih edilir. Label propagation
ve pseudo-labeling teknikleri bu kategoridedir.

BÖLÜM 3: DERİN ÖĞRENME MİMARİLERİ
---------------------------------

YAPAY SİNİR AĞLARI (ANN):
En temel derin öğrenme mimarisi. Giriş katmanı, gizli katmanlar ve 
çıkış katmanından oluşur. Her nöron, ağırlıklı toplam ve aktivasyon 
fonksiyonu uygular. ReLU, Sigmoid ve Tanh yaygın aktivasyon fonksiyonlarıdır.

EVRİŞİMLİ SİNİR AĞLARI (CNN):
Görüntü işleme için tasarlanmış mimari. Evrişim katmanları, havuzlama 
katmanları ve tam bağlantılı katmanlardan oluşur. ResNet, VGG, Inception 
popüler CNN mimarileridir. Görüntü sınıflandırma, nesne tespiti, 
yüz tanıma gibi görevlerde kullanılır.

TEKRARLAYAN SİNİR AĞLARI (RNN):
Sıralı veriler için tasarlanmış mimari. Gizli durum, önceki zaman 
adımlarından bilgi taşır. Vanishing gradient problemi nedeniyle 
uzun dizilerde zorlanır. Metin üretimi, zaman serisi analizi,
konuşma tanıma gibi görevlerde kullanılır.

LSTM VE GRU:
RNN'in geliştirilmiş versiyonları. LSTM (Long Short-Term Memory) 
unutma kapısı, girdi kapısı ve çıktı kapısı içerir. GRU (Gated 
Recurrent Unit) daha basit bir yapıya sahiptir. Her ikisi de 
uzun vadeli bağımlılıkları öğrenebilir.

TRANSFORMER:
2017'de "Attention is All You Need" makalesiyle tanıtıldı. 
Self-attention mekanizması ile paralel işlem yapar. BERT, GPT, 
T5 gibi modellerin temelini oluşturur. NLP alanında devrim yarattı.

BÖLÜM 4: DOĞAL DİL İŞLEME (NLP)
-------------------------------

TOKENİZASYON:
Metni daha küçük birimlere (token) ayırma işlemi. Kelime düzeyinde,
alt-kelime düzeyinde (BPE, WordPiece) veya karakter düzeyinde olabilir.
BERT WordPiece, GPT BPE kullanır.

WORD EMBEDDINGS:
Kelimeleri yoğun vektörlere dönüştürme. Word2Vec (CBOW, Skip-gram),
GloVe ve FastText popüler yöntemlerdir. Anlamsal benzerliği yakalar:
king - man + woman ≈ queen

TRANSFORMER TABANLI MODELLER:
BERT (Bidirectional Encoder Representations from Transformers):
Çift yönlü bağlam anlama. Masked language modeling ile eğitilir.
Sınıflandırma, soru cevaplama, NER görevlerinde kullanılır.

GPT (Generative Pre-trained Transformer):
Tek yönlü, metin üretimine odaklı. Autoregressive generation yapar.
GPT-3'ün 175 milyar parametresi var. ChatGPT bu serinin ürünüdür.

T5 (Text-to-Text Transfer Transformer):
Her NLP görevini metin-to-metin formatına dönüştürür.
"translate English to French: Hello" → "Bonjour"

BÖLÜM 5: BÜYÜK DİL MODELLERİ (LLM)
----------------------------------

LLM'ler milyarlarca parametre içeren dev transformer modelleridir.
Few-shot ve zero-shot öğrenme yetenekleri vardır. Prompt engineering
ile farklı görevlere uyarlanabilirler.

ÖRNEKLER:
- GPT-4 (OpenAI): Multimodal, kod yazma, analiz
- Claude (Anthropic): Güvenlik odaklı, uzun bağlam
- Gemini (Google): Multimodal, çok dilli
- LLaMA (Meta): Açık kaynak, araştırma odaklı
- Mistral: Verimli, açık kaynak

RAG (RETRIEVAL AUGMENTED GENERATION):
LLM'leri harici bilgi kaynaklarıyla güçlendirme. Güncel bilgi,
özel dokümanlar ve halüsinasyon azaltma için kullanılır.
Pipeline: Soru → Retrieval → Context + Soru → LLM → Cevap

BÖLÜM 6: VERİTABANLARI VE VEKTÖR DB
-----------------------------------

GELENEKSEL VERİTABANLARI:
- İlişkisel (PostgreSQL, MySQL): Yapılandırılmış veri, SQL
- NoSQL (MongoDB, Redis): Esnek şema, ölçeklenebilir
- Grafik (Neo4j): İlişki ağırlıklı sorgular

VEKTÖR VERİTABANLARI:
Yüksek boyutlu vektörleri depolamak ve aramak için optimize edilmiş.
Similarity search, ANN (Approximate Nearest Neighbor) algoritmaları.

POPÜLER VEKTÖR DB'LER:
- Pinecone: Tam yönetilen, ölçeklenebilir
- Chroma: Açık kaynak, Python dostu
- Weaviate: Hibrit arama, GraphQL
- Milvus: Yüksek performans, dağıtık
- FAISS (Facebook): Kütüphane, yerel kullanım
- Qdrant: Rust tabanlı, hızlı

SİMİLARİTY METRICS:
- Cosine Similarity: Açı benzerliği, -1 ile 1 arası
- Euclidean Distance: Uzaklık ölçümü
- Dot Product: İç çarpım benzerliği

BÖLÜM 7: ETİK VE GÜVENLİK
-------------------------

ÖNYARGI (BIAS):
Eğitim verisindeki önyargılar modele yansır. Cinsiyet, ırk, yaş 
gibi hassas özellikler için dikkatli olunmalı. Fairness metrics
ve debiasing teknikleri uygulanmalı.

GİZLİLİK:
PII (Personally Identifiable Information) korunmalı. Differential
privacy, federated learning gibi teknikler kullanılabilir.

HALÜSINASYON:
LLM'lerin yanlış bilgi üretmesi. Grounding, RAG ve fact-checking
ile azaltılabilir.

GÜVENLİK:
Prompt injection, jailbreaking gibi saldırılara karşı önlem.
Input validation, output filtering, safety training gerekli.
"""

# ============================================================
# 1. METNİ CHUNK'LARA AYIRMA
# ============================================================

from langchain.text_splitter import RecursiveCharacterTextSplitter

print("="*60)
print("1. METNİ CHUNK'LARA AYIRMA")
print("="*60)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,         # Her chunk max 500 karakter
    chunk_overlap=100,      # 100 karakter örtüşme
    separators=["\n\n", "\n", ". ", " ", ""],
    length_function=len
)

chunks = text_splitter.split_text(sample_text)

print(f"Toplam metin uzunluğu: {len(sample_text)} karakter")
print(f"Oluşan chunk sayısı: {len(chunks)}")
print(f"Ortalama chunk boyutu: {sum(len(c) for c in chunks) // len(chunks)} karakter")

print("\n--- İlk 3 Chunk Önizleme ---")
for i, chunk in enumerate(chunks[:3]):
    print(f"\n[Chunk {i+1}] ({len(chunk)} karakter)")
    print(f"'{chunk[:150]}...'")

# ============================================================
# 2. EMBEDDING NEDİR? - TEORİ
# ============================================================

print("\n" + "="*60)
print("2. EMBEDDING NEDİR? - TEORİ")
print("="*60)

print("""
EMBEDDING: Metni sayısal vektörlere dönüştürme işlemi

NEDEN GEREKLİ?
- Bilgisayarlar metni doğrudan anlayamaz
- Vektörler matematiksel işlem yapılabilir
- Benzerlik hesaplanabilir (cosine similarity)

ÖRNEK:
"Kedi" → [0.2, -0.5, 0.8, 0.1, ...]  (768 veya 1536 boyutlu)
"Köpek" → [0.3, -0.4, 0.7, 0.2, ...]  (benzer vektör)
"Araba" → [-0.6, 0.9, -0.2, 0.4, ...] (farklı vektör)

Kedi ve Köpek vektörleri birbirine yakın (hayvan)
Araba vektörü onlardan uzak (farklı kategori)

BOYUT (DIMENSION):
- OpenAI ada-002: 1536 boyut
- OpenAI text-embedding-3-small: 1536 boyut
- OpenAI text-embedding-3-large: 3072 boyut
- BERT base: 768 boyut
- Sentence-BERT: 384-768 boyut
- HuggingFace modelleri: 384-1024 boyut

EMBEDDING MODELLERİ:
1. OpenAI Embeddings (Ücretli, yüksek kalite)
2. HuggingFace Embeddings (Ücretsiz, çeşitli)
3. Google Embeddings (Vertex AI)
4. Cohere Embeddings
5. Local modeller (sentence-transformers)
""")

# ============================================================
# 3. HUGGINGFACE EMBEDDINGS (ÜCRETSİZ)
# ============================================================

print("="*60)
print("3. HUGGINGFACE EMBEDDINGS (ÜCRETSİZ)")
print("="*60)

try:
    from langchain_huggingface import HuggingFaceEmbeddings
    
    # Model yükleme (ilk seferde indirilir)
    print("Model yükleniyor... (ilk seferde ~100MB indirilir)")
    
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",  # Hafif ve hızlı
        model_kwargs={'device': 'cpu'},  # CPU kullan
        encode_kwargs={'normalize_embeddings': True}  # Normalize et
    )
    
    # Tek metin embedding
    test_text = "Yapay zeka günümüzün en önemli teknolojisidir."
    vector = embeddings.embed_query(test_text)
    
    print(f"\n✓ Model yüklendi!")
    print(f"Test metni: '{test_text}'")
    print(f"Vektör boyutu: {len(vector)}")
    print(f"İlk 10 değer: {vector[:10]}")
    
    # Birden fazla metin embedding
    texts = [
        "Makine öğrenmesi verileri analiz eder.",
        "Derin öğrenme yapay sinir ağları kullanır.",
        "Python programlama dilidir."
    ]
    
    vectors = embeddings.embed_documents(texts)
    print(f"\n{len(texts)} metin için embedding oluşturuldu.")
    
except ImportError:
    print("❌ langchain_huggingface yüklü değil!")
    print("pip install langchain-huggingface sentence-transformers")
except Exception as e:
    print(f"Hata: {e}")

# ============================================================
# 4. COSINE SIMILARITY (BENZERLİK HESAPLAMA)
# ============================================================

print("\n" + "="*60)
print("4. COSINE SIMILARITY (BENZERLİK HESAPLAMA)")
print("="*60)

import numpy as np

def cosine_similarity(vec1, vec2):
    """İki vektör arasındaki cosine similarity hesapla"""
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)

print("""
COSINE SIMILARITY FORMÜLÜ:
                    A · B
cos(θ) = ─────────────────────
         ||A|| × ||B||

SONUÇ YORUMLAMA:
- 1.0  → Tamamen aynı yönde (çok benzer)
- 0.5  → Orta benzerlik
- 0.0  → Dik açı (ilişkisiz)
- -1.0 → Tam zıt yönde (zıt anlamlı)
""")

# Örnek benzerlik hesabı
try:
    sentences = [
        "Yapay zeka makinelerin düşünmesini sağlar.",
        "Makine öğrenmesi yapay zekanın bir dalıdır.",
        "Bugün hava çok güzel ve güneşli."
    ]
    
    if 'embeddings' in dir():
        vecs = embeddings.embed_documents(sentences)
        
        print("Benzerlik Matrisi:")
        print("-" * 40)
        for i, s1 in enumerate(sentences):
            for j, s2 in enumerate(sentences):
                sim = cosine_similarity(vecs[i], vecs[j])
                print(f"[{i+1}] vs [{j+1}]: {sim:.4f}")
            print()
        
        print("Cümleler:")
        for i, s in enumerate(sentences):
            print(f"[{i+1}] {s}")
            
except Exception as e:
    print(f"Benzerlik hesabı yapılamadı: {e}")

# ============================================================
# 5. CHUNK'LARI EMBEDDİNG'E DÖNÜŞTÜRME
# ============================================================

print("\n" + "="*60)
print("5. CHUNK'LARI EMBEDDİNG'E DÖNÜŞTÜRME")
print("="*60)

try:
    if 'embeddings' in dir() and 'chunks' in dir():
        print(f"Toplam {len(chunks)} chunk embedding'e dönüştürülüyor...")
        
        # Sadece ilk 5 chunk'ı dönüştür (zaman kazanmak için)
        sample_chunks = chunks[:5]
        chunk_embeddings = embeddings.embed_documents(sample_chunks)
        
        print(f"✓ {len(sample_chunks)} chunk için embedding oluşturuldu!")
        
        for i, (chunk, vec) in enumerate(zip(sample_chunks, chunk_embeddings)):
            print(f"\nChunk {i+1}: '{chunk[:50]}...'")
            print(f"Vektör boyutu: {len(vec)}, İlk 5 değer: {vec[:5]}")
            
except Exception as e:
    print(f"Chunk embedding hatası: {e}")

# ============================================================
# 6. GOOGLE EMBEDDINGS (API KEY İLE)
# ============================================================

print("\n" + "="*60)
print("6. GOOGLE EMBEDDINGS (API KEY İLE)")
print("="*60)

try:
    from langchain_google_genai import GoogleGenerativeAIEmbeddings
    
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if api_key:
        google_embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=api_key
        )
        
        test_text = "Yapay zeka çok önemlidir."
        vector = google_embeddings.embed_query(test_text)
        
        print(f"✓ Google Embedding başarılı!")
        print(f"Metin: '{test_text}'")
        print(f"Vektör boyutu: {len(vector)}")
        print(f"İlk 10 değer: {vector[:10]}")
    else:
        print("GOOGLE_API_KEY bulunamadı. .env dosyasını kontrol edin.")
        
except ImportError:
    print("langchain_google_genai yüklü değil: pip install langchain-google-genai")
except Exception as e:
    print(f"Google Embedding hatası: {e}")

# ============================================================
# 7. VECTOR STORE'A KAYDETME (CHROMA)
# ============================================================

print("\n" + "="*60)
print("7. VECTOR STORE'A KAYDETME (CHROMA)")
print("="*60)

try:
    from langchain_chroma import Chroma
    from langchain.schema import Document
    
    # Chunk'ları Document formatına çevir
    documents = [
        Document(
            page_content=chunk,
            metadata={"source": "ai_encyclopedia.txt", "chunk_id": i}
        )
        for i, chunk in enumerate(chunks[:10])  # İlk 10 chunk
    ]
    
    print(f"Toplam {len(documents)} doküman hazırlandı.")
    
    if 'embeddings' in dir():
        # In-memory vector store oluştur
        db = Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            collection_name="rag_tutorial"
        )
        
        print("✓ Vector Store oluşturuldu!")
        print(f"Koleksiyon adı: rag_tutorial")
        print(f"Kayıtlı doküman: {len(documents)}")
        
        # Similarity search test
        query = "Derin öğrenme nedir?"
        results = db.similarity_search(query, k=3)
        
        print(f"\nSorgu: '{query}'")
        print("En benzer 3 chunk:")
        for i, doc in enumerate(results):
            print(f"\n[{i+1}] Skor: N/A (similarity_search skoru vermez)")
            print(f"Chunk ID: {doc.metadata['chunk_id']}")
            print(f"İçerik: '{doc.page_content[:100]}...'")
            
except ImportError:
    print("chromadb yüklü değil: pip install langchain-chroma chromadb")
except Exception as e:
    print(f"Vector Store hatası: {e}")

# ============================================================
# 8. SIMILARITY SEARCH WITH SCORES
# ============================================================

print("\n" + "="*60)
print("8. SIMILARITY SEARCH WITH SCORES")
print("="*60)

try:
    if 'db' in dir():
        query = "Transformer mimarisi nasıl çalışır?"
        results_with_scores = db.similarity_search_with_score(query, k=3)
        
        print(f"Sorgu: '{query}'")
        print("\nEn benzer 3 chunk (skor ile):")
        
        for i, (doc, score) in enumerate(results_with_scores):
            print(f"\n[{i+1}] Benzerlik Skoru: {score:.4f}")
            print(f"Chunk ID: {doc.metadata['chunk_id']}")
            print(f"İçerik: '{doc.page_content[:150]}...'")
            
        print("\nSkor Yorumu:")
        print("- Düşük skor = Daha benzer (distance-based)")
        print("- Cosine: 0'a yakın = çok benzer")
        
except Exception as e:
    print(f"Skor ile arama hatası: {e}")

# ============================================================
# 9. TAM RAG PIPELINE - ÖZET
# ============================================================

print("\n" + "="*60)
print("9. TAM RAG PIPELINE")
print("="*60)

print("""
RAG PIPELINE ADIMLARI:
══════════════════════════════════════════════════════════════

1. LOAD (Yükle)
   ├── PDF: PyPDFLoader
   ├── TXT: TextLoader  
   ├── Web: WebBaseLoader
   └── Word: Docx2txtLoader

2. SPLIT (Parçala) ← Chunking
   ├── RecursiveCharacterTextSplitter (önerilen)
   ├── CharacterTextSplitter
   └── TokenTextSplitter

3. EMBED (Gömme) ← ŞU AN BURASI
   ├── HuggingFaceEmbeddings (ücretsiz)
   ├── OpenAIEmbeddings (ücretli, yüksek kalite)
   └── GoogleGenerativeAIEmbeddings

4. STORE (Sakla)
   ├── Chroma (kolay, açık kaynak)
   ├── FAISS (hızlı, yerel)
   ├── Pinecone (bulut, ölçeklenebilir)
   └── Weaviate, Milvus, Qdrant

5. RETRIEVE (Getir)
   ├── similarity_search()
   ├── similarity_search_with_score()
   └── max_marginal_relevance_search()

6. GENERATE (Üret)
   ├── Context + Question → LLM
   └── RetrievalQA Chain

══════════════════════════════════════════════════════════════

ÖRNEK KOD (Tam Pipeline):
-------------------------
from langchain.chains import RetrievalQA

qa_chain = RetrievalQA.from_chain_type(
    llm=model,
    chain_type="stuff",
    retriever=db.as_retriever(search_kwargs={"k": 3})
)

answer = qa_chain.invoke("Derin öğrenme nedir?")
print(answer)
══════════════════════════════════════════════════════════════
""")

print("="*60)
print("RAG EMBEDDING EĞİTİMİ TAMAMLANDI!")
print("="*60)

print("""
KURULUM GEREKSİNİMLERİ:
-----------------------
pip install langchain langchain-huggingface sentence-transformers
pip install langchain-google-genai langchain-chroma chromadb
pip install numpy python-dotenv
""")
