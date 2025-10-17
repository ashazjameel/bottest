import os
import discord
from discord.ext import commands
from discord import app_commands
from speedruncompy import *
from time import sleep as wait
from keep_alive import keep_alive
import asyncio

keep_alive()

first = "<:1st:1427708892678455477>"
second = "<:2nd:1427708891390541925>"
third = "<:3rd:1427708889499176960>"
fourth = "<:4th:1427783463481639024>"


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
    await bot.tree.sync()
    bot.tree.clear_commands()
    await bot.tree.sync()
    #await tree.sync(guild=discord.Object(id=guildid))
    print("Ready!")
    """
    # Clear ALL slash commands from this guild
    await bot.tree.sync(guild=discord.Object(id=guildid))
    bot.tree.clear_commands(guild=discord.Object(id=guildid))
    await bot.tree.sync(guild=discord.Object(id=guildid))"""

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
    #guild=discord.Object(id=guildid)
)
async def statlookup(interaction: discord.Interaction, username: str):#(ctx, username: str): #interaction: discord.Interaction, username: str):
    if username is None:
        await interaction.response.send_message("no username provided")        #ts never runs lol
        #await ctx.send("no username provided")
        return
        
    ep = "j1nermw1"
    ep_ce = "9do8wj31"
    #username = "Emmir44"# "William_Swordsmith"
    try:
        userid1 = await GetUserSummary(username).perform_async()
    except:
        await interaction.response.send_message("User not found")
        return 0
    userid = userid1.user.id

    ldr = await GetUserLeaderboard(userid).perform_async()
    runs = ldr.runs

    ep_ldr = {1:0,2:0,3:0,4:0}
    epce_ldr = {1:0,2:0,3:0,4:0}
    b = " ‎ ‎ ‎"

    for i in runs:
        if i.place != None and (i.gameId == ep or i.gameId == ep_ce):
            place = i.place
            if i.gameId == ep:
                if 1 <= place <= 4:
                    ep_ldr[place] += 1             
            elif i.gameId == ep_ce:
            
                if 1 <= place <= 4:
                    epce_ldr[place] += 1
                    
    print("Username:",username,"Entry Point",ep_ldr,"Entry Point Category Extensions",epce_ldr)
    #await interaction.response.send_message(f"Username: {username} Entry Point {ep_ldr} Entry Point Category Extensions {epce_ldr}")
    description = f"Entry Point:‎‎ {b} {first} {ep_ldr[1]} {b} {second} {ep_ldr[2]} {b} {third} {ep_ldr[3]} {b} {fourth} {ep_ldr[4]} \n Entry Point Category Extensions: {b} {first} {epce_ldr[1]} {b} {second} {epce_ldr[2]} {b} {third} {epce_ldr[3]} {b} {fourth} {epce_ldr[4]}"
    title = f"{username}'s stats"
    embed = discord.Embed(title=title,description=description,color=0x00ff00)
    embed.add_field(name="Field1", value="hi", inline=False)
    embed.add_field(name="Field2", value="hi2", inline=False)
    await interaction.response.send_message(embed=embed)




#if __name__ == "__main__":
    #threading.Thread(target=run_web).start()
bot.run(TOKEN)
