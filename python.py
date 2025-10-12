import os
import discord
from discord.ext import commands

TOKEN = os.environ['BOT_TOKEN']  # Fetch token from Render

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello from Render!")

bot.run(TOKEN)
