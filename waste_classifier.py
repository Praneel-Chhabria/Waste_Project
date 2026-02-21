import os
from google import  genai
from dotenv import load_dotenv

load_dotenv()
api=os.getenv("GOOGLE_API_KEY")
client=genai.Client(api_key=api)
SYSTEM_INSTRUCTIONS = """
You are a waste management expert. Classify the item in the image into:
1. Wet Waste (Organic/Biodegradable)
2. Dry Waste (Recyclables like clean plastic, paper, metal)
3. Domestic Hazardous (Batteries, meds, chemicals, sanitary waste)

Respond strictly in this JSON format:
{
  "category": "Wet/Dry/Hazardous",
  "item": "Name of the item",
  "confidence": 0.95,
  "instruction": "Short tip for disposal"
}
"""
model=genai.GenerativeModel('gemini-2.0-flash')

def classify_waste_image(img): # img for taking pil image 
    print()
    
