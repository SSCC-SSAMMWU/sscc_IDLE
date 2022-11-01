import discord
from discord import app_commands, Interaction, Object
from discord.ui import Button, View
from discord import ButtonStyle


class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)


    @discord.ui.button(label="Green Button",style=discord.ButtonStyle.green) # or .success
    async def green_button(self, button: Button, interaction: Interaction):
        print(Interaction.response)
        # interaction.disabled=True
        await interaction.response.send_message("You clicked the green button!", ephemeral=True)

# class Buttons(discord.ui.View):
#     def __init__(self, *, timeout=180):
#         super().__init__(timeout=timeout)
#
#     @app_commands.command(name="버튼")
#     async def button(self, interaction: Interaction) -> None:
#         button1 = Button(label="버튼1", style=ButtonStyle.primary)
#     # async def gray_button(self, button: discord.ui.Button, interaction: Interaction):
#     #     # await interaction.message.edit(content=f"This is an edited button response!")
#     #     # await interaction.channel.send("This message has buttons!", view=Buttons())
#     #     print(interaction.response)
#     async def button1_callback(interaction: Interaction):
#         await interaction.response.send_message("1번입니다.")

# 봇 앱 작성
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.content == 'ping':
            # await message.channel.send('pong')
            await message.channel.send("This message has buttons!", view=Buttons())


# 봇 실행부
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('NzExNDc0NDYwODEyNjQwMjU3.GkNOW8.piKoo50G68lEJmbBCaNG-S67YEl15nm5R7Cf88')

#  # ButtonType().Primary
#  # ButtonType().Success
#  # ButtonType().Secondary
#  # ButtonType().Danger
#  # ButtonType().Link
