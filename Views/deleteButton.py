import discord


class DeleteButton(discord.ui.View):
    def __init__(self, operation_channel, chaneldetail):
        super().__init__()
        self.operation_channel = operation_channel
        self.chaneldetail = chaneldetail

    @discord.ui.button(label='Excluir Canal', style=discord.ButtonStyle.red)
    async def delete_channel(self, button: discord.ui.Button, interaction: discord.Interaction):
        await self.operation_channel.delete_channel(self.chaneldetail)
        await interaction.channel.delete()
