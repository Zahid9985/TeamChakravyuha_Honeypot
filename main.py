from fastapi import FastAPI, Header, HTTPException, Request
from typing import Dict, Any

app = FastAPI()

# "Spy Mode" Code
@app.post("/detect-scam")
async def detect_scam(request: Request, x_api_key: str = Header(None)):
    
    # 1. Grab the raw data sent by the Tester
    data = await request.json()
    
    # 2. PRINT IT to the Render Logs (This is how we spy!)
    print("--------------------------------------------------")
    print("🔎 SPY MODE - RECEIVED DATA:", data)
    print("--------------------------------------------------")

    # 3. Security Check (Keep this)
    # Replace with your ACTUAL password!
    YOUR_SECRET_KEY = "Chakravyuha_2026_ZS60!" 
    
    if x_api_key != YOUR_SECRET_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # 4. Return the dummy response (so the tester doesn't crash)
    return {
        "is_scam": True,
        "scam_type": "Phishing",
        "extracted_info": {
            "upi_id": "scammer@sbi",
            "bank_account": "123456789"
        },
        "confidence_score": 0.99,
        "explanation": "Debug mode active."
    }

@app.get("/")
def home():
    return {"status": "System is Online"}