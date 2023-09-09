from discord.ext import commands


class Talks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if "duda" in message.content.lower():
            await message.channel.send('Auau!')


async def setup(bot):
    await bot.add_cog(Talks(bot))
