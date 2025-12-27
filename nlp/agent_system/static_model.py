import os
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.language_models.fake_chat_models import FakeListChatModel
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")


basic_model = ChatGroq(
    api_key=api_key,
    model="openai/gpt-oss-20b",
)

advanced_model = ChatGroq(
    api_key=api_key,
    model="openai/gpt-oss-120b",
)


# messages =[ 
#     SystemMessage(content="Sen bana yardımcı olacak iyi bir Türk arkadaşsin."),
#     HumanMessage(content="Naber"),
# ]
# ai_msg = basic_model.invoke(messages)
# print(ai_msg.content)


# FakeChatModel sanki llm var gibi cevap verir. Unit Test için birebirdir.

# Sırayla verilecek cevapları tanımla
# fake_llm = FakeListChatModel(responses=["Merhaba!", "Nasılsın?", "İyiyim teşekkürler"])
# print(fake_llm.invoke("test1",content="Merhaba").content)  # "Merhaba!"
# print(fake_llm.invoke("test2",content="Nasılsın").content)  # "Nasılsın?"
# print(fake_llm.invoke("test3",content="İyiyim").content)  # "İyiyim teşekkürler"


def dynamic_model_selector(messages: list):
    """
    Mesaj sayısına göre model seçer.
    < 5 mesaj: basic_model (hızlı, ucuz)
    >= 5 mesaj: advanced_model (güçlü)
    """
    message_count = len(messages)
    print(f"Mesaj sayısı: {message_count}")
    
    if message_count < 5:
        print("Basic model kullanılıyor...")
        return basic_model.invoke(messages)
    else:
        print("Advanced model kullanılıyor...")
        return advanced_model.invoke(messages)


# Test
messages = [ 
    SystemMessage(content="Sen bana yardımcı olacak iyi bir Türk arkadaşsin."),
    HumanMessage(content="Naber"),
    HumanMessage(content="Naber"),
    HumanMessage(content="Naber"),
    HumanMessage(content="Naber"),
    HumanMessage(content="Naber"),
]

response = dynamic_model_selector(messages)
print(response.content)