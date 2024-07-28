import asyncio
import os
import sys
from pathlib import Path

# Adiciona o diretório src ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import discord
from decouple import config
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command('help')

# Load Extensions
async def load_cogs():
    await bot.load_extension('help')
    await bot.load_extension('manager')

    commands_path = Path(__file__).parent / "Commands"
    for file in os.listdir(commands_path):
        if file.endswith(".py"):
            cog = file[:-3]
            await bot.load_extension(f'Commands.{cog}')

async def main():
    await load_cogs()
    await bot.start(config('TOKEN'))

asyncio.run(main())