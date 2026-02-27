Smart Waste Classification System
---------------------------------

About
-----
This is an image classification system we built to figure out the right way to dispose of waste. You upload an image of some trash, and the backend uses the Gemini API to classify it into:
1. Wet Waste (organic/biodegradable)
2. Dry Waste (recyclables like plastic, paper, metal)
3. Domestic Hazardous (batteries, medical waste, chemicals)

It also gives you a short instruction on how to actually dispose of it safely.

**Live Demo:** [ecosortprime.streamlit.app](https://ecosortprime.streamlit.app/)

Working Images
--------------
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f562ee7c-9e74-45fa-aead-d382a6206534" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cf3041f9-eca6-4ae2-942c-ea535a3c57d6" />

Tech Stack
----------
* Python
* Streamlit (frontend and deployment)
* Google Gemini API (gemini-2.5-flash)
* Pillow (image processing)
* python-dotenv

How to run this locally
-----------------------
1. Clone this repository to your machine.
2. Install the required packages:
   
   pip install -r requirements.txt
   
3. Make a `.env` file in the main folder and add your Google API key:
   
   GOOGLE_API_KEY="your_api_key_here"
   
4. Start the app:
   
   streamlit run app.py
   

Created by
----------
Praneel Chhabria, Amogh Kulkarni, Priyanshu Hazra, Vivaan Vora, Insha Hasan Ansari, Aayush Khandelwal
