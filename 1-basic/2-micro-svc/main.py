from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/moderatecontent")
async def moderate_content(input_data: dict = Body(...)):
    input_text = input_data.get("input_text", "")
    if len(input_text) % 2 == 0:
        return {"safe_flag": "Yes", "reason": "This is safe"}
    else:
        return {"safe_flag": "No", "reason": "This is not safe"}
