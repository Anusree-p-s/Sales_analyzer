# test_key.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

print("--- Start of Key Test ---")

# 1. Test loading the environment variables
load_dotenv() 
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("❌ ERROR 1: GEMINI_API_KEY is not being loaded from .env.")
    print("   Please check the .env file exists and is in the current directory.")
else:
    print(f"✅ Status: API Key loaded (Length: {len(GEMINI_API_KEY)} characters)")
    
    try:
        # 2. Test configuration
        genai.configure(api_key=GEMINI_API_KEY)
        print("✅ Status: genai.configure() successful.")
        
        # 3. Test API connection and key validity
        print("🔍 Testing by listing models...")
        # Note: This list operation is the simplest API call to validate the key
        models = list(genai.list_models()) 
        
        if models:
            print(f"✅ SUCCESS: API Key is active! Found {len(models)} models.")
            print(f"   The first model is: {models[0].name}")
        else:
            print("❌ FAILURE 3: Key is likely invalid or restricted. No models were returned.")

    except Exception as e:
        print(f"❌ CRITICAL ERROR 2: The key failed to authenticate or connect.")
        print(f"   Details: {e}")

print("--- End of Key Test ---")