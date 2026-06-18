from fastapi import APIRouter
from pathlib import Path
from app.schemas.chatbot import ChatRequest, ChatResponse, GeminiModel, ModelsResponse
from app.services.llm_service import LLMService
from app.services.rag.rag_manager import get_rag_manager, initialize_rag
from app.services.conversation_memory import conversation_memory
from app.core.config import settings
from google import genai

router = APIRouter()
llm_service = LLMService()

# Global flag to track RAG initialization
_rag_initialized = False


def ensure_rag_initialized():
    """Ensure RAG pipeline is initialized on first request."""
    global _rag_initialized
    if not _rag_initialized:
        # Get the backend directory for vector_db storage
        backend_dir = Path(__file__).parent.parent.parent
        db_path = str(backend_dir / "vector_db")
        
        # Initialize RAG pipeline
        initialize_rag(db_path=db_path, verbose=True)
        _rag_initialized = True


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = llm_service.get_response(request.question)
    return ChatResponse(answer=answer)

@router.post("/clear")
def clear_chat():
    """
    Clear conversation memory endpoint.
    
    When the user clicks the "Clear Chat" button on the frontend,
    this endpoint resets the conversation memory to start fresh.
    """
    conversation_memory.clear_history()
    return {"status": "Chat history cleared"}


@router.post("/gemini", response_model=ChatResponse)
def chat_gemini(request: ChatRequest):
    """
    Chat endpoint using RAG (Retrieval-Augmented Generation) with conversation memory.
    
    Flow:
    1. Retrieve conversation history from memory (for context)
    2. Retrieve relevant chunks from ChromaDB based on user's question
    3. Send context + history to LLM
    4. Store the exchange in conversation memory
    5. Return LLM's response
    """
    # Ensure RAG is initialized
    ensure_rag_initialized()
    
    # Get RAG manager and retrieve relevant context
    backend_dir = Path(__file__).parent.parent.parent
    db_path = str(backend_dir / "vector_db")
    rag_manager = get_rag_manager(db_path=db_path)
    
    # Retrieve top-3 most relevant chunks based on user's question
    relevant_context = rag_manager.retrieve_context(
        query=request.question,
        top_k=3,
        verbose=False
    )
    
    # Get conversation history for context
    conversation_history = conversation_memory.format_history_for_prompt()
    
    # Build the system prompt with gym data context and conversation history
    system_prompt = f"""You are a AI assistant for a gym called Planet Fitness with access to this gym data:

    {relevant_context}

    Rules:
    1. Answer only questions related to the gym data provided above.
    2. Do not answer questions about topics outside of the gym data.
    3. You should be friendly, polite and helpful when answering questions about the gym data.
    4. The conversation should be human like and should not feel robotic.
    4. If asked about something outside of gym/fitness or not in the provided data, politely decline and redirect to questions related to Planet Fitness.
    5. If the provided data doesn't contain information to answer the question, say you don't have that information.
    6. Do not greet the user with "Hello", "Hi", or "Hello there" in every response. Only greet them if it's the first message in the conversation.
    7. Be ellaborative and provide detailed answers when possible, but make sure to just answer the question and not provide unnecessary information."""
    
    # Add conversation history if it exists
    if conversation_history:
        system_prompt += f"\n\nPrevious conversation context:\n{conversation_history}"
    
    response = llm_service.get_response(request.question, system_prompt=system_prompt)
    
    # Add the exchange to conversation memory for context in future queries
    conversation_memory.add_exchange(
        user_message=request.question,
        assistant_response=response.answer
    )
    
    return response