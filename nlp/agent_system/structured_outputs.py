import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from pydantic import BaseModel, Field 

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


class WeitherResponse(BaseModel):
    temperature: float = Field(..., description = "Sıcaklık celsius cinsinden")
    condition: str = Field(..., description = "Hava Durumu")
    humidity: int = Field(..., description = "Nem Oranı cinsinden")
    
model.with_structured_output(WeitherResponse)
response = model.invoke("Sivas için yazları hava durumu nedir?")
print(response.content)

