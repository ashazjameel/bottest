import os
import discord
from discord.ext import commands
from discord import app_commands
from speedruncompy import *

guildid = 793898712806981673
TOKEN = os.environ['BOT_TOKEN']  # Fetch token from Render

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await tree.sync(guild=discord.Object(id=guildid))
    print("Ready!")

###slash command###
                    
@tree.command(
    name="commandname",
    description="My first application Command",
    guild=discord.Object(id=guildid)
)
async def first_command(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")
    
###################
                    
@bot.command()
async def statlookup(ctx, username: str):
    if username == "":
        await ctx.send("no username provided")
        return
        
    ep = "j1nermw1"
    ep_ce = "9do8wj31"
    #username = "Emmir44"# "William_Swordsmith"
    userid1 = await GetUserSummary(username).perform_async()
    userid = userid1.user.id

    ldr = await GetUserLeaderboard(userid).perform_async()
    runs = ldr.runs

    ep_ldr = {1:0,2:0,3:0}
    epce_ldr = {1:0,2:0,3:0}

    for i in runs:
        if i.place != None and (i.gameId == ep or i.gameId == ep_ce):
            place = i.place
            if i.gameId == ep:
                if 1 <= place <= 3:
                    ep_ldr[place] += 1             
            elif i.gameId == ep_ce:
            
                if 1 <= place <= 3:
                    epce_ldr[place] += 1
                    
    print("Username:",username,"Entry Point",ep_ldr,"Entry Point Category Extensions",epce_ldr)
    await ctx.send(f"Username: {username} Entry Point {ep_ldr} Entry Point Category Extensions {epce_ldr}")
    embed = discord.Embed(title="title",description="description")
    embed_message = await ctx.send(embed=embed)

bot.run(TOKEN)
