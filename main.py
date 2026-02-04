from fastapi import FastAPI, Request, Header
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# 1. CORS (Crucial for the tool to connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 2. UPTIME MONITOR FIX ---
# This stops UptimeRobot from getting "405 Method Not Allowed" errors
@app.head("/")
@app.head("/detect-scam")
def ping():
    return {"status": "alive"}

@app.post("/detect-scam")
async def detect_scam(request: Request, x_api_key: str = Header(None)):

    # 1. API key check
    if x_api_key != "Chakravyuha_2026_ZS60":
        return {
            "status": "success",
            "reply": "Unable to verify message at this time."
        }

    # 2. Safe JSON parsing
    try:
        data = await request.json()
        text = data.get("message", {}).get("text", "")
        text = text.lower()
    except:
        text = ""

    # 3. Scam detection
    reply = "This message appears safe."

    if "bank" in text or "account" in text or "otp" in text:
        reply = "Why is my account being suspended?"
    elif "win" in text or "lottery" in text or "prize" in text:
        reply = "Is this lottery message genuine?"
    elif "blocked" in text or "urgent" in text or "verify" in text:
        reply = "Is this message trying to scare me?"

    # 4. EXACT expected response
    return {
        "status": "success",
        "reply": reply
    }


@app.get("/")
def home():
    return {"status": "Team Chakravyuha Agent Online"}