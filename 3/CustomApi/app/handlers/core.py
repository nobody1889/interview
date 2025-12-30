from .commands.start import start_command
from .commands.help import help_command
from .feature.echo import echo_feature

async def core(api, updates):
    if not updates:
        return
    
    for update in updates:
        if "message" not in update:
            continue
        
        message = update["message"]
        chat_id = message["chat"]["id"]

        if "text" in message:
            text = message["text"]

            if text.startswith("/"):
                cmd = text.split()[0]

                if cmd == "/start":
                    await start_command(api, chat_id)

                elif cmd == "/help":
                    await help_command(api, chat_id)
                    
                else:
                    await api.send_message(chat_id, "Unknown command")
            else:
                await echo_feature(api, chat_id, text)

        elif "sticker" in message:
            sticker_id = message["sticker"]["file_id"]
            await api.send_sticker(chat_id, sticker_id)

        elif "photo" in message:
            photo_id = message["photo"][-1]["file_id"]
            await api.send_photo(chat_id, photo_id)

        elif "document" in message:
            doc_id = message["document"]["file_id"]
            await api.send_document(chat_id, doc_id)

        else:
            await api.send_message(chat_id, "Unsupported message type")
