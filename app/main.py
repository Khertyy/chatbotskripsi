from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chatbot, reports
from app.config import settings

app = FastAPI(title="DP3A Child Protection Chatbot",
             description="AI-powered child violence reporting system",
             version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

app.include_router(chatbot.router, prefix="/api/v1/chatbot")
app.include_router(reports.router, prefix="/api/v1/chatbot/reports")