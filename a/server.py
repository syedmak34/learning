from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from gemini import get_gemini_reply

DATABASE_URL = "postgresql://chatuser:chatpass@localhost:5433/chatdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    username: str
    text: str

with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            username TEXT NOT NULL,
            text TEXT NOT NULL,
            timestamp TIMESTAMPTZ DEFAULT NOW()
        );
    """))

@app.post("/send")
async def send_message(msg: Message):
    with SessionLocal() as session:
        session.execute(text("""
            INSERT INTO messages (username, text, timestamp)
            VALUES (:username, :text, :timestamp)
        """), {
            "username": msg.username,
            "text": msg.text,
            "timestamp": datetime.utcnow()
        })
        session.commit()

    # Gemini auto-reply (optional)
    if msg.username.lower() != "gemini":
        reply = get_gemini_reply(msg.text)
        if reply:
            with SessionLocal() as session:
                session.execute(text("""
                    INSERT INTO messages (username, text, timestamp)
                    VALUES ('Gemini', :text, :timestamp)
                """), {
                    "text": reply,
                    "timestamp": datetime.utcnow()
                })
                session.commit()

    return {"status": "Message sent"}

@app.get("/messages")
async def get_messages():
    with SessionLocal() as session:
        result = session.execute(text("""
            SELECT username, text, timestamp FROM messages
            ORDER BY timestamp DESC LIMIT 50
        """)).fetchall()
    return [
        {"username": r[0], "text": r[1], "timestamp": r[2].isoformat()}
        for r in reversed(result)
    ]
