"""
RAG - DATABASE (Vector Store İşlemleri)
=======================================
Chroma ve diğer vector database işlemleri
"""

import os
from dotenv import load_dotenv
load_dotenv()


# 1. CHROMA VECTOR STORE

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document

# Embedding modeli
def get_embeddings():
    """HuggingFace embedding modeli döndür"""
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )




def create_vectorstore(documents: list, collection_name: str = "default"):
    embeddings = get_embeddings()
    
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name=collection_name
    )
    
    return vectorstore



def create_persistent_vectorstore(
    documents: list,
    persist_directory: str = "./chroma_db",
    collection_name: str = "my_collection"
):
    """Diske kaydedilen vector store oluştur"""
    embeddings = get_embeddings()
    
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name=collection_name,
        persist_directory=persist_directory
    )
    
    print(f"✓ {len(documents)} doküman kaydedildi: {persist_directory}")
    return vectorstore


# ============================================================
# 4. MEVCUT VECTOR STORE'U YÜKLE
# ============================================================

def load_vectorstore(
    persist_directory: str = "./chroma_db",
    collection_name: str = "my_collection"
):
    """Mevcut vector store'u yükle"""
    embeddings = get_embeddings()
    
    vectorstore = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=persist_directory
    )
    
    print(f"✓ Vector store yüklendi: {persist_directory}")
    return vectorstore


# ============================================================
# 5. DOKÜMAN EKLEME
# ============================================================

def add_documents(vectorstore, documents: list):
    """Mevcut vector store'a doküman ekle"""
    vectorstore.add_documents(documents)
    print(f"✓ {len(documents)} doküman eklendi")
    return vectorstore


def similarity_search(vectorstore, query: str, k: int = 3):
    """Sorguya en benzer dokümanları bul"""
    results = vectorstore.similarity_search(query, k=k)
    return results


def similarity_search_with_scores(vectorstore, query: str, k: int = 3):
    """Sorguya en benzer dokümanları skor ile bul"""
    results = vectorstore.similarity_search_with_score(query, k=k)
    return results




def get_retriever(vectorstore, k: int = 3, search_type: str = "similarity"):
    """Vector store'dan retriever oluştur"""
    retriever = vectorstore.as_retriever(
        search_type=search_type,  # "similarity" veya "mmr"
        search_kwargs={"k": k}
    )
    return retriever


# ============================================================
# 8. KOLEKSİYON SİL
# ============================================================

def delete_collection(persist_directory: str, collection_name: str):
    """Koleksiyonu sil"""
    import shutil
    if os.path.exists(persist_directory):
        shutil.rmtree(persist_directory)
        print(f"✓ Koleksiyon silindi: {collection_name}")


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":
    print("="*50)
    print("VECTOR DATABASE TEST")
    print("="*50)
    
    # Test dokümanları
    documents = [
        Document(page_content="Yapay zeka makinelerin düşünmesidir.", metadata={"source": "ai.txt"}),
        Document(page_content="Python programlama dilidir.", metadata={"source": "python.txt"}),
        Document(page_content="Makine öğrenmesi verileri analiz eder.", metadata={"source": "ml.txt"}),
    ]
    
    # Vector store oluştur
    print("\n1. Vector store oluşturuluyor...")
    vectorstore = create_vectorstore(documents, "test_collection")
    print(f"✓ {len(documents)} doküman eklendi")
    
    # Arama yap
    print("\n2. Benzerlik araması yapılıyor...")
    query = "yapay zeka nedir?"
    results = similarity_search(vectorstore, query, k=2)
    
    print(f"Sorgu: '{query}'")
    print("Sonuçlar:")
    for i, doc in enumerate(results):
        print(f"  [{i+1}] {doc.page_content}")
    
    # Skor ile arama
    print("\n3. Skor ile arama...")
    results_with_scores = similarity_search_with_scores(vectorstore, query, k=2)
    
    for doc, score in results_with_scores:
        print(f"  Skor: {score:.4f} | {doc.page_content}")
    
    print("\n✓ Test tamamlandı!")
