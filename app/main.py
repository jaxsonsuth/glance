from fastapi import FastAPI
from pydantic import BaseModel
from .summarizer import summarize_text

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/summarize")
async def summarize(input: TextInput):
    if len(input.text) < 50:  # You can adjust the threshold as needed
        # Return a message that repeats the text or just returns it as-is
        return {
            "summary": f"Text too short to summarize effectively. Here is the content: {input.text}"
        }
    summary = summarize_text(input.text)
    return {"summary": summary}
