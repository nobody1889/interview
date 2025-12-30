import httpx
from os import environ
from dotenv import load_dotenv

load_dotenv()

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
    
    async def send_sticker(self, chat_id, sticker_file_id):
        url = self.base_url + "/sendSticker"
        return await self.client.post(url, params={
            "chat_id": chat_id,
            "sticker": sticker_file_id
        })

    async def send_document(self, chat_id, file_id):
        url = self.base_url + "/sendDocument"
        return await self.client.post(url, params={
            "chat_id": chat_id,
            "document": file_id
        })

    async def send_photo(self, chat_id, file_id):
        url = self.base_url + "/sendPhoto"
        return await self.client.post(url, params={
            "chat_id": chat_id,
            "photo": file_id
        })
    
    async def get_updates(self, offset: int | None = None) -> tuple:
        print("offset is: ", offset)
        method = "/getUpdates"
        url = self.base_url + method

        payload = {
            "offset": offset
        }
        
        response = await self.client.get(
            url,
            params=payload
            )
        data = response.json()

        if data["ok"]:
            updates = data.get("result", [])
            if updates:
                return updates, updates[-1]["update_id"] + 1
            else:
                return [], offset
        else:
            print("Error fetching updates:", data)
            return [], offset
