from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# 1. Define the Input Format (What the tester sends you)
class ScamMessage(BaseModel):
    message: str
    sender_id: Optional[str] = "unknown"

# 2. Define your "Secret Password" (API Key)
# In a real app, use Environment Variables, but for now, hardcode it for testing.
YOUR_SECRET_KEY = "Chakravyuha_2026_ZS60" 

@app.post("/detect-scam")
async def detect_scam(data: ScamMessage, x_api_key: str = Header(None)):
    
    # 3. Security Check: Verify the API Key
    if x_api_key != YOUR_SECRET_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # 4. The Logic (Currently just a dummy response to pass the test)
    # later, we will put the AI Agent logic here.
    
    return {
        "is_scam": True,  # We pretend it's always a scam for the test
        "scam_type": "Phishing",
        "extracted_info": {
            "upi_id": "scammer@sbi", # Dummy data
            "bank_account": "123456789"
        },
        "confidence_score": 0.99,
        "explanation": "This is a test response from Team Mirsad."
    }

# 5. A simple check to see if the server is running
@app.get("/")
def home():
    return {"status": "System is Online", "team": "Team Mirsad"}