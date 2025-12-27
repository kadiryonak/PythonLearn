import os
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
import random

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# Model
model = ChatGroq(
    api_key=api_key,
    model="llama-3.3-70b-versatile",
)



@tool
def get_weather(city: str) -> str:
    weather_data = {
        "istanbul": "İstanbul: Parçalı bulutlu, 15°C",
        "ankara": "Ankara: Güneşli, 12°C", 
        "izmir": "İzmir: Açık, 18°C",
        "kayseri": "Kayseri: Karlı, -2°C",
    }
    city_lower = city.lower()
    return weather_data.get(city_lower, f"{city}: Hava bilgisi bulunamadı")


@tool
def calculate(expression: str) -> str:
    try:
        result = eval(expression)
        return f"Sonuç: {result}"
    except Exception as e:
        return f"Hesaplama hatası: {str(e)}"


@tool
def roll_dice(sides: int = 6) -> str:
    result = random.randint(1, sides)
    return f"🎲 {sides} yüzlü zar atıldı: {result}"


tools = [get_weather, calculate, roll_dice]
model_with_tools = model.bind_tools(tools)


# Test 1: Hava durumu
print("\n📍 Test 1: Hava Durumu")
response1 = model_with_tools.invoke([
    SystemMessage(content="Sen yardımcı bir asistansın. Tool'ları kullanarak soruları yanıtla."),
    HumanMessage(content="Kayseri'de hava nasıl?")
])
print(f"Model yanıtı: {response1.content}")
if response1.tool_calls:
    print(f"Tool çağrısı: {response1.tool_calls}")
    # Tool'u manuel çalıştır
    for tool_call in response1.tool_calls:
        if tool_call['name'] == 'get_weather':
            result = get_weather.invoke(tool_call['args'])
            print(f"Tool sonucu: {result}")


# Test 2: Hesaplama
print("\n🔢 Test 2: Hesaplama")
response2 = model_with_tools.invoke([
    SystemMessage(content="Sen yardımcı bir asistansın. Tool'ları kullanarak soruları yanıtla."),
    HumanMessage(content="125 * 48 kaç eder?")
])
print(f"Model yanıtı: {response2.content}")
if response2.tool_calls:
    print(f"Tool çağrısı: {response2.tool_calls}")
    for tool_call in response2.tool_calls:
        if tool_call['name'] == 'calculate':
            result = calculate.invoke(tool_call['args'])
            print(f"Tool sonucu: {result}")


# Test 3: Zar atma
print("\n🎲 Test 3: Zar Atma")
response3 = model_with_tools.invoke([
    SystemMessage(content="Sen yardımcı bir asistansın. Tool'ları kullanarak soruları yanıtla."),
    HumanMessage(content="20 yüzlü bir zar at")
])
print(f"Model yanıtı: {response3.content}")
if response3.tool_calls:
    print(f"Tool çağrısı: {response3.tool_calls}")
    for tool_call in response3.tool_calls:
        if tool_call['name'] == 'roll_dice':
            result = roll_dice.invoke(tool_call['args'])
            print(f"Tool sonucu: {result}")

