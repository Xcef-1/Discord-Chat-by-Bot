import os
import nextcord
from nextcord.ext import commands
import asyncio
from dotenv import load_dotenv

load_dotenv()

# Configuration from .env
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
TARGET_USER_ID = int(os.getenv('TARGET_USER_ID'))

intents = nextcord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')
    await start_dm_session()

async def start_dm_session():
    try:
        # Get the target user
        target_user = await bot.fetch_user(TARGET_USER_ID)
        if target_user is None:
            print(f"Error: User with ID {TARGET_USER_ID} not found")
            await bot.close()
            return

        # Open DM channel
        dm_channel = await target_user.create_dm()
        print(f"DM session started with {target_user.name}#{target_user.discriminator}")
        print("Type your message (or 'exit' to quit):")

        # Start message loop
        while True:
            # Get input from console
            message_content = await asyncio.get_event_loop().run_in_executor(None, input, "You: ")
            
            if message_content.lower() == 'exit':
                break
                
            if message_content:
                await dm_channel.send(message_content)
                print(f"Sent: {message_content}")

    except nextcord.Forbidden:
        print("Error: The user has DMs disabled or blocked the bot")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await bot.close()

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
        
    # Check if message is from our target user in a DM
    if isinstance(message.channel, nextcord.DMChannel) and message.author.id == TARGET_USER_ID:
        print(f"\n{message.author.name}: {message.content}")
        
    # Process commands if needed
    await bot.process_commands(message)

# Run the bot
if __name__ == "__main__":
    bot.run(BOT_TOKEN)