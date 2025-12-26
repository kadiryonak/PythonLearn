"""
RAG - RETRIEVE (Doküman Getirme)
================================
Vector store'dan benzer dokümanları bulma
"""

import os
from dotenv import load_dotenv
load_dotenv()

# ============================================================
# 1. TEMEL RETRIEVER
# ============================================================

def create_basic_retriever(vectorstore, k: int = 3):
    """
    Temel similarity retriever oluştur
    
    k: Döndürülecek doküman sayısı
    """
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": k}
    )
    return retriever


# ============================================================
# 2. MMR RETRIEVER (Maximum Marginal Relevance)
# ============================================================

def create_mmr_retriever(vectorstore, k: int = 3, fetch_k: int = 10):
    """
    MMR retriever - Hem benzerlik hem çeşitlilik sağlar
    
    fetch_k: İlk aşamada getirilecek doküman sayısı
    k: Sonuçta döndürülecek doküman sayısı (fetch_k'dan seçilir)
    
    MMR, benzer ama birbirinden farklı dokümanlar seçer.
    Tek tip sonuç yerine çeşitlilik sağlar.
    """
    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": k,
            "fetch_k": fetch_k
        }
    )
    return retriever


# ============================================================
# 3. SKOR FİLTRELİ RETRIEVER
# ============================================================

def create_threshold_retriever(vectorstore, k: int = 3, score_threshold: float = 0.5):
    """
    Belirli skor eşiğinin üstündeki dokümanları getir
    
    score_threshold: Minimum benzerlik skoru (0-1 arası)
    """
    retriever = vectorstore.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": k,
            "score_threshold": score_threshold
        }
    )
    return retriever


# ============================================================
# 4. FİLTRELİ RETRIEVER (Metadata bazlı)
# ============================================================

def create_filtered_retriever(vectorstore, k: int = 3, filter_dict: dict = None):
    """
    Metadata filtresi ile doküman getir
    
    filter_dict: {"source": "file.txt"} gibi filtre
    """
    search_kwargs = {"k": k}
    
    if filter_dict:
        search_kwargs["filter"] = filter_dict
    
    retriever = vectorstore.as_retriever(
        search_kwargs=search_kwargs
    )
    return retriever


# ============================================================
# 5. CONTEXTUAL COMPRESSION RETRIEVER
# ============================================================

def create_compression_retriever(vectorstore, llm, k: int = 5):
    """
    Bulunan dokümanları LLM ile sıkıştır/özetle
    
    Sadece soruyla ilgili kısımları döndürür.
    """
    from langchain.retrievers import ContextualCompressionRetriever
    from langchain.retrievers.document_compressors import LLMChainExtractor
    
    base_retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    
    compressor = LLMChainExtractor.from_llm(llm)
    
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor,
        base_retriever=base_retriever
    )
    
    return compression_retriever


# ============================================================
# 6. MULTI-QUERY RETRIEVER
# ============================================================

def create_multi_query_retriever(vectorstore, llm):
    """
    Soruyu farklı şekillerde yeniden yaz ve ara
    
    Tek soru yerine 3-5 varyasyon oluşturur.
    Daha kapsamlı sonuçlar döner.
    """
    from langchain.retrievers.multi_query import MultiQueryRetriever
    
    base_retriever = vectorstore.as_retriever()
    
    retriever = MultiQueryRetriever.from_llm(
        retriever=base_retriever,
        llm=llm
    )
    
    return retriever


# ============================================================
# 7. RERANK RETRIEVER
# ============================================================

def rerank_documents(docs: list, query: str, top_k: int = 3):
    """
    Bulunan dokümanları yeniden sırala
    
    Cross-encoder ile daha doğru sıralama yapar.
    pip install sentence-transformers gerekli.
    """
    try:
        from sentence_transformers import CrossEncoder
        
        # Cross-encoder modeli
        model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
        
        # Her doküman için skor hesapla
        pairs = [[query, doc.page_content] for doc in docs]
        scores = model.predict(pairs)
        
        # Skora göre sırala
        scored_docs = list(zip(docs, scores))
        scored_docs.sort(key=lambda x: x[1], reverse=True)
        
        # En iyi k tanesini döndür
        return [doc for doc, score in scored_docs[:top_k]]
        
    except ImportError:
        print("sentence-transformers yüklü değil. pip install sentence-transformers")
        return docs[:top_k]


# ============================================================
# 8. HYBRID SEARCH (BM25 + Semantic)
# ============================================================

def create_hybrid_retriever(vectorstore, documents, k: int = 3):
    """
    BM25 (keyword) + Semantic arama birleştir
    
    Hem kelime eşleşmesi hem anlam benzerliği kullanır.
    """
    from langchain.retrievers import BM25Retriever, EnsembleRetriever
    
    # BM25 (keyword based) retriever
    bm25_retriever = BM25Retriever.from_documents(documents)
    bm25_retriever.k = k
    
    # Semantic retriever
    semantic_retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    
    # Ensemble (birleştir)
    ensemble_retriever = EnsembleRetriever(
        retrievers=[bm25_retriever, semantic_retriever],
        weights=[0.5, 0.5]  # Eşit ağırlık
    )
    
    return ensemble_retriever


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":
    print("="*50)
    print("RETRIEVER TEST")
    print("="*50)
    
    from langchain_chroma import Chroma
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain.schema import Document
    
    # Embedding
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    # Test dokümanları
    documents = [
        Document(page_content="Python hızlı ve kolay bir programlama dilidir.", metadata={"topic": "python"}),
        Document(page_content="Yapay zeka makinelerin düşünmesini sağlar.", metadata={"topic": "ai"}),
        Document(page_content="Makine öğrenmesi verileri analiz eder.", metadata={"topic": "ml"}),
        Document(page_content="Derin öğrenme sinir ağları kullanır.", metadata={"topic": "dl"}),
        Document(page_content="NLP metin işleme teknolojisidir.", metadata={"topic": "nlp"}),
    ]
    
    # Vector store
    vectorstore = Chroma.from_documents(documents, embeddings)
    
    # Retriever oluştur
    retriever = create_basic_retriever(vectorstore, k=2)
    
    # Test
    query = "yapay zeka nedir?"
    results = retriever.invoke(query)
    
    print(f"\nSorgu: '{query}'")
    print("Sonuçlar:")
    for i, doc in enumerate(results):
        print(f"  [{i+1}] {doc.page_content}")
    
    print("\n✓ Test tamamlandı!")
