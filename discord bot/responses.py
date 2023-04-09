import chatbot

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return 'Hey there!'
    
    if p_message == 'tristan':
        return 'Tristan is a marie'
    
    else:
        return chatbot.respond(p_message)