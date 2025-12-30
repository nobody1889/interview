async def start_command(api, chat_id):
    await api.send_message(
        chat_id = chat_id, 
        message = "Bot started 🚀"
        )