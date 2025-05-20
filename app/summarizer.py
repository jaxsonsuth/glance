from transformers.pipelines import pipeline
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

model = os.getenv("MODEL", "pegasus-xsum")
beam_width = int(os.getenv("BEAM_WIDTH", 5))
summary_length = int(os.getenv("SUMMARY_LENGTH", 150))

# Load once when server starts
summarizer = pipeline("summarization", model=model)

def summarize_text(text: str) -> str:
    result = summarizer(text, max_length=summary_length, min_length=30, do_sample=False)
    return result[0]["summary_text"]
