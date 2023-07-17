import discord
import openai
from decouple import config
from discord.ext import commands


class ChatOpenAi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gpt", help="!gpt <texto> - Faça uma pergunta ao chata OpenAI")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def chatopenai(self, ctx, *, text):
        openai.api_key = config('APIKEY')

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=[
                {"role": "user", "content": f"{text}"}
            ],
            temperature=0.5,
            max_tokens=150
        )
        embed = discord.Embed(
            title=f"DudaGPT",
            description=f"{text}",
            color=0xdddddd)
        embed.add_field(name="Resposta:", value=f"{completion.choices[0].message.content}", inline=False)
        embed.set_thumbnail(url="https://i.imgur.com/RGSi4uC.jpg")
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(ChatOpenAi(bot))
