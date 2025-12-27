"""
Playwright Tool Agent - Web Otomasyon Örneği
LangChain ile Playwright tool'larını kullanarak web sayfalarını otomatize eder.
"""
import asyncio
from playwright.async_api import async_playwright


async def main():
    """Ana fonksiyon - Playwright ile web sayfası otomasyon örneği."""
    
    async with async_playwright() as p:
        # Tarayıcıyı başlat (headless=False görünür modda)
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        try:
            print("=" * 60)
            print("1. Web sitesine gidiliyor...")
            print("=" * 60)
            await page.goto("https://erciyesyapayzeka.com.tr/")
            await asyncio.sleep(2)
            print("✅ Sayfa yüklendi!")
            
            print("\n" + "=" * 60)
            print("2. Mevcut sayfa URL'si:")
            print("=" * 60)
            print(f"📍 URL: {page.url}")
            
            print("\n" + "=" * 60)
            print("3. Sayfa başlığı:")
            print("=" * 60)
            title = await page.title()
            print(f"📝 Başlık: {title}")
            
            print("\n" + "=" * 60)
            print("4. Sayfadaki metinler çıkarılıyor...")
            print("=" * 60)
            # Body içindeki tüm metni al
            text_content = await page.inner_text("body")
            # İlk 500 karakteri göster
            preview = text_content[:500].replace("\n", " ").strip()
            print(f"📄 İçerik önizleme: {preview}...")
            
            print("\n" + "=" * 60)
            print("5. Sayfadaki linkler çıkarılıyor...")
            print("=" * 60)
            links = await page.query_selector_all("a")
            print(f"🔗 Toplam {len(links)} link bulundu:")
            for i, link in enumerate(links[:5]):  # İlk 5 linki göster
                href = await link.get_attribute("href")
                text = await link.inner_text()
                text = text.strip()[:30] if text else "(boş)"
                print(f"   {i+1}. {text} -> {href}")
            
            print("\n" + "=" * 60)
            print("6. Bir butona tıklanıyor...")
            print("=" * 60)
            # Sayfada bir link varsa tıkla
            first_link = await page.query_selector("nav a")
            if first_link:
                link_text = await first_link.inner_text()
                print(f"🖱️ '{link_text}' linkine tıklanıyor...")
                await first_link.click()
                await asyncio.sleep(2)
                print(f"✅ Yeni sayfa: {page.url}")
            else:
                print("⚠️ Tıklanacak link bulunamadı")
            
            print("\n" + "=" * 60)
            print("7. Geri gidiliyor...")
            print("=" * 60)
            await page.go_back()
            await asyncio.sleep(1)
            print(f"✅ Geri dönüldü: {page.url}")
            
            print("\n" + "=" * 60)
            print("8. Ekran görüntüsü alınıyor...")
            print("=" * 60)
            await page.screenshot(path="screenshot.png")
            print("📸 Ekran görüntüsü kaydedildi: screenshot.png")
            
            print("\n" + "=" * 60)
            print("✅ İşlemler tamamlandı!")
            print("=" * 60)
            
            # Tarayıcıyı 3 saniye açık tut (görmek için)
            await asyncio.sleep(3)
            
        except Exception as e:
            print(f"❌ Hata oluştu: {e}")
            import traceback
            traceback.print_exc()
        
        finally:
            await browser.close()
            print("🔒 Tarayıcı kapatıldı.")


if __name__ == "__main__":
    asyncio.run(main())