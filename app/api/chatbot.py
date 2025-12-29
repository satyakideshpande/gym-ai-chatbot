from fastapi import APIRouter
from app.schemas.chatbot import ChatRequest, ChatResponse
from app.services.llm_service import LLMService

router = APIRouter()
llm_service = LLMService()

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = llm_service.get_response(request.question)
    return ChatResponse(answer=answer)
