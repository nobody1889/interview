import httpx
from os import environ

class TelegtamApi():
    def __init__(self):
        self.token = environ.get('BOT_TOKEN')

        if not self.token:
            raise RuntimeError("BOT_TOKEN not set")
        
        self.base_url = f"https://api.telegram.org/bot{self.token}"

        self.client = httpx.AsyncClient(timeout=10)

    async def send_message(self, chat_id, message):
        method = "/sendMessage"
        url = self.base_url + method

        params = {
            "chat_id": chat_id,
            "text": message
        }

        response = await self.client.post(
            url,
            params=params
            )
        return response
    
    async def get_updates(self, offset: int | None = None):
        method = "/getUpdates"
        url = self.base_url + method

        payload = {
            "offset": offset
        }
        
        response = await self.client.get(
            url,
            params=payload
            )
        
        return response
