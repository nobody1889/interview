from commands.start import start_command
from commands.help import help_command
from feature.echo import echo_feature

async def core(api, updates):
    if not updates:
        return

    for update in updates:
        if "message" not in update:
            continue
        
        message = update["message"]
        chat_id = message["chat"]["id"]
        text = message.get("text", "")

        if text.startswith("/"):
            command = text.split()[0]  

            if command == "/start":
                await start_command(api, chat_id)

            elif command == "/help":
                await help_command(api, chat_id)

            else:
                await api.send_message(chat_id, f"Unknown command: {command}")
        
        elif text:
            await echo_feature(api, chat_id, text)
