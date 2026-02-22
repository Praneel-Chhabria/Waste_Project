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

def classify_waste_image(img):
    try:
       
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[SYSTEM_INSTRUCTIONS, img],
            config={
                'response_mime_type': 'application/json', # Forces JSON output
            }
        )
        return response.text
    except Exception as e:
        return {"error": f"Failed to process image: {str(e)}"}
    
