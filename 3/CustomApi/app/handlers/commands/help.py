async def help_command(api, chat_id):
    await api.send_message(
        chat_id = chat_id, 
        text = "just send a message to me and i will echo it back to you 🤖"
        )