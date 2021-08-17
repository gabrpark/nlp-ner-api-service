# Fast API
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

# NLP NER
import spacy

# An example text. NEED TO BE REMOVED LATER ON.
sentence = "European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices."

app = FastAPI(
    title="NER Model API",
    description="An HTTP API that run NER on a given text",
    version="0.1",
)

class NER(BaseModel):
    name: str
    type: str

# Load the NER model
nlp = spacy.load('en_core_web_sm')

async def analyze_text(input_text=sentence):
    doc = nlp(input_text)
    result = []
    for ent in doc.ents:
        result.append(NER(name=ent.text, type=ent.label_))
    return result

@app.get("/")
async def read_root():
    return await analyze_text()
