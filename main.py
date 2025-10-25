import os
import discord
from discord.ext import commands
from discord import app_commands
from speedruncompy import *
from time import sleep as wait
from keep_alive import keep_alive
import asyncio
from PIL import Image
import requests
from io import BytesIO

keep_alive()

first = "<:1st:1427708892678455477>"
second = "<:2nd:1427708891390541925>"
third = "<:3rd:1427708889499176960>"
fourth = "<:4th:1427783463481639024>"
colours = {"44BBEE":"gw3r7nq7","6666EE":"1x3216j7","E77471":"ew6x2n47","FF3091":"qr3jl64g","8AC951":"w461onv1","C279E5":"pw37o6d7","FFB3F3":"e7nmx3ym","09B876":"rq69m391","EF8241":"9j3po614","F772C5":"ryndx3gd","A010A0":"1y6emnpv","EE4444":"4e3w46z5","B8B8B8":"296vz3ve","FFFFFF":"kr3q9nwx","F0C03E":"gy3l7n4l"}
countries = {"a":"🇦", "b":"🇧", "c":"🇨", "d":"🇩", "e":"🇪", "f":"🇫", "g":"🇬", "h":"🇭", "i":"🇮", "j":"🇯", "k":"🇰", "l":"🇱", "m":"🇲", "n":"🇳", "o":"🇴", "p":"🇵", "q":"🇶", "r":"🇷", "s":"🇸", "t":"🇹", "u":"🇺", "v":"🇻", "w":"🇼", "x":"🇽", "y":"🇾", "z":"🇿",}

ep = "j1nermw1"
ep_ce = "9do8wj31"

levelList_ep = {"The Blacksite":"y9mr34lw", "The Financier":"5wkno45w", "The Deposit":"5928leg9", "The Lakehouse":"29vlxg1w", "The Withdrawal":"xd4yzp0d", "The Scientist":"rdnl83nw",  "The SCRS":"ldy56qjw",  "Black Dusk":"gdr8lr89", "The Killhouse":"xd02yp09", "The Auction":"rw6lx2nw", "The Gala":"n93nek7w", "The Cache":"z98zqp79", "The Setup":"ldykqozw", "Lockup":"gdrorzzd", "Score":"nwlz08rd", "The Concept":"ewp3l2kd"}
levelList_epce = {"The Blacksite":"n93z56nw", "The Financier":"z984v1gw", "The Deposit":"rdn4jeq9", "The Lakehouse":"ldyl7mk9", "The Withdrawal":"gdr6456d", "The Scientist":"nwl4xr09", "The SCRS":"ywexk6y9", "Black Dusk":"69zeokl9", "The Killhouse":"r9gq0v5d", "The Auction":"o9xr5p09", "The Gala":"495xo70d", "The Cache":"rdq42xk9", "The Setup":"5d7qkogw", "The Lockup":"kwj4lnnw", "The Score":"owo41zo9", "The Concept":"29v83xqd"}

catlist_ep = {"Story %":"7dgnl742", "Solo":"jdrvo6l2", "Genocide":"q25mo88d", "Pacifist":"824geme2", "Ironman Solo":"vdo8wnok", "Trio":"02q3mw9k", "Duo":"jdz96062", "Ironman Multiplayer":"wkp16rvk", "Quad":"824gjen2", "Story % Multiplayer":"9kvo0j32", "100% Multiplayer":"rkllpe8k", "Ironman Genocide":"rkl3lz6k", "Freelancer":"wdmxn43k", "Ironman Pacifist":"w203pw52", "100%":"mke9379d", "Sabotaged Halcyon":"wdmxvo3k", "Planned The Final Strike":"wkp10e8k"}
catlist_epce = {"No Perks":"wdm5oj32", "No Disguise":"wk60e7qk", "Armed and Armoured":"7kjo8pn2", "No Armor":"n2ye95zk", "Loud":"vdozgpvk", "Take out the trash":"9kvq6mod", "Take out the trash (Full Game)":"mkevlz82", "Pierre%":"9d8oe662", "Firing Range%":"5dw965e2", "Leveling":"jdr9o7gd"}
# ^^^ organise ts if u want




guildid = 793898712806981673
TOKEN = os.environ['BOT_TOKEN']  # Fetch token from Render
IMAGE_API_KEY = os.environ['IMAGE_API_KEY']

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
        
    #username = "Emmir44"# "William_Swordsmith"
    try:
        userid1 = await GetUserSummary(username).perform_async()
    except:
        await interaction.response.send_message("User not found")
        return 0
    userid = userid1.user.id

    link1 = await GetUserSummary(username).perform_async()
    images = link1.user.staticAssets
    if len(images) != 0:
        link = "/static/user/qjo0qgnj/image.png?v=44e25be"
        for i in images:
            if i["assetType"] == "image":
                link = i.path
    else:
        link = "/static/user/qjo0qgnj/image.png?v=44e25be"
    f = Image.open(BytesIO(requests.get(f"https://www.speedrun.com{link}").content))
    image_link = f"https://cdn.filestackcontent.com/{IMAGE_API_KEY}/resize=width:{min(f.size)},height:{min(f.size)},fit:crop/https://www.speedrun.com{link}"
    #image_link = "https://cdn.filestackcontent.com/AA3hldwYkSYG026IjoXhYz/resize=width:400,height:400,fit:crop/https://www.speedrun.com/static/user/qjo0qgnj/image.png?width=600&height=4600"
    country = link1.user.areaId.split("/")[0]
    countryId = ""
    for i in country:
        countryId += countries[i.lower()]
    #countryId = "🇬🇧"     #test
    
    #link = "/static/user/j9516yv8/image.jpg?v=e87ae57"
    ldr = await GetUserLeaderboard(userid).perform_async()
    runs = ldr.runs
    username = ldr.user.name
    colour1 = ldr.user.color1Id
    colour = "FF0000"
    for key, value in colours.items():
        if value == colour1:
            colour = key

    ep_ldr = {1:0,2:0,3:0,4:0}
    epce_ldr = {1:0,2:0,3:0,4:0}
    b = " ‎ ‎ ‎"               #white-space

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
    embed = discord.Embed(title=title,description=description,color=int(colour, 16))
    embed.set_author(name=username, icon_url=image_link)#f"https://www.speedrun.com{link}") #"https://www.speedrun.com/static/user/j9516yv8/image.jpg?v=e87ae57")
    #embed.set_author(name=username, icon_url="https://www.speedrun.com/static/user/j9516yv8/image.jpg?v=e87ae57")   good
    #embed.set_thumbnail(url="https://www.speedrun.com/static/user/j9516yv8/image.jpg?v=e87ae57")     ts more like a thumbnail icl
    #embed.add_field(name="Field1", value="hi", inline=False)             #use ts for the profile
    await interaction.response.send_message(embed=embed)


@tree.command(
    name="leaderboard",
    description="Shows the leaderboard for a given category",
)
async def leaderboard(interaction: discord.Interaction):
    player_list = []
    for i,v in catlist_ep.items():
        print(v,flush=True)
        ldr = await GetGameLeaderboard2(gameId=ep, catergoryId=v).perform_async()
        plyr = ldr.playerList
        for x in plyr:
            if not(x.id in player_list):
                player_list.append(x.id)
    for i,v in catlist_epce.items():
        ldr = await GetGameLeaderboard2(gameId=ep_ce, catergoryId=v).perform_async()
        plyr = ldr.playerList
        for x in plyr:
            if not(x.id in player_list):
                player_list.append(x.id)
    await interaction.response.send_message(len(player_list))



bot.run(TOKEN)
