import os
import requests
from fastapi import FastAPI, HTTPException, Body
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

# Fetch App1 URL from environment variables
APP1_URL = os.getenv("APP1_URL")


@app.post("/summarisecontent")
async def summarise_content(input_text: str = Body(...)):
    # Call App1 to generate text
    response = requests.post(f"{APP1_URL}/generatetext", data=input_text,headers={"Content-Type": "text/plain"})
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Text generation service failed")
    app1_result = response.json()
    return {"generated_text": app1_result}
