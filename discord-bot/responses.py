import chatbot
import random

def handle_response(message) -> str:
    p_message = message.lower()
    
    if p_message == '!tristan':
        return 'Tristan is a marie'
    
    #TODO: Pick a random bully maguire line from the intents file
    if p_message == '!bullymaguire':
        pass

    if p_message == '!roll':
        return str(random.randint(1,6))
    
    #TODO: Provide a comprehensive description of bot
    if p_message == '!info':
        return "current version: v0.0.2"
    
    #TODO: Provide a comprehensive list of commands for bot
    if p_message == "!help":
        pass
    
    else:
        return chatbot.respond(p_message)