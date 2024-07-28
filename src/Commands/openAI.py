import discord
import os
from openai import AsyncOpenAI
from decouple import config
from discord.ext import commands


class ChatOpenAi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gpt", help="!gpt <texto> - Faça uma pergunta ao chata OpenAI")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def chatopenai(self, ctx, *, text):
        try:
            client = AsyncOpenAI(
                api_key=os.environ['OPENAI_API_KEY']
            )

            response = await client.chat.completions.create(
                model="gpt-3.5-turbo",
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
            
            embed.add_field(name="Resposta:", value=f"{response.choices[0].message.content}", inline=False)
            embed.set_thumbnail(url="https://i.imgur.com/RGSi4uC.jpg")
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"Não foi possível se conectar ao OpenAi: {e}")


async def setup(bot):
    await bot.add_cog(ChatOpenAi(bot))
