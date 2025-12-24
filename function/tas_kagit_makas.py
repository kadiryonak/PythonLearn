# ==========================================
# TAŞ KAĞIT MAKAS OYUNU
# ==========================================
import random


def oyunu_baslat():
    """Ana oyun fonksiyonu"""
    
    secenekler = ["taş", "kağıt", "makas"]
    
    oyuncu_skor = 0
    bilgisayar_skor = 0
    
    print("=" * 40)
    print("   TAŞ KAĞIT MAKAS OYUNU")
    print("=" * 40)
    print("Çıkmak için 'q' yazın")
    print()
    
    while True:
        # Oyuncu seçimi
        oyuncu = input("Seçiminiz (taş/kağıt/makas): ").lower().strip()
        
        # Çıkış kontrolü
        if oyuncu == 'q':
            print("\nOyun bitti!")
            print(f"Son Skor - Siz: {oyuncu_skor} | Bilgisayar: {bilgisayar_skor}")
            break
        
        # Geçerlilik kontrolü
        if oyuncu not in secenekler:
            print("Geçersiz seçim! Taş, kağıt veya makas yazın.\n")
            continue
        
        # Bilgisayar seçimi
        bilgisayar = random.choice(secenekler)
        print(f"Bilgisayar: {bilgisayar}")
        
        # Kazananı belirle
        sonuc = kazanani_belirle(oyuncu, bilgisayar)
        
        if sonuc == "oyuncu":
            oyuncu_skor += 1
            print("Kazandınız!")
        elif sonuc == "bilgisayar":
            bilgisayar_skor += 1
            print("Kaybettiniz!")
        else:
            print("Berabere!")
        
        print(f"Skor - Siz: {oyuncu_skor} | Bilgisayar: {bilgisayar_skor}\n")


def kazanani_belirle(oyuncu, bilgisayar):
    """Kazananı belirler"""
    
    if oyuncu == bilgisayar:
        return "berabere"
    
    # Kazanma kuralları
    kazanma_kurallari = {
        "taş": "makas",      # Taş makası kırar
        "makas": "kağıt",    # Makas kağıdı keser
        "kağıt": "taş"       # Kağıt taşı sarar
    }
    
    if kazanma_kurallari[oyuncu] == bilgisayar:
        return "oyuncu"
    else:
        return "bilgisayar"


# Oyunu başlat
if __name__ == "__main__":
    oyunu_baslat()
