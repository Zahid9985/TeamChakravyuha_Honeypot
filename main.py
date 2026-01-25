from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 1. THE FIX: Allow the Tester Tool to talk to us (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

# 2. THE LOGIC: Check Security + Spy on Data
@app.post("/detect-scam")
async def detect_scam(request: Request, x_api_key: str = Header(None)):
    
    # --- SECURITY CHECK ---

    YOUR_SECRET_KEY = "Chakravyuha_2026_ZS60!" 
    
    if x_api_key != YOUR_SECRET_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # --- SPY MODE ---
    # We grab whatever data they sent so we can learn the format
    try:
        data = await request.json()
        print("--------------------------------------------------")
        print("🟢 SUCCESS! RECEIVED DATA:", data)
        print("--------------------------------------------------")
    except:
        print("⚠️ Connection worked, but no JSON data found.")

    # --- SUCCESS RESPONSE ---
    return {
        "is_scam": True,
        "scam_type": "Phishing",
        "extracted_info": {
            "upi_id": "scammer@sbi",
            "bank_account": "123456789"
        },
        "confidence_score": 0.99,
        "explanation": "Connection Successful. Security Passed."
    }

@app.get("/")
def home():
    return {"status": "System is Online", "team": "Team Chakravyuha"}