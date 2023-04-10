import discord
import responses
import json

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = json.loads(open('../private-information/discord-bots.json').read())['bots'][0]['token']
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        #get message information
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        #perform some validation checks
        if message.author == client.user:
            return
        if channel != 'botnis-everdeen':
            return
        if user_message == '!kill':
            await client.close()
        print(f'{username} said: {user_message} in channel ({channel})')

        #respond to message
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)