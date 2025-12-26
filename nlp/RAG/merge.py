"""
RAG (Retrieval Augmented Generation) MİMARİSİ REHBERİ
=====================================================

Bu dosya, adım adım bir RAG sistemi oluşturmayı öğretir.
Kodları SEN yazacaksın, ben sadece adımları açıklıyorum.

RAG NEDİR?
----------
LLM'lere harici bilgi kaynakları vererek daha doğru cevaplar üretmek.
- Halüsinasyonu azaltır
- Güncel bilgi sağlar
- Özel dokümanları kullanır

RAG PIPELINE:
    LOAD → SPLIT → EMBED → STORE → RETRIEVE → GENERATE
"""

# ============================================================
# ADIM 0: GEREKLİ KÜTÜPHANELER
# ============================================================
"""
Aşağıdaki kütüphaneleri yükle:

pip install langchain langchain-google-genai python-dotenv
pip install langchain-huggingface sentence-transformers
pip install langchain-chroma chromadb
pip install pypdf  # PDF okumak için
"""

# TODO: Gerekli import'ları yaz
# import os
# from dotenv import load_dotenv
# load_dotenv()


# ============================================================
# ADIM 1: LOAD (Doküman Yükleme)
# ============================================================
"""
Farklı dosya formatlarından veri yükle:

1. TXT dosyası için:
   from langchain_community.document_loaders import TextLoader
   loader = TextLoader("dosya.txt", encoding="utf-8")
   documents = loader.load()

2. PDF dosyası için:
   from langchain_community.document_loaders import PyPDFLoader
   loader = PyPDFLoader("dosya.pdf")
   documents = loader.load()

3. Web sayfası için:
   from langchain_community.document_loaders import WebBaseLoader
   loader = WebBaseLoader("https://example.com")
   documents = loader.load()

4. Birden fazla dosya için:
   from langchain_community.document_loaders import DirectoryLoader
   loader = DirectoryLoader("./docs", glob="*.txt")
   documents = loader.load()

Her document şu yapıda:
- page_content: Metnin kendisi
- metadata: {"source": "dosya.txt", "page": 1}
"""

# TODO: Kendi dokümanını yükle
# loader = ...
# documents = loader.load()
# print(f"Yüklenen doküman sayısı: {len(documents)}")


# ============================================================
# ADIM 2: SPLIT (Chunking - Parçalama)
# ============================================================
"""
Büyük dokümanları küçük parçalara böl:

from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # Her parça max 500 karakter
    chunk_overlap=100,   # Parçalar arası 100 karakter tekrar
    separators=["\n\n", "\n", ". ", " ", ""]  # Bölme önceliği
)

chunks = text_splitter.split_documents(documents)

CHUNK SIZE REHBERİ:
- Q&A: 256-512 karakter
- Doküman arama: 512-1024 karakter
- Özetleme: 1024-2048 karakter

OVERLAP KURALI: chunk_size * 0.1-0.2 (10-20%)
"""

# TODO: Dokümanları parçala
# text_splitter = RecursiveCharacterTextSplitter(...)
# chunks = text_splitter.split_documents(documents)
# print(f"Oluşan chunk sayısı: {len(chunks)}")


# ============================================================
# ADIM 3: EMBED (Vektöre Dönüştürme)
# ============================================================
"""
Metinleri sayısal vektörlere çevir:

SEÇENEK 1 - HuggingFace (Ücretsiz):
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'}
)

SEÇENEK 2 - Google (API Key gerekli):
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

TEST:
test_vector = embeddings.embed_query("Test metni")
print(f"Vektör boyutu: {len(test_vector)}")
"""

# TODO: Embedding modelini seç ve oluştur
# embeddings = HuggingFaceEmbeddings(...)
# veya
# embeddings = GoogleGenerativeAIEmbeddings(...)


# ============================================================
# ADIM 4: STORE (Vector Database'e Kaydet)
# ============================================================
"""
Chunk'ları ve embedding'lerini veritabanına kaydet:

from langchain_chroma import Chroma

# Yeni veritabanı oluştur
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="my_rag_collection",
    persist_directory="./chroma_db"  # Diske kaydet (opsiyonel)
)

# Mevcut veritabanını yükle
vectorstore = Chroma(
    collection_name="my_rag_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

DİĞER VECTOR DB SEÇENEKLERİ:
- FAISS: Hızlı, yerel
- Pinecone: Bulut, ölçeklenebilir
- Weaviate: Hibrit arama
- Qdrant: Rust tabanlı, hızlı
"""

# TODO: Vector store oluştur
# vectorstore = Chroma.from_documents(...)


# ============================================================
# ADIM 5: RETRIEVE (Benzer Dokümanları Getir)
# ============================================================
"""
Kullanıcı sorusuna en benzer chunk'ları bul:

YÖNTEM 1 - Doğrudan arama:
results = vectorstore.similarity_search(
    query="Sorum nedir?",
    k=3  # En benzer 3 chunk
)

for doc in results:
    print(doc.page_content)

YÖNTEM 2 - Skor ile arama:
results = vectorstore.similarity_search_with_score(
    query="Sorum nedir?",
    k=3
)

for doc, score in results:
    print(f"Skor: {score:.4f}")
    print(doc.page_content)

YÖNTEM 3 - Retriever olarak kullan:
retriever = vectorstore.as_retriever(
    search_type="similarity",  # veya "mmr"
    search_kwargs={"k": 3}
)

docs = retriever.invoke("Sorum nedir?")
"""

# TODO: Retriever oluştur ve test et
# retriever = vectorstore.as_retriever(...)
# docs = retriever.invoke("Test sorusu")


# ============================================================
# ADIM 6: GENERATE (LLM ile Cevap Üret)
# ============================================================
"""
Bulunan chunk'ları LLM'e vererek cevap üret:

YÖNTEM 1 - Manuel prompt:
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Context oluştur
context = "\n\n".join([doc.page_content for doc in docs])

# Prompt hazırla
prompt = f'''Aşağıdaki bilgilere dayanarak soruyu cevapla.
Bilgiler dışında cevap verme.

BİLGİLER:
{context}

SORU: {query}

CEVAP:'''

response = llm.invoke(prompt)
print(response.content)


YÖNTEM 2 - RetrievalQA Chain (Otomatik):
from langchain.chains import RetrievalQA

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # Tüm chunk'ları birleştir
    retriever=retriever,
    return_source_documents=True
)

result = qa_chain.invoke({"query": "Sorum nedir?"})
print(result["result"])
print(result["source_documents"])


YÖNTEM 3 - Conversational (Sohbet geçmişi ile):
from langchain.chains import ConversationalRetrievalChain

conv_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

chat_history = []
result = conv_chain.invoke({
    "question": "Sorum nedir?",
    "chat_history": chat_history
})
"""

# TODO: LLM ve chain oluştur
# llm = ChatGoogleGenerativeAI(...)
# qa_chain = RetrievalQA.from_chain_type(...)


# ============================================================
# ADIM 7: TAM PIPELINE - HEPSİNİ BİRLEŞTİR
# ============================================================
"""
Tüm adımları bir fonksiyonda topla:

def rag_pipeline(query: str) -> str:
    # 1. Benzer dokümanları bul
    docs = retriever.invoke(query)
    
    # 2. Context oluştur
    context = "\n\n".join([doc.page_content for doc in docs])
    
    # 3. Prompt hazırla
    prompt = f'''Aşağıdaki bilgilere dayanarak cevapla:
    
    {context}
    
    Soru: {query}'''
    
    # 4. LLM'den cevap al
    response = llm.invoke(prompt)
    
    return response.content

# Kullanım
answer = rag_pipeline("Yapay zeka nedir?")
print(answer)
"""

# TODO: Kendi RAG pipeline fonksiyonunu yaz
# def rag_pipeline(query):
#     ...


# ============================================================
# BONUS: STREAMLIT İLE WEB ARAYÜZÜ
# ============================================================
"""
pip install streamlit

streamlit_app.py:
-----------------
import streamlit as st

st.title("📚 RAG Soru-Cevap")

query = st.text_input("Sorunuzu yazın:")

if query:
    with st.spinner("Düşünüyorum..."):
        answer = rag_pipeline(query)
    st.write(answer)

Çalıştır: streamlit run streamlit_app.py
"""


# ============================================================
# ÖZET - RAG CHECKLIST
# ============================================================
"""
□ 1. Kütüphaneleri yükle (pip install ...)
□ 2. .env dosyasında API key'i ayarla
□ 3. Dokümanları yükle (TextLoader, PyPDFLoader)
□ 4. Chunk'lara böl (RecursiveCharacterTextSplitter)
□ 5. Embedding modeli seç (HuggingFace veya Google)
□ 6. Vector DB oluştur (Chroma)
□ 7. Retriever ayarla (as_retriever)
□ 8. LLM bağla (ChatGoogleGenerativeAI)
□ 9. Pipeline oluştur (RetrievalQA veya manuel)
□ 10. Test et ve optimize et

İYİ ÇALIŞMALAR! 🚀
"""
