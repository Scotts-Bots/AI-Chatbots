import chatbot

def handle_response(message) -> str:
    p_message = message.lower()
    return chatbot.respond(p_message)