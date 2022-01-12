import discord
from discord.ext import commands
import json
import os

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready')

client.load_extension("cogs.connect4")


client.run(key)