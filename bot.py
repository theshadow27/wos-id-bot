import os
import discord
from bot_logic import handle_message

from dotenv import load_dotenv
load_dotenv()

# Load configuration from environment variables
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))
BOT_NAME = os.getenv('DISCORD_BOT_NAME')
SECRET_KEY = os.getenv('SECRET_KEY')
API_URL = os.getenv('API_URL')

# Define the bot with intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Check if the message is in the specified channel and mentions the bot
    if message.channel.id != CHANNEL_ID or BOT_NAME not in message.content:
        return

    response = handle_message(message.content, BOT_NAME, SECRET_KEY, API_URL)
    if response:
        await message.channel.send(response)

# Run the bot with the token
client.run(os.getenv('DISCORD_TOKEN'))

