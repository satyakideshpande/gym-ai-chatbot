from fastapi import FastAPI
from app.api.chatbot import router as chatbot_router
from app.api.health import router as health_router

app = FastAPI(
    title="GYM AI Chatbot",
    description="Stateless AI-powered gym assistant",
    version="1.0.0"
)

app.include_router(chatbot_router, prefix="/chatbot", tags=["Chatbot"])
app.include_router(health_router, prefix="/health", tags=["Health"])
