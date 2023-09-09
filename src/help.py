import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Comandos",
                              description="Aqui estão os comandos disponíveis:",
                              color=0xdddddd)
        for command in self.bot.commands:
            if command.name != "help":
                embed.add_field(name=f"!{command.name}", value=command.help, inline=False)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot))
