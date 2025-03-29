# Discord Chat by Bot

A versatile Discord bot that enables communication through either a specific server channel or direct messages with a target user. Built with Nextcord.

## Features

- **Server Channel Chat**: Communicate through a specific channel in a Discord server
- **Direct Message Chat**: Have private conversations with a specific user
- **Cross-platform**: Works on Windows, MacOS, and Linux
- **Real-time messaging**: Send and receive messages in real-time

## Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Discord bot token (from [Discord Developer Portal](https://discord.com/developers/applications))
- Bot added to your server with appropriate permissions

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/discord-chat-bot.git
   cd discord-chat-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the bot:
   - Edit the `.env` file with your credentials:
     ```
     DISCORD_BOT_TOKEN=your_bot_token_here
     TARGET_SERVER_ID=123456789012345678  # Only for server channel chat
     TARGET_CHANNEL_ID=123456789012345678 # Only for server channel chat
     TARGET_USER_ID=123456789012345678    # Only for direct message chat
     ```

## Usage

### Windows

#### Requirements
- Python 3.8+
- [Git](https://git-scm.com/downloads/win) (optional, for cloning)

#### How to Use
1. Open Command Prompt in the project directory
2. To use server channel chat:
   ```cmd
   python Chat_by_Discord_Bot_in_Server.py
   ```
3. To use direct message chat:
   ```cmd
   python Chat_by_Discord_Bot_with_User.py
   ```
4. Type your messages in the console (type 'exit' to quit)

### MacOS

#### Requirements
- Python 3.8+ (install via Homebrew: `brew install python`)
- Git (optional)

#### How to Use
1. Open Terminal in the project directory
2. To use server channel chat:
   ```bash
   python3 Chat_by_Discord_Bot_in_Server.py
   ```
3. To use direct message chat:
   ```bash
   python3 Chat_by_Discord_Bot_with_User.py
   ```
4. Type your messages in the terminal (type 'exit' to quit)

### Linux

#### Requirements
- Python 3.8+ (usually pre-installed)
- pip (install via package manager if needed)
- Git (optional)

#### How to Use
1. Open terminal in the project directory
2. To use server channel chat:
   ```bash
   python3 Chat_by_Discord_Bot_in_Server.py
   ```
3. To use direct message chat:
   ```bash
   python3 Chat_by_Discord_Bot_with_User.py
   ```
4. Type your messages in the terminal (type 'exit' to quit)

## Bot Permissions

Ensure your bot has these permissions in your server:
- View Channels
- Send Messages
- Read Message History

For DM functionality, users must have "Allow direct messages from server members" enabled in their privacy settings.

## Troubleshooting

- **Bot not responding**: Check if the bot is online and has proper permissions
- **DM not working**: Verify the target user hasn't blocked the bot and has DMs enabled
- **Channel not found**: Confirm the channel ID is correct and the bot has access
- **Module errors**: Ensure all dependencies are installed (`pip install -r requirements.txt`)

## License

This project is open-source and available under the MIT License.

## Support
For issues or questions, please open an issue on GitHub.
