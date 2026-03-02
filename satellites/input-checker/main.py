from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Vigilant AI Input Checker", description="Basic security gate for Vigilant AI—validates inputs before scanning for African fraud patterns.")

class InputText(BaseModel):
    text: str  # The SMS or message to check

@app.post("/check")
def check_input(input_data: InputText):
    text = input_data.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Input cannot be empty—fraudsters often send blanks to probe systems.")
    if len(text) > 1000:
        raise HTTPException(status_code=400, detail="Input too long—could be a denial-of-service attempt. Keep under 1000 chars for safety.")
    if any(bad in text.lower() for bad in ["virus", "hack", "<script>"]):  # Basic bad pattern check (expand with your ML rules later)
        raise HTTPException(status_code=400, detail="Suspicious content detected—possible injection or malware reference.")
    
    # If valid, "clean" it and return (this could forward to backend/ML in full integration)
    return {
        "status": "valid",
        "cleaned_text": text,
        "note": "Passed basic checks. Safe for Vigilant AI scan (e.g., M-Pesa fraud detection)."
    }

@app.get("/")
def root():
    return {"message": "Vigilant AI Input Checker is online. POST to /check with {'text': 'your message'}."}