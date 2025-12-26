"""
RAG - LOAD (Doküman Yükleme)
============================
Farklı dosya formatlarından veri yükleme örnekleri
"""

import os
from dotenv import load_dotenv
load_dotenv()

# ============================================================
# 1. TXT DOSYASI YÜKLEME
# ============================================================

from langchain_community.document_loaders import TextLoader

def load_txt(file_path: str):
    """TXT dosyasını yükle"""
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()
    return documents

# Örnek: docs = load_txt("./veriler/bilgi.txt")


# ============================================================
# 2. PDF DOSYASI YÜKLEME
# ============================================================

from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path: str):
    """PDF dosyasını sayfa sayfa yükle"""
    loader = PyPDFLoader(file_path)
    documents = loader.load()  # Her sayfa ayrı document
    return documents

# Örnek: docs = load_pdf("./veriler/rapor.pdf")


# ============================================================
# 3. WEB SAYFASI YÜKLEME
# ============================================================

from langchain_community.document_loaders import WebBaseLoader

def load_web(url: str):
    """Web sayfasını yükle"""
    loader = WebBaseLoader(url)
    documents = loader.load()
    return documents

# Örnek: docs = load_web("https://tr.wikipedia.org/wiki/Yapay_zeka")


# ============================================================
# 4. DİZİN İÇİNDEKİ TÜM DOSYALARI YÜKLEME
# ============================================================

from langchain_community.document_loaders import DirectoryLoader

def load_directory(dir_path: str, file_pattern: str = "*.txt"):
    """Dizindeki tüm dosyaları yükle"""
    loader = DirectoryLoader(dir_path, glob=file_pattern)
    documents = loader.load()
    return documents

# Örnek: docs = load_directory("./veriler", "*.txt")


# ============================================================
# 5. MARKDOWN DOSYASI YÜKLEME
# ============================================================

from langchain_community.document_loaders import UnstructuredMarkdownLoader

def load_markdown(file_path: str):
    """Markdown dosyasını yükle"""
    loader = UnstructuredMarkdownLoader(file_path)
    documents = loader.load()
    return documents


# ============================================================
# 6. JSON DOSYASI YÜKLEME
# ============================================================

from langchain_community.document_loaders import JSONLoader

def load_json(file_path: str, jq_schema: str = "."):
    """JSON dosyasını yükle"""
    loader = JSONLoader(
        file_path=file_path,
        jq_schema=jq_schema,
        text_content=False
    )
    documents = loader.load()
    return documents


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":
    print("="*50)
    print("DOCUMENT LOADER TEST")
    print("="*50)
    
    # Test metni oluştur
    test_content = """
    Yapay Zeka Nedir?
    
    Yapay zeka (AI), makinelerin insan benzeri zeka 
    göstermesini sağlayan bir bilgisayar bilimi dalıdır.
    
    Makine öğrenmesi, derin öğrenme ve doğal dil işleme
    yapay zekanın alt dallarıdır.
    """
    
    # Test dosyası oluştur
    test_file = "test_doc.txt"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write(test_content)
    
    # Yükle ve göster
    docs = load_txt(test_file)
    
    print(f"Yüklenen doküman sayısı: {len(docs)}")
    print(f"İçerik:\n{docs[0].page_content[:200]}")
    print(f"Metadata: {docs[0].metadata}")
    
    # Test dosyasını sil
    os.remove(test_file)
    
    print("\n✓ Test başarılı!")
