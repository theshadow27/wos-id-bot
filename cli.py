import os
from bot_logic import handle_message

def main():
    # Load configuration from environment variables
    CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')
    BOT_NAME = os.getenv('DISCORD_BOT_NAME')
    SECRET_KEY = os.getenv('SECRET_KEY')
    API_URL = os.getenv('API_URL')

    if not all([CHANNEL_ID, BOT_NAME, SECRET_KEY, API_URL]):
        print("Error: Missing environment variables. Please set DISCORD_CHANNEL_ID, DISCORD_BOT_NAME, SECRET_KEY, and API_URL.")
        return

    # Simulate the bot's behavior
    print("Welcome to the Discord Bot CLI Tester!")
    print(f"Bot Name: {BOT_NAME}")
    print(f"Channel ID: {CHANNEL_ID}")
    print(f"API URL: {API_URL}")
    
    while True:
        message = input("\nEnter a message (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        if BOT_NAME in message:
            response = handle_message(message, BOT_NAME, SECRET_KEY, API_URL)
            print(f"Bot Response:\n{response}")
        else:
            print("Bot name not mentioned in the message. Try again.")

if __name__ == "__main__":
    main()
