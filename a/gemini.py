import requests

API_KEY = "AIzaSyBsW9s1Uy-HOTA8yVIg97IaHIhZ2iXrnlU"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

def get_gemini_reply(prompt: str) -> str:
    try:
        response = requests.post(GEMINI_URL, json={
            "contents": [{"parts": [{"text": prompt}]}]
        })
        if response.status_code == 200:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print("Gemini error:", e)
    return "Sorry, I couldn't respond."
