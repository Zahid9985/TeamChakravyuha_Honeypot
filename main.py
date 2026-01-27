from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# 1. CORS (Keeps the connection open for the tool)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/detect-scam")
async def detect_scam(request: Request, x_api_key: str = Header(None)):
    
    # --- LOGGING START (Check Render Logs for this!) ---
    print(f"--- INCOMING REQUEST ---")
    print(f"API Key Received: {x_api_key}")

    # --- SECURITY CHECK ---
    YOUR_SECRET_KEY = "Chakravyuha_2026_ZS60"
    if x_api_key != YOUR_SECRET_KEY:
        print("ERROR: Invalid API Key")
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # --- UNIVERSAL INPUT READER ---
    try:
        data = await request.json()
        print(f"Data Received: {json.dumps(data)}") # Log the input
    except:
        print("ERROR: Could not parse JSON")
        raise HTTPException(status_code=400, detail="Invalid JSON format")

    input_text = str(data).lower()
    
    # --- LOGIC ---
    # We define the inner data first
    intelligence_data = {}
    is_scam_flag = False
    scam_type_str = "None"

    if "bank" in input_text or "account" in input_text or "otp" in input_text:
        is_scam_flag = True
        scam_type_str = "Banking Fraud"
        intelligence_data = {
            "risk_level": "Critical",
            "action": "Block Sender",
            "intent": "Financial Theft"
        }
    elif "win" in input_text or "lottery" in input_text:
        is_scam_flag = True
        scam_type_str = "Lottery Scam"
        intelligence_data = {
            "risk_level": "High",
            "action": "Warn User",
            "intent": "Phishing"
        }
    else:
        intelligence_data = {"risk_level": "Safe"}

    # --- THE SHOTGUN RESPONSE ---
    # We send the data in ALL possible formats to satisfy the picky tool
    response_payload = {
        "status": "success",
        
        # Format 1: Standard
        "is_scam": is_scam_flag,
        "scam_type": scam_type_str,
        
        # Format 2: The User's Logic
        "extracted_info": intelligence_data,
        
        # Format 3: The Problem Statement Logic ("extracted intelligence")
        "intelligence": intelligence_data,
        
        # Format 4: Generic
        "data": intelligence_data,
        "analysis": scam_type_str
    }

    print(f"--- SENDING RESPONSE ---")
    print(json.dumps(response_payload)) # Log what we send
    
    return response_payload

@app.get("/")
def home():
    return {"status": "Team Chakravyuha Agent Online", "ready": True}