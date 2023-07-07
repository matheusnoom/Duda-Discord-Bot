import discord
import requests
from decouple import config
from discord.ext import commands


class WatchTogether(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="w2g", help="Cria uma sala no Watch2Gether.")
    async def watchtogether(self, ctx):
        url = "https://api.w2g.tv/rooms/create.json"

        headers = {"Content-Type": "application/json",
                   "Accept": "application/json"}
        data = {
            "w2g_api_key": config("W2G_API_KEY"),
            "bg_color": "#4F4F4F",
            "bg_opacity": "50"
        }

        response = requests.post(url, headers=headers, json=data)

        embed = discord.Embed(
            title=f"Watch2Gether",
            description=f"https://w2g.tv/rooms/{response.json()['streamkey']}",
            color=0x5A5A5A)
        embed.set_thumbnail(url="https://i.imgur.com/RGSi4uC.jpg")
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(WatchTogether(bot))
