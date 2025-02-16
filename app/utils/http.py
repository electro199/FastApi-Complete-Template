from typing import Optional

from aiohttp import ClientSession


class HttpClient:
    session: Optional[ClientSession] = None

    @classmethod
    async def start(cls) -> ClientSession:
        """
        Start Client
        """
        if not cls.session:
            cls.session = ClientSession()
        return cls.session

    async def stop(self):
        """
        Cloes Client gracefully
        """
        assert self.session is not None, "session is closed"
        await self.session.close()
        self.session = None

    def __call__(self) -> ClientSession:
        assert self.session is not None
        return self.session