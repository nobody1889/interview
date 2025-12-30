async def echo_feature(api, chat_id, text):
    await api.send_message(chat_id, f"You said:\n[{text}]")
