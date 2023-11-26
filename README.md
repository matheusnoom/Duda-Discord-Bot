# Discord Bot Documentation

## Introduction
This document provides an overview of the Discord bot developed in Python using the following libraries:
- `discord.py` for Discord API interactions
- `openai` for communication with the OpenAI GPT-3 API
- `python-decouple` for handling environment variables
- `asyncio` for asynchronous programming

## Bot Functions

### 1. Delete Command
- **Command:** `!delete <quantity>`
- **Description:** Deletes a specific number of messages in the channel.

### 2. Create ChatOpenAI Channel Command
- **Command:** `!canalgpt`
- **Description:** Creates a channel for interacting with ChatOpenAI.

### 3. Delete All Messages Command
- **Command:** `!deleteall`
- **Description:** Deletes all messages in the channel.

### 4. Watch2Gether Command
- **Command:** `!w2g`
- **Description:** Creates a Watch2Gether room.

### 5. OpenAI Chat Command
- **Command:** `!gpt <text>`
- **Description:** Asks a question to the OpenAI Chat.

## Environment Variables (.env)

Ensure that you have a `.env` file in the root directory with the following variables:

- `OPENAI_API_KEY`: API key for OpenAI
- `W2G_API_KEY`: API key for Watch2Gether
- `TOKEN`: Discord bot token

Example `.env` file:
OPENAI_API_KEY=your_openai_api_key
W2G_API_KEY=your_w2g_api_key
TOKEN=your_discord_bot_token
