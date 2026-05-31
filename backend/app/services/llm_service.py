from google import genai
from app.core.config import settings
from app.schemas.chatbot import ChatResponse


class LLMService:
    """
    Handles all LLM-related logic.
    """

    def get_response(self, question: str, system_prompt: str = None) -> str:
        """
        Get response from Gemini with optional system prompt (guardrail).
        
        Args:
            question: User's question/prompt
            system_prompt: Optional system instruction to constrain model behavior
        
        Returns:
            ChatResponse with the model's answer
        """
        client = genai.Client(api_key=settings.google_api_key)
        
        # If system prompt provided, prepend it to the question
        if system_prompt:
            full_prompt = f"{system_prompt}\n\nUser question: {question}"
        else:
            full_prompt = question
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt
        )
        print("Response:", response.text)
        return ChatResponse(answer=response.text)