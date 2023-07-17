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
        return channel

    async def delete_channel(self, channel):
        channel_id = channel.id
        for author in self.messageMap:
            for id in self.messageMap[author]:
                if id == channel_id:
                    self.messageMap[author].remove(id)
                    break
        await self.bot.get_cog("ChatOpenAiChannel").delete_user_context(channel_id)
        await channel.delete()
