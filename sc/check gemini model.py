import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv(r'your/path/.env') #need to ensure you have '.env'
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# List available models
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
