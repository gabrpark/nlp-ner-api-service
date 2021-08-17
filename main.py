# Fast API
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

# NLP NER
import spacy

# An example text. NEED TO BE REMOVED LATER ON.

class NER(BaseModel):
    name: str
    type: str

app = FastAPI()

# Load the NER model
nlp = spacy.load('en_core_web_sm')

# Run NER on the input text and store it in a list
async def analyze_text(input_text: str):
    doc = nlp(input_text)
    result = []
    for ent in doc.ents:
        result.append(NER(name=ent.text, type=ent.label_))
    return result

@app.post("/")
async def read_root(input_text: str):
    return await analyze_text(input_text)