import discord
from discord.ext import commands


class OperationChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.messageMap = {}

    async def create_channel(self, ctx):
        guild = ctx.guild
        author = ctx.author

        # Cria o canal de texto
        category = discord.utils.get(guild.categories, name='Chat DudaGPT')

        if category is None:
            category = await guild.create_category_channel("Chat DudaGPT")

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
            author: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            self.bot.user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }

        channel = await guild.create_text_channel(f"channel-{author.name}", category=category, overwrites=overwrites)

        # Armazena o ID do canal para uso posterior
        if author.id not in self.messageMap:
            self.messageMap[author.id] = []

        self.messageMap[author.id].append(channel.id)

        await ctx.send(f"Canal de texto criado: {channel.mention}")
        return self.messageMap

    async def delete_channel(self, ctx):
        author = ctx.author
        actualChannel = ctx.channel

        if author.id not in self.messageMap or actualChannel.id not in self.messageMap[author.id]:
            return await ctx.send("Você não tem permissão para deletar este canal!")

        # Remove o ID do canal do dicionário
        self.messageMap[author.id].remove(actualChannel.id)
        if not self.messageMap[author.id]:
            del self.messageMap[author.id]

        # Remove o canal de texto atual
        await actualChannel.delete()

        await ctx.send(f"Canal de texto removido: {actualChannel.mention}")