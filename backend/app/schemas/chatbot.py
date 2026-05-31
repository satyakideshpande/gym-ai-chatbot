from pydantic import BaseModel, Field
from typing import List

class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1)

class ChatResponse(BaseModel):
    answer: str

class GeminiModel(BaseModel):
    name: str
    display_name: str

class ModelsResponse(BaseModel):
    models: List[GeminiModel]
