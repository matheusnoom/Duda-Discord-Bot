import discord
import openai
from decouple import config
from discord.ext import commands

from src.Service.operationChannel import OperationChannel
from src.Views.deleteButton import DeleteButton


class ChatOpenAiChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.operationChannel = OperationChannel(bot)
        self.user_contexts = {}  # Dicionário para armazenar os contextos dos usuários

    @commands.command(name="canalgpt", help="!canalgpt - Cria um canal para interagir com o ChatOpenAi")
    async def chatopenaichannel(self, ctx):
        channeldetail = await self.operationChannel.create_channel(ctx)
        embed = discord.Embed(title="ChatOpenAi",
                              description="Esse canal está disponível apenas para você, então fique tranquilo.",
                              color=0xdddddd)
        embed.add_field(name="Resposta do chat OpenAi",
                        value="Algumas respostas podem demorar por conta do tempo de resposta do OpenAi.", inline=False)
        embed.add_field(name="Resposta do chat OpenAi",
                        value="Para encerrar o canal basta clicar no botão de excluir canal.", inline=False)
        delete_button = DeleteButton(self.operationChannel, channeldetail)
        await channeldetail.send(embed=embed, view=delete_button)

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
        try:
            openai.api_key = config('OPENAI_API_KEY')

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0301",
                messages=context,
                temperature=0.7,
                max_tokens=150
            )
            return response
        except Exception as e:
            return f"Não foi possível se conectar ao OpenAi: {e}"

    async def delete_user_context(self, channel_id):
        if channel_id in self.user_contexts:
            del self.user_contexts[channel_id]


async def setup(bot):
    await bot.add_cog(ChatOpenAiChannel(bot))
