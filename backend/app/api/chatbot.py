from fastapi import APIRouter
from pathlib import Path
from app.schemas.chatbot import ChatRequest, ChatResponse, GeminiModel, ModelsResponse
from app.services.llm_service import LLMService
from app.core.config import settings
from google import genai

router = APIRouter()
llm_service = LLMService()

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = llm_service.get_response(request.question)
    return ChatResponse(answer=answer)

@router.post("/gemini", response_model=ChatResponse)
def chat_gemini(request: ChatRequest):
    gym_data = read_gym_data()
    
    # Create a system prompt (guardrail) for the gym assistant
    system_prompt = f"""You are a gym and fitness AI assistant with access to this gym data:

    {gym_data}

    Rules:
    1. Answer only questions about fitness, workouts, gym services, and health
    2. Provide information only from the gym data provided
    3. Be friendly and helpful
    4. If asked about something outside of gym/fitness, politely decline and redirect to gym topics"""
    
    response = llm_service.get_response(request.question, system_prompt=system_prompt)
    return response

def read_gym_data():
    """Reads the gym_data.txt file from the knowledge_base folder and prints the data."""
    knowledge_base_path = Path(__file__).parent.parent.parent / "knowledge_base" / "atenx_kothrud.txt"
    try:
        with open(knowledge_base_path, 'r') as file:
            gym_data = file.read()
            #print(gym_data)
            return gym_data
    except FileNotFoundError:
        print(f"Error: File not found at {knowledge_base_path}")
        return None