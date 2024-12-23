import os
import requests
from fastapi import FastAPI, HTTPException, Body
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Fetch URLs from environment variables
APP2_URL = os.getenv("APP2_URL")
APP3_URL = os.getenv("APP3_URL")

@app.post("/generatetext")
async def generate_text(input_text: str = Body(...)):
    # Call App2 to moderate content
    response = requests.post(f"{APP2_URL}/moderatecontent", json={"input_text": input_text})
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Moderation service failed")
    moderation_result = response.json()
    if moderation_result["safe_flag"] == "No":
        return {"message": f"Content not safe: {moderation_result['reason']}"}
    
    # Call App3 to generate LLM response
    response = requests.post(f"{APP3_URL}/generatellmresponse", json={"input_text": input_text})
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="LLM generation service failed")
    llm_result = response.json()
    return {"llm_response": llm_result}
