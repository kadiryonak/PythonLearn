"""
RAG - GENERATE (Cevap Üretme)
=============================
Bulunan dokümanlarla LLM'den cevap üretme
"""

import os
from dotenv import load_dotenv
load_dotenv()

# ============================================================
# 1. LLM OLUŞTUR
# ============================================================

from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm(model: str = "gemini-2.0-flash", temperature: float = 0.7):
    """Google Gemini LLM oluştur"""
    api_key = os.getenv("GOOGLE_API_KEY")
    
    llm = ChatGoogleGenerativeAI(
        model=model,
        google_api_key=api_key,
        temperature=temperature,
        max_tokens=1024
    )
    
    return llm


# ============================================================
# 2. MANUEL RAG CEVAP ÜRETME
# ============================================================

def generate_manual(llm, query: str, documents: list) -> str:
    """
    Manuel prompt ile cevap üret
    
    En esnek yöntem - prompt'u tam kontrol edersin.
    """
    # Context oluştur
    context = "\n\n---\n\n".join([doc.page_content for doc in documents])
    
    # Prompt hazırla
    prompt = f"""Aşağıdaki bilgilere dayanarak soruyu cevapla.
Sadece verilen bilgileri kullan. Bilmiyorsan "bilmiyorum" de.

BİLGİLER:
{context}

SORU: {query}

CEVAP:"""
    
    # LLM'den cevap al
    response = llm.invoke(prompt)
    
    return response.content


# ============================================================
# 3. RETRIEVAL QA CHAIN
# ============================================================

from langchain.chains import RetrievalQA

def create_qa_chain(llm, retriever, chain_type: str = "stuff"):
    """
    RetrievalQA chain oluştur
    
    chain_type seçenekleri:
    - "stuff": Tüm dokümanları birleştir (default, hızlı)
    - "map_reduce": Her dokümanı ayrı işle, sonra birleştir
    - "refine": Sırayla işle, her seferinde cevabı geliştir
    - "map_rerank": Her dokümanı ayrı işle, en iyisini seç
    """
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type=chain_type,
        retriever=retriever,
        return_source_documents=True
    )
    
    return qa_chain


def ask_qa_chain(qa_chain, query: str):
    """QA chain ile soru sor"""
    result = qa_chain.invoke({"query": query})
    
    answer = result["result"]
    sources = result["source_documents"]
    
    return answer, sources


# ============================================================
# 4. CONVERSATIONAL CHAIN (Sohbet Geçmişi ile)
# ============================================================

from langchain.chains import ConversationalRetrievalChain

def create_conversational_chain(llm, retriever):
    """
    Sohbet geçmişini hatırlayan chain
    
    Önceki sorular ve cevaplar bağlamda kalır.
    """
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        verbose=False
    )
    
    return chain


def ask_conversational(chain, query: str, chat_history: list):
    """
    Sohbet geçmişi ile soru sor
    
    chat_history: [(soru1, cevap1), (soru2, cevap2), ...]
    """
    result = chain.invoke({
        "question": query,
        "chat_history": chat_history
    })
    
    answer = result["answer"]
    sources = result["source_documents"]
    
    # Geçmişe ekle
    chat_history.append((query, answer))
    
    return answer, sources, chat_history


# ============================================================
# 5. CUSTOM PROMPT İLE CHAIN
# ============================================================

from langchain.prompts import PromptTemplate

def create_custom_qa_chain(llm, retriever, custom_prompt: str = None):
    """
    Özel prompt şablonu ile chain oluştur
    
    {context} ve {question} placeholders kullanılmalı.
    """
    if custom_prompt is None:
        custom_prompt = """Sen yardımcı bir asistansın.
Aşağıdaki bağlam bilgilerini kullanarak soruyu cevapla.
Bağlamda yoksa "Bu bilgi mevcut değil" de.

BAĞLAM:
{context}

SORU: {question}

DETAYLI CEVAP:"""
    
    prompt_template = PromptTemplate(
        template=custom_prompt,
        input_variables=["context", "question"]
    )
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt_template}
    )
    
    return qa_chain


# ============================================================
# 6. STREAMING CEVAP
# ============================================================

def generate_streaming(llm, query: str, documents: list):
    """
    Cevabı stream olarak üret (anlık görüntüleme)
    """
    context = "\n\n".join([doc.page_content for doc in documents])
    
    prompt = f"""Bilgiler: {context}

Soru: {query}

Cevap:"""
    
    print("Cevap: ", end="", flush=True)
    
    full_response = ""
    for chunk in llm.stream(prompt):
        print(chunk.content, end="", flush=True)
        full_response += chunk.content
    
    print()  # Yeni satır
    return full_response


# ============================================================
# 7. TAM RAG PIPELINE
# ============================================================

class RAGPipeline:
    """Tam RAG pipeline sınıfı"""
    
    def __init__(self, vectorstore, llm=None):
        self.vectorstore = vectorstore
        self.llm = llm or get_llm()
        self.retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        self.chat_history = []
    
    def ask(self, query: str, stream: bool = False) -> str:
        """Soru sor ve cevap al"""
        # Dokümanları bul
        docs = self.retriever.invoke(query)
        
        # Cevap üret
        if stream:
            return generate_streaming(self.llm, query, docs)
        else:
            return generate_manual(self.llm, query, docs)
    
    def ask_with_sources(self, query: str):
        """Soru sor ve kaynakları da döndür"""
        docs = self.retriever.invoke(query)
        answer = generate_manual(self.llm, query, docs)
        
        return {
            "answer": answer,
            "sources": [doc.metadata for doc in docs],
            "documents": docs
        }
    
    def chat(self, query: str) -> str:
        """Sohbet geçmişi ile soru sor"""
        # Context'e geçmiş ekle
        history_text = "\n".join([f"S: {q}\nC: {a}" for q, a in self.chat_history])
        
        docs = self.retriever.invoke(query)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        prompt = f"""Sohbet Geçmişi:
{history_text}

Bilgiler:
{context}

Yeni Soru: {query}

Cevap:"""
        
        answer = self.llm.invoke(prompt).content
        self.chat_history.append((query, answer))
        
        return answer
    
    def clear_history(self):
        """Sohbet geçmişini temizle"""
        self.chat_history = []


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":
    print("="*50)
    print("RAG GENERATE TEST")
    print("="*50)
    
    from langchain_chroma import Chroma
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain.schema import Document
    
    # Test dokümanları
    documents = [
        Document(page_content="Python 1991'de Guido van Rossum tarafından oluşturuldu."),
        Document(page_content="Python kolay öğrenilen ve okunaklı bir dildir."),
        Document(page_content="Python veri bilimi ve yapay zekada çok kullanılır."),
    ]
    
    # Embedding ve vectorstore
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(documents, embeddings)
    
    print("\n1. Manuel cevap üretme testi...")
    
    # LLM ve retriever
    try:
        llm = get_llm()
        retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
        
        # Manuel test
        query = "Python'u kim oluşturdu?"
        docs = retriever.invoke(query)
        answer = generate_manual(llm, query, docs)
        
        print(f"Sorgu: {query}")
        print(f"Cevap: {answer}")
        
    except Exception as e:
        print(f"LLM hatası (API key kontrol edin): {e}")
    
    print("\n✓ Test tamamlandı!")
