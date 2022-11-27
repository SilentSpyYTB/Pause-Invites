import os
import discord
from discord import app_commands
from discord.app_commands import Choice
from dotenv import load_dotenv

load_dotenv()

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"{self.user} logged in")


bot = client()
tree = app_commands.CommandTree(bot)

@tree.command(name="pause-invites", description="Pauses invites")
@app_commands.default_permissions()
@app_commands.describe(state="Whether invites should be on or off")
@app_commands.choices(state=[Choice(name="On", value=1), Choice(name="Off", value=0)])
async def pause(interaction:discord.Interaction, state: Choice[int]):
    if state.value == 1: state = True
    else: state = False

    await interaction.guild.edit(invites_disabled=state)
    if state:
        await interaction.response.send_message(ephemeral=True, content="Invites have been paused")
    else:
        await interaction.response.send_message(ephemeral=True, content="Invites have been resumed")


bot.run(os.getenv('TOKEN'))