import asyncio
import os

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
    for file in os.listdir("Commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            await bot.load_extension(f'Commands.{cog}')


async def main():
    await load_cogs()
    await bot.start(config('TOKEN'))


asyncio.run(main())