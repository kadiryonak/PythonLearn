"""
Tool Error Handling - LangChain Tool Hata Yönetimi
Bu dosya, LangChain tool'larında hata yönetiminin farklı yöntemlerini gösterir.
"""
import os
from typing import Optional
from langchain_core.tools import tool, ToolException
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import traceback

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(
    api_key=api_key,
    model="llama-3.3-70b-versatile",
)


# ============================================================
# 1. TEMEL HATA YAKALAMA - Try/Except ile
# ============================================================

@tool
def divide_numbers(a: float, b: float) -> str:
    """İki sayıyı böler. Sıfıra bölme hatası yakalayabilir."""
    try:
        if b == 0:
            return "Hata: Sıfıra bölme yapılamaz!"
        result = a / b
        return f"{a} / {b} = {result}"
    except Exception as e:
        return f"Hesaplama hatası: {str(e)}"


# ============================================================
# 2. TOOL EXCEPTION - LangChain'in Özel Hata Sınıfı
# ============================================================

@tool(handle_tool_error=True)
def fetch_user_data(user_id: int) -> str:
    """Kullanıcı verilerini getirir. Geçersiz ID'ler için hata fırlatır."""
    valid_users = {1: "Ali", 2: "Ayşe", 3: "Mehmet"}
    
    if user_id not in valid_users:
        # ToolException kullanarak anlamlı hata mesajı
        raise ToolException(f"Kullanıcı ID '{user_id}' bulunamadı. Geçerli ID'ler: 1, 2, 3")
    
    return f"Kullanıcı bulundu: {valid_users[user_id]}"


# ============================================================
# 3. CUSTOM ERROR HANDLER - Özel Hata İşleyici Fonksiyon
# ============================================================

def custom_error_handler(error: ToolException) -> str:
    """Tool hatalarını özelleştirilmiş şekilde işler."""
    return f"⚠️ İşlem başarısız: {error.args[0]}\n💡 Lütfen geçerli parametreler kullanın."


@tool(handle_tool_error=custom_error_handler)
def get_weather_data(city: str) -> str:
    """Şehir hava durumunu getirir. Bilinmeyen şehirler için hata fırlatır."""
    weather_db = {
        "istanbul": "Parçalı bulutlu, 18°C",
        "ankara": "Güneşli, 15°C",
        "izmir": "Açık, 22°C",
    }
    
    city_lower = city.lower().strip()
    if city_lower not in weather_db:
        raise ToolException(f"'{city}' şehri veritabanında yok. Desteklenen şehirler: İstanbul, Ankara, İzmir")
    
    return f"🌤️ {city}: {weather_db[city_lower]}"


# ============================================================
# 4. RETRY MEKANİZMASI - Hata Durumunda Tekrar Deneme
# ============================================================

class RetryableTool:
    """Hata durumunda tekrar deneyen tool wrapper."""
    
    def __init__(self, max_retries: int = 3):
        self.max_retries = max_retries
        self.attempt_count = 0
    
    def reset(self):
        self.attempt_count = 0


retry_state = RetryableTool(max_retries=3)


@tool
def unstable_api_call(query: str) -> str:
    """Bazen başarısız olan bir API çağrısını simüle eder."""
    import random
    
    retry_state.attempt_count += 1
    
    # %50 başarısızlık şansı (ilk 2 denemede)
    if retry_state.attempt_count < 3 and random.random() < 0.5:
        return f"⏳ Deneme {retry_state.attempt_count}/{retry_state.max_retries} başarısız. Tekrar deneyin."
    
    retry_state.reset()
    return f"✅ API başarılı! Sonuç: '{query}' için veri getirildi."


# ============================================================
# 5. VALIDATION - Parametre Doğrulama
# ============================================================

@tool
def send_email(to: str, subject: str, body: str) -> str:
    """E-posta gönderir. Parametreleri doğrular."""
    errors = []
    
    # E-posta validasyonu
    if not to or "@" not in to:
        errors.append("Geçersiz e-posta adresi")
    
    # Konu validasyonu
    if not subject or len(subject) < 3:
        errors.append("Konu en az 3 karakter olmalı")
    
    # İçerik validasyonu  
    if not body or len(body) < 10:
        errors.append("İçerik en az 10 karakter olmalı")
    
    if errors:
        return f"❌ Doğrulama hatası:\n" + "\n".join(f"  • {e}" for e in errors)
    
    return f"✅ E-posta gönderildi!\n  📧 Alıcı: {to}\n  📝 Konu: {subject}"


# ============================================================
# 6. FALLBACK - Yedek Tool Mekanizması
# ============================================================

@tool
def primary_search(query: str) -> str:
    """Ana arama motoru. Başarısız olursa yedek kullanılır."""
    # Bazı sorgular için başarısız ol (simülasyon)
    if "test" in query.lower():
        raise ToolException("Ana arama motoru geçici olarak kullanılamıyor")
    return f"🔍 Ana arama sonucu: '{query}' için 10 sonuç bulundu"


@tool
def fallback_search(query: str) -> str:
    """Yedek arama motoru. Her zaman çalışır."""
    return f"🔄 Yedek arama sonucu: '{query}' için 5 sonuç bulundu"


def search_with_fallback(query: str) -> str:
    """Ana arama başarısız olursa yedek kullanır."""
    try:
        return primary_search.invoke(query)
    except Exception as e:
        print(f"⚠️ Ana arama başarısız: {e}")
        print("🔄 Yedek aramaya geçiliyor...")
        return fallback_search.invoke(query)


# ============================================================
# 7. AGENT İLE HATA YÖNETİMİ
# ============================================================

def run_tool_with_agent():
    """Model ile tool çağrısı ve hata yönetimi."""
    
    tools = [divide_numbers, fetch_user_data, get_weather_data, send_email]
    model_with_tools = model.bind_tools(tools)
    
    test_messages = [
        "10'u 0'a böl",
        "5 numaralı kullanıcıyı getir",
        "Bursa'nın hava durumunu söyle",
        "test@email.com adresine 'Merhaba' konulu bir e-posta gönder",
    ]
    
    print("\n" + "=" * 60)
    print("AGENT İLE TOOL HATA YÖNETİMİ TESTİ")
    print("=" * 60)
    
    for msg in test_messages:
        print(f"\n📝 Kullanıcı: {msg}")
        print("-" * 40)
        
        response = model_with_tools.invoke([
            SystemMessage(content="Sen yardımcı bir asistansın. Tool'ları kullanarak soruları yanıtla."),
            HumanMessage(content=msg)
        ])
        
        if response.tool_calls:
            for tool_call in response.tool_calls:
                tool_name = tool_call['name']
                tool_args = tool_call['args']
                print(f"🔧 Tool: {tool_name}")
                print(f"📥 Args: {tool_args}")
                
                # Tool'u çalıştır
                try:
                    tool_map = {
                        'divide_numbers': divide_numbers,
                        'fetch_user_data': fetch_user_data,
                        'get_weather_data': get_weather_data,
                        'send_email': send_email,
                    }
                    result = tool_map[tool_name].invoke(tool_args)
                    print(f"📤 Sonuç: {result}")
                except Exception as e:
                    print(f"❌ Hata: {e}")
        else:
            print(f"💬 Model yanıtı: {response.content}")


# ============================================================
# TESTLER
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("LANGCHAIN TOOL HATA YÖNETİMİ ÖRNEKLERİ")
    print("=" * 60)
    
    # Test 1: Temel hata yakalama
    print("\n📌 Test 1: Sıfıra Bölme")
    print(divide_numbers.invoke({"a": 10, "b": 0}))
    print(divide_numbers.invoke({"a": 10, "b": 2}))
    
    # Test 2: ToolException
    print("\n📌 Test 2: Geçersiz Kullanıcı")
    print(fetch_user_data.invoke({"user_id": 1}))
    print(fetch_user_data.invoke({"user_id": 99}))
    
    # Test 3: Custom error handler
    print("\n📌 Test 3: Bilinmeyen Şehir")
    print(get_weather_data.invoke({"city": "istanbul"}))
    print(get_weather_data.invoke({"city": "londra"}))
    
    # Test 4: Parametre validasyonu
    print("\n📌 Test 4: E-posta Validasyonu")
    print(send_email.invoke({"to": "test@mail.com", "subject": "Merhaba", "body": "Bu bir test mesajıdır."}))
    print(send_email.invoke({"to": "invalid", "subject": "AB", "body": "Kısa"}))
    
    # Test 5: Fallback mekanizması
    print("\n📌 Test 5: Fallback Arama")
    print(search_with_fallback("python öğren"))
    print(search_with_fallback("test sorgusu"))
    
    # Test 6: Agent ile test
    run_tool_with_agent()
