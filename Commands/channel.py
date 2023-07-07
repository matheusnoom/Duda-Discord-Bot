import asyncio

from discord.ext import commands


class ChannelCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help='Deleta todas mensagens do canal.')
    @commands.has_permissions(administrator=True)
    async def deleteall(self, ctx):
        asyncio.create_task(ctx.channel.purge())

    @commands.command(help='!delete <quantidade> - Delete um numero especifico de mensagens.')
    @commands.has_permissions(administrator=True)
    async def delete(self, ctx, limit: int):
        asyncio.create_task(ctx.channel.purge(limit=limit + 1))


async def setup(bot):
    await bot.add_cog(ChannelCommands(bot))
    return ChannelCommands(bot)