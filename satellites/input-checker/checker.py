from fastapi import FastAPI
import re

app = FastAPI()

@app.post("/check")
def check_input(body: dict):
    text = body.get("text", "")
    # Allowlist: Only letters, numbers, and spaces. Block symbols like < > ;
    if not re.match(r'^[a-zA-Z0-9\s]+$', text):
        return {"error": "Invalid input! Potential hacking attempt."}
    return {"valid": True, "clean_text": text}
