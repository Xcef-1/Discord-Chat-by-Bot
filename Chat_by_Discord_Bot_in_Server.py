import os
import nextcord
from nextcord.ext import commands
import asyncio
from dotenv import load_dotenv

load_dotenv()

# Configuration from .env
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
TARGET_SERVER_ID = int(os.getenv('TARGET_SERVER_ID'))
TARGET_CHANNEL_ID = int(os.getenv('TARGET_CHANNEL_ID'))

# Set up bot with required intents
intents = nextcord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'\nLogged in as {bot.user.name} ({bot.user.id})')
    print('------')
    await setup_channel_communication()

async def setup_channel_communication():
    try:
        # Get target server and channel
        target_server = bot.get_guild(TARGET_SERVER_ID)
        if not target_server:
            print(f"Error: Not in server with ID {TARGET_SERVER_ID}")
            await bot.close()
            return

        target_channel = target_server.get_channel(TARGET_CHANNEL_ID)
        if not target_channel:
            print(f"Error: Channel {TARGET_CHANNEL_ID} not found")
            await bot.close()
            return

        print(f"Connected to #{target_channel.name} in {target_server.name}")
        print("Type your messages below (or 'exit' to quit):\n")

        # Start message loop
        while True:
            # Get user input (non-blocking)
            message = await asyncio.get_event_loop().run_in_executor(None, input, "You > ")
            
            if message.lower() == 'exit':
                await bot.close()
                return
                
            if message:
                await target_channel.send(message)
                print(f"Sent: {message}")

    except Exception as e:
        print(f"Error: {e}")
        await bot.close()

@bot.event
async def on_message(message):
    # Ignore bot's own messages
    if message.author == bot.user:
        return
        
    # Only show messages from target channel
    if message.channel.id == TARGET_CHANNEL_ID:
        # Format the output
        timestamp = message.created_at.strftime("%H:%M:%S")
        author = message.author.display_name
        print(f"\n[{timestamp}] {author}: {message.content}")
        
    await bot.process_commands(message)

# Clean shutdown handler
async def shutdown():
    print("\nBot is shutting down...")
    await bot.close()

if __name__ == "__main__":
    try:
        print("Starting Discord bot...")
        bot.run(BOT_TOKEN)
    except KeyboardInterrupt:
        asyncio.run(shutdown())
    except Exception as e:
        print(f"Fatal error: {e}")