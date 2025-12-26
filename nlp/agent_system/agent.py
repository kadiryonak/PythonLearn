import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv()

# API key'i .env dosyasından al veya environment'tan oku
api_key = os.getenv("GOOGLE_API_KEY")

# Model oluştur
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=api_key,
    temperature=0.7,
    max_tokens=1024
)

# content = [{

#     "role": "system", 
#     "content": "Sen Matematik Profesörüsün."
# }, 
# {
#     "role": "user", 
#     "content": "2 + 2 kaçtıt"
# },
# {
#     "role": "assistant", 
#     "content": "4"
# },
# {
#     "role": "user", 
#     "content": "2*235 Kaçtır"
# }
# ]

# content = [
#     SystemMessage(content="Sen Matematik Profesörüsün."),
#     HumanMessage(content="2 + 2 kaçtıt"),
#     AIMessage(content="4"),
#     HumanMessage(content="2*235 Kaçtır")
# ]

# # Basic Chat
# response = model.invoke(content)
# print(response.content)

# Example Streaming

# for chunk in model.stream("Bana Çanakkale savaşını anlat"):
#     print(chunk.content, end = "|", flush=True)


# # Basic Chat
response = model.invoke(content)
# print(response.content)

# ============================================================
# STREAMING / CHUNKING ÖRNEKLERİ
# ============================================================

# -------------------------------------------------------------
# 1. TEMEL STREAMING (Basit Chunk Okuma)
# -------------------------------------------------------------
# stream() metodu, LLM yanıtını parça parça (chunk) döndürür
# Bu sayede uzun cevapları beklemeden anlık görebilirsiniz



for response in model.batch_as_completed(
    [
        HumanMessage(content = "2 + 2 "),
        HumanMessage(content = "savaş"),
        HumanMessage(content = "NLP nedir?"),
        HumanMessage(content = "NLP nedir?"),
        HumanMessage(content = "NLP nedir?")
    ]
)

response = model.batch(
    [
        HumanMessage(content = "NLP nedir?"),
        HumanMessage(content = "NLP nedir?"),
        HumanMessage(content = "NLP nedir?"),
        HumanMessage(content = "NLP nedir?"),
        HumanMessage(content = "NLP nedir?")
    ]
)




# print("\n" + "="*50)
# print("1. TEMEL STREAMING")
# print("="*50)

# for chunk in model.stream("Python nedir? Kısa açıkla."):
#     # Her chunk, AIMessageChunk tipindedir
#     # chunk.content -> Metnin o parçası
#     print(chunk.content, end="", flush=True)

# print("\n")  # Yeni satır

# # -------------------------------------------------------------
# # 2. CHUNK METADATA (Parça Bilgileri)
# # -------------------------------------------------------------
# # Her chunk'ın metadata bilgileri vardır

# print("="*50)
# print("2. CHUNK METADATA")
# print("="*50)

# chunk_count = 0
# total_chars = 0

# for chunk in model.stream("Merhaba, nasılsın?"):
#     chunk_count += 1
#     char_count = len(chunk.content)
#     total_chars += char_count
    
#     print(f"Chunk #{chunk_count}: '{chunk.content}' ({char_count} karakter)")
    
#     # Metadata erişimi (varsa)
#     if hasattr(chunk, 'response_metadata') and chunk.response_metadata:
#         print(f"  Metadata: {chunk.response_metadata}")

# print(f"\nToplam: {chunk_count} chunk, {total_chars} karakter")

# # -------------------------------------------------------------
# # 3. STREAMING İLE LİSTE OLUŞTURMA
# # -------------------------------------------------------------
# # Chunk'ları biriktirip tam yanıtı elde etme

# print("\n" + "="*50)
# print("3. CHUNK'LARI BİRLEŞTİRME")
# print("="*50)

# chunks = []  # Chunk'ları sakla
# full_response = ""  # Tam yanıt

# for chunk in model.stream("1'den 5'e kadar say."):
#     chunks.append(chunk)
#     full_response += chunk.content
#     print(chunk.content, end="", flush=True)

# print(f"\n\nChunk sayısı: {len(chunks)}")
# print(f"Tam yanıt: {full_response}")

# # -------------------------------------------------------------
# # 4. STREAMING İLE ZAMAN ÖLÇÜMÜ
# # -------------------------------------------------------------
# import time

# print("\n" + "="*50)
# print("4. STREAMING PERFORMANS ÖLÇÜMÜ")
# print("="*50)

# start_time = time.time()
# first_chunk_time = None
# chunk_times = []

# for i, chunk in enumerate(model.stream("Python'un avantajları nelerdir?")):
#     current_time = time.time()
    
#     if first_chunk_time is None:
#         first_chunk_time = current_time - start_time
#         print(f"[İlk chunk: {first_chunk_time:.3f}s]")
    
#     chunk_times.append(current_time)
#     print(chunk.content, end="", flush=True)

# end_time = time.time()
# total_time = end_time - start_time

# print(f"\n\nİlk chunk süresi (TTFT): {first_chunk_time:.3f} saniye")
# print(f"Toplam süre: {total_time:.3f} saniye")
# print(f"Ortalama chunk arası: {(total_time - first_chunk_time) / max(len(chunk_times)-1, 1):.3f} saniye")

# # -------------------------------------------------------------
# # 5. STREAMING VS INVOKE KARŞILAŞTIRMASI
# # -------------------------------------------------------------

# print("\n" + "="*50)
# print("5. STREAM vs INVOKE KARŞILAŞTIRMASI")
# print("="*50)

# question = "2+2 kaçtır?"

# # Invoke - Tüm yanıtı bekler
# print("INVOKE (bekleyerek):")
# start = time.time()
# response = model.invoke(question)
# invoke_time = time.time() - start
# print(f"Yanıt: {response.content}")
# print(f"Süre: {invoke_time:.3f}s")

# print()

# # Stream - Anlık gösterir
# print("STREAM (anlık):")
# start = time.time()
# first_chunk = None
# for chunk in model.stream(question):
#     if first_chunk is None:
#         first_chunk = time.time() - start
#     print(chunk.content, end="", flush=True)
# stream_time = time.time() - start
# print(f"\nİlk chunk: {first_chunk:.3f}s, Toplam: {stream_time:.3f}s")

# # -------------------------------------------------------------
# # 6. CONVERSATION GEÇMİŞİ İLE STREAMING
# # -------------------------------------------------------------

# print("\n" + "="*50)
# print("6. CONVERSATION İLE STREAMING")
# print("="*50)

# messages = [
#     SystemMessage(content="Sen yardımcı bir asistansın. Kısa cevap ver."),
#     HumanMessage(content="Başkent neresi?"),
#     AIMessage(content="Hangi ülkenin başkentini soruyorsun?"),
#     HumanMessage(content="Türkiye")
# ]

# print("Soru: Türkiye'nin başkenti neresi?")
# print("Yanıt: ", end="")

# for chunk in model.stream(messages):
#     print(chunk.content, end="", flush=True)

# print("\n")

# # -------------------------------------------------------------
# # 7. HATA YÖNETİMİ İLE STREAMING
# # -------------------------------------------------------------

# print("="*50)
# print("7. HATA YÖNETİMİ")
# print("="*50)

# try:
#     for chunk in model.stream("Merhaba"):
#         print(chunk.content, end="", flush=True)
#     print(" ✓ Başarılı!")
# except Exception as e:
#     print(f"\n❌ Hata: {type(e).__name__}: {e}")

# print("\n" + "="*50)
# print("CHUNKING EĞİTİMİ TAMAMLANDI!")
# print("="*50)

# """
# ÖZET - CHUNKING / STREAMING NEDİR?

# 1. STREAMING: LLM yanıtını beklemeden parça parça alma
# 2. CHUNK: Her bir metin parçası (AIMessageChunk)
# 3. TTFT (Time To First Token): İlk chunk'a kadar geçen süre

# AVANTAJLARI:
# - Kullanıcı deneyimi: Yanıt anında görünmeye başlar
# - Algılanan hız: Toplam süre aynı olsa da daha hızlı hissedilir
# - Memory: Büyük yanıtlar için bellek tasarrufu
# - İptal: İstenirse stream durdurulabilir

# KULLANIM ALANLARI:
# - Chat uygulamaları (ChatGPT tarzı)
# - Gerçek zamanlı çeviriler
# - Kod tamamlama
# - Ses sentezi (TTS) ile kombinasyon

# TEMEL METODLAR:
# - model.invoke(prompt)  -> Tam yanıt döner (AIMessage)
# - model.stream(prompt)  -> Generator döner (AIMessageChunk'lar)
# - model.batch([p1, p2]) -> Toplu istek
# """

