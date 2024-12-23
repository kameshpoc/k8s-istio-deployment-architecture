import random
from fastapi import FastAPI, Body

app = FastAPI()

responses = [
    "Hi I am from Gemini 1.5 pro",
    "Hi I am from Llama 3.2",
    "Hi I am from Mars",
    "Hi I am from India",
    "Hi I am from UK",
]

@app.post("/generatellmresponse")
async def generate_llm_response(input_data: dict = Body(...)):
    input_text = input_data.get("input_text", "")
    random_response = random.choice(responses)
    return {"response": random_response}
