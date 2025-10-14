import os
import discord
from discord.ext import commands
from discord import app_commands
from speedruncompy import *



from flask import Flask
from threading import Thread

app = Flask("")

@app.route("/")
def home():
    return "Bot is running!"

def run():
    app.run(host="0.0.0.0", port=10000)

# Start Flask in a background thread
t = Thread(target=run)
t.start()




guildid = 793898712806981673
TOKEN = os.environ['BOT_TOKEN']  # Fetch token from Render

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='/', intents=intents)
app_commands.CommandTree(client)
#tree = app_commands.CommandTree(client)
tree = bot.tree

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await tree.sync(guild=discord.Object(id=guildid))
    print("Ready!")
    # Clear ALL slash commands from this guild
    await bot.tree.sync(guild=discord.Object(id=guildid))
    bot.tree.clear_commands(guild=discord.Object(id=guildid))
    await bot.tree.sync(guild=discord.Object(id=guildid))

###slash command###
                    
#async def first_command(interaction: discord.Interaction):
    #await interaction.response.send_message("Hello!")
    
###################
                 
#@tree.command(
#    name="lookup",
#    description="Checks a user's runs",
#    guild=discord.Object(id=guildid)
#)

#@bot.command()
@tree.command(
    name="statslookup",
    description="Checks a user's stats",
    guild=discord.Object(id=guildid)
)
async def statlookup(interaction: discord.Interaction, username: str):#(ctx, username: str): #interaction: discord.Interaction, username: str):
    if username is None:
        await interaction.response.send_message("no username provided")        #ts never runs lol
        #await ctx.send("no username provided")
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
    #await interaction.response.send_message(f"Username: {username} Entry Point {ep_ldr} Entry Point Category Extensions {epce_ldr}")
    #await ctx.send(f"Username: {username} Entry Point {ep_ldr} Entry Point Category Extensions {epce_ldr}")
    embed = discord.Embed(title=f"{username}'s stats",description="description")
    await interaction.response.send_message(embed=embed)

bot.run(TOKEN)
