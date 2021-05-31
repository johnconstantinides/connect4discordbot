import discord
from discord.ext import commands
import json
import os

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready')

client.load_extension("cogs.connect4")


client.run('ODQ3NjYwNDk3MjU2MTg1ODc3.YLBTWw.3-wP7sIl2mYB9efVC4_JdvF9Rv0')