from uuid import uuid4
from datetime import datetime
from app.services.redis_service import redis_service

class SessionManager:
    def __init__(self):
        self.redis = redis_service

    async def create_session(self) -> str:
        session_id = str(uuid4())
        session_data = {
            "session_id": session_id,
            "created_at": datetime.now().isoformat(),
            "history": []
        }
        
        await self.redis.set_session(session_id, session_data)
        return session_id

    async def get_session(self, session_id: str):
        if not session_id:
            return None
            
        session = await self.redis.get_session(session_id)
        if session:
            # Update created_at to extend session
            session["created_at"] = datetime.now().isoformat()
            await self.redis.set_session(session_id, session)
        return session

    async def set_session(self, session_id: str, session_data: dict):
        """Menyimpan data session ke Redis"""
        if not session_id:
            raise ValueError("Session ID tidak boleh kosong")
        
        # Pastikan session_id ada dalam data
        session_data["session_id"] = session_id
        session_data["updated_at"] = datetime.now().isoformat()
        
        await self.redis.set_session(session_id, session_data)

    async def cleanup_sessions(self):
        """Membersihkan session yang sudah expired"""
        # Redis akan otomatis membersihkan sesi yang expired
        pass

session_manager = SessionManager()