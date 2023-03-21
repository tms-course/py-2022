from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Message


class MessageRepo:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, text: str) -> Message:
        msg = Message(text=text)
        self._session.add(msg)
        await self._session.commit()

        return msg

    async def list(self) -> list[Message]:
        query = select(Message)
        result = await self._session.execute(query)
        
        return result.scalars().all()