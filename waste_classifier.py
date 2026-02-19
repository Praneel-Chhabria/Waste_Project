import os
from google import  genai
from dotenv import load_dotenv

load_dotenv()
api=os.getenv("GOOGLE_API_KEY")
client=genai.Client(api_key=api)

model=genai.GenerativeModel('gemini-2.0-flash')

def classify_waste_image(img): # img for taking pil image 
    print()