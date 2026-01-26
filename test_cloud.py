import requests

# 1. Your Cloud URL (Make sure it ends with /detect-scam)
url = "https://teamchakravyuha-honeypot.onrender.com/detect-scam"

# 2. The Data we want to send (Simulating the Tester Tool)
payload = {
    "message": "Hello, I am a scammer. Give me money.",
    "sender": "BadGuy123"
}

# 3. The Headers (Your Password)
headers = {
    "x-api-key": "Chakravyuha_2026_ZS60!"
}

print(f"🚀 Sending message to {url}...")

try:
    response = requests.post(url, json=payload, headers=headers)
    
    # 4. Print the Result
    print(f"✅ Status Code: {response.status_code}")
    print("📜 Response from Server:")
    print(response.json())

except Exception as e:
    print(f"❌ Error: {e}")