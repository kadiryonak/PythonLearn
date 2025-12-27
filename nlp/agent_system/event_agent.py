"""
ERÜ Yapay Zeka Kulübü - Etkinlik Agent
Web sayfasından etkinlikleri çeker, tarihe göre aktif/pasif belirler ve LLM ile kullanıcıya sunar.
"""
import asyncio
import os
from datetime import datetime
from dataclasses import dataclass
from typing import Optional
from playwright.async_api import async_playwright
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# LLM Model
llm = ChatGroq(
    api_key=api_key,
    model="llama-3.3-70b-versatile",
)


@dataclass
class Event:
    """Etkinlik veri yapısı."""
    title: str
    date: Optional[datetime]
    date_str: str
    description: str
    is_active: bool
    status: str  # "Aktif", "Tamamlandı", "Yaklaşıyor"


# Global etkinlik listesi
events_cache: list[Event] = []


async def scrape_events() -> list[Event]:
    """Etkinlikler sayfasından etkinlikleri çeker."""
    events = []
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # Görünmez mod
        page = await browser.new_page()
        
        try:
            print("🔍 Etkinlikler sayfasına gidiliyor...")
            await page.goto("https://erciyesyapayzeka.com.tr/etkinlikler")
            await asyncio.sleep(2)
            
            # Sayfa içeriğini kontrol et
            content = await page.inner_text("body")
            print(f"📄 Sayfa yüklendi. İçerik uzunluğu: {len(content)} karakter")
            
            # Etkinlik kartlarını bul (site yapısına göre selector değişebilir)
            # Önce sayfayı inceleyelim
            
            # Tüm metin içeriğini al
            full_text = await page.inner_text("body")
            
            # Tarih formatlarını bul (örn: 15 Ocak 2025, 2025-01-15, etc.)
            import re
            
            # Türkçe ay isimleri
            months_tr = {
                'ocak': 1, 'şubat': 2, 'mart': 3, 'nisan': 4,
                'mayıs': 5, 'haziran': 6, 'temmuz': 7, 'ağustos': 8,
                'eylül': 9, 'ekim': 10, 'kasım': 11, 'aralık': 12
            }
            
            # Etkinlik kartlarını bulmaya çalış
            cards = await page.query_selector_all(".card, .event, .etkinlik, article, .event-card")
            
            if cards:
                print(f"📋 {len(cards)} etkinlik kartı bulundu")
                for card in cards:
                    try:
                        title_el = await card.query_selector("h2, h3, h4, .title, .card-title")
                        title = await title_el.inner_text() if title_el else "Bilinmeyen Etkinlik"
                        
                        date_el = await card.query_selector(".date, .tarih, time, .event-date")
                        date_str = await date_el.inner_text() if date_el else ""
                        
                        desc_el = await card.query_selector("p, .description, .card-text")
                        description = await desc_el.inner_text() if desc_el else ""
                        
                        # Tarihi parse et
                        event_date = parse_turkish_date(date_str) if date_str else None
                        is_active, status = check_event_status(event_date)
                        
                        events.append(Event(
                            title=title.strip(),
                            date=event_date,
                            date_str=date_str.strip(),
                            description=description.strip()[:200],
                            is_active=is_active,
                            status=status
                        ))
                    except Exception as e:
                        print(f"⚠️ Kart parse hatası: {e}")
            else:
                # Kart bulunamadıysa sayfa içeriğini analiz et
                print("ℹ️ Etkinlik kartı bulunamadı, sayfa içeriği analiz ediliyor...")
                
                # Sayfadaki tüm başlıkları al
                headings = await page.query_selector_all("h1, h2, h3, h4")
                for heading in headings:
                    text = await heading.inner_text()
                    print(f"  📌 Başlık: {text}")
                
                # Örnek etkinlik ekle (demo amaçlı)
                events.append(Event(
                    title="Demo Etkinlik - Python Workshop",
                    date=datetime(2025, 1, 15, 14, 0),
                    date_str="15 Ocak 2025, 14:00",
                    description="Python programlama dili üzerine workshop. Başlangıç seviyesi.",
                    is_active=True,
                    status="Yaklaşıyor"
                ))
                events.append(Event(
                    title="Demo Etkinlik - AI Semineri",
                    date=datetime(2024, 12, 20, 10, 0),
                    date_str="20 Aralık 2024, 10:00",
                    description="Yapay zeka ve makine öğrenmesi semineri.",
                    is_active=False,
                    status="Tamamlandı"
                ))
            
        except Exception as e:
            print(f"❌ Scraping hatası: {e}")
            import traceback
            traceback.print_exc()
        
        finally:
            await browser.close()
    
    return events


def parse_turkish_date(date_str: str) -> Optional[datetime]:
    """Türkçe tarih string'ini datetime'a çevirir."""
    import re
    
    months_tr = {
        'ocak': 1, 'şubat': 2, 'mart': 3, 'nisan': 4,
        'mayıs': 5, 'haziran': 6, 'temmuz': 7, 'ağustos': 8,
        'eylül': 9, 'ekim': 10, 'kasım': 11, 'aralık': 12
    }
    
    date_str = date_str.lower().strip()
    
    # "15 Ocak 2025" formatı
    pattern = r'(\d{1,2})\s+(\w+)\s+(\d{4})'
    match = re.search(pattern, date_str)
    if match:
        day = int(match.group(1))
        month_name = match.group(2)
        year = int(match.group(3))
        month = months_tr.get(month_name, 1)
        
        # Saat bilgisi varsa ekle
        time_pattern = r'(\d{1,2}):(\d{2})'
        time_match = re.search(time_pattern, date_str)
        hour, minute = (int(time_match.group(1)), int(time_match.group(2))) if time_match else (0, 0)
        
        try:
            return datetime(year, month, day, hour, minute)
        except ValueError:
            return None
    
    # "2025-01-15" formatı
    iso_pattern = r'(\d{4})-(\d{2})-(\d{2})'
    iso_match = re.search(iso_pattern, date_str)
    if iso_match:
        try:
            return datetime(int(iso_match.group(1)), int(iso_match.group(2)), int(iso_match.group(3)))
        except ValueError:
            return None
    
    return None


def check_event_status(event_date: Optional[datetime]) -> tuple[bool, str]:
    """Etkinliğin aktif olup olmadığını kontrol eder."""
    if event_date is None:
        return False, "Tarih belirsiz"
    
    now = datetime.now()
    
    if event_date < now:
        return False, "Tamamlandı"
    elif (event_date - now).days <= 7:
        return True, "Yaklaşıyor (Bu Hafta!)"
    elif (event_date - now).days <= 30:
        return True, "Yaklaşıyor"
    else:
        return True, "Planlandı"


def format_events_for_llm(events: list[Event]) -> str:
    """Etkinlikleri LLM için formatlı string'e çevirir."""
    if not events:
        return "Şu anda kayıtlı etkinlik bulunmamaktadır."
    
    now = datetime.now()
    output = f"📅 Şu anki tarih: {now.strftime('%d %B %Y, %H:%M')}\n\n"
    
    active_events = [e for e in events if e.is_active]
    past_events = [e for e in events if not e.is_active]
    
    if active_events:
        output += "🟢 AKTİF/YAKLASAN ETKİNLİKLER:\n"
        output += "-" * 40 + "\n"
        for e in active_events:
            output += f"📌 {e.title}\n"
            output += f"   📆 Tarih: {e.date_str}\n"
            output += f"   📊 Durum: {e.status}\n"
            if e.description:
                output += f"   📝 Açıklama: {e.description}\n"
            output += "\n"
    else:
        output += "🟡 Şu anda aktif etkinlik bulunmamaktadır.\n\n"
    
    if past_events:
        output += "🔴 GEÇMİŞ ETKİNLİKLER:\n"
        output += "-" * 40 + "\n"
        for e in past_events[:3]:  # Son 3 geçmiş etkinlik
            output += f"📌 {e.title} ({e.date_str}) - {e.status}\n"
    
    return output


@tool
def get_active_events() -> str:
    """Aktif ve yaklaşan etkinlikleri getirir. Kullanıcı etkinlik, seminer, workshop sorduğunda kullanılır."""
    global events_cache
    
    if not events_cache:
        return "Etkinlik verisi henüz yüklenmedi. Lütfen önce etkinlikleri yükleyin."
    
    return format_events_for_llm(events_cache)


@tool
def get_current_datetime() -> str:
    """Şu anki tarih ve saati döndürür."""
    now = datetime.now()
    return f"Şu anki tarih ve saat: {now.strftime('%d %B %Y, %A, %H:%M:%S')}"


async def run_event_agent():
    """Ana agent fonksiyonu."""
    global events_cache
    
    print("=" * 60)
    print("🤖 ERÜ YAPAY ZEKA KULÜBÜ - ETKİNLİK AGENT")
    print("=" * 60)
    
    # 1. Etkinlikleri web'den çek
    print("\n📥 Etkinlikler web sitesinden çekiliyor...")
    events_cache = await scrape_events()
    print(f"✅ {len(events_cache)} etkinlik bulundu!\n")
    
    # 2. Etkinlikleri göster
    print(format_events_for_llm(events_cache))
    
    # 3. LLM ile sohbet
    tools = [get_active_events, get_current_datetime]
    model_with_tools = llm.bind_tools(tools)
    
    # Kullanıcı sorgusu
    user_query = "Aktif etkinlikler neler? Bu hafta katılabileceğim bir etkinlik var mı?"
    
    print("=" * 60)
    print(f"👤 Kullanıcı: {user_query}")
    print("=" * 60)
    
    # Sistem mesajı ile etkinlik bilgisini ekle
    events_info = format_events_for_llm(events_cache)
    
    response = llm.invoke([
        SystemMessage(content=f"""Sen ERÜ Yapay Zeka Kulübü'nün yardımcı asistanısın.
Kullanıcılara etkinlikler hakkında bilgi veriyorsun.

İşte güncel etkinlik bilgileri:
{events_info}

Kullanıcının sorularını bu bilgilere göre yanıtla. 
Türkçe yanıt ver. Samimi ve yardımsever ol."""),
        HumanMessage(content=user_query)
    ])
    
    print(f"\n🤖 Asistan: {response.content}")


if __name__ == "__main__":
    asyncio.run(run_event_agent())
