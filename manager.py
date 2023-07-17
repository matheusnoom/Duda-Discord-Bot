from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument, CommandNotFound


class Manager(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            return await ctx.send('Por favor, insira todos os argumentos.')
        if isinstance(error, CommandNotFound):
            return await ctx.send('Comando não encontrado.')
        if isinstance(error, commands.MissingPermissions):
            return await ctx.send('Vocé não tem permissão para executar este comando.')


async def setup(bot):
    await bot.add_cog(Manager(bot))
