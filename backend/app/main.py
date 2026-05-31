from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chatbot import router as chatbot_router
from app.api.health import router as health_router

app = FastAPI(
    title="GYM AI Chatbot",
    description="Stateless AI-powered gym assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your frontend URL like http://localhost:3000
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(chatbot_router, prefix="/chatbot", tags=["Chatbot"])
app.include_router(health_router, prefix="/health", tags=["Health"])
