import openai
from decouple import config
from discord.ext import commands

from Services.operationChannel import OperationChannel


class ChatOpenAiChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.operationChannel = OperationChannel(bot)
        self.user_contexts = {}  # Dicionário para armazenar os contextos dos usuários

    @commands.command(name="gptteste", help="!gptteste - Cria um canal para interagir com o bot")
    async def chatopenaichannel(self, ctx):
        await self.operationChannel.create_channel(ctx)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.author.id not in self.operationChannel.messageMap:
            return
        if message.channel.id not in self.operationChannel.messageMap[message.author.id]:
            return
        if message.content.startswith("!"):
            return

        channel = message.channel.id
        user_context = self.user_contexts.get(channel, [])

        user_context.append({"role": "user", "content": message.content})

        response = await self.send_to_openai(user_context)

        reply = response.choices[0].message.content

        user_context.append({"role": "assistant", "content": reply})
        self.user_contexts[channel] = user_context
        await message.channel.send(reply)

    async def send_to_openai(self, context):
        openai.api_key = config('APIKEY')

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=context,
            temperature=0.7,
            max_tokens=150
        )
        return response


async def setup(bot):
    await bot.add_cog(ChatOpenAiChannel(bot))
