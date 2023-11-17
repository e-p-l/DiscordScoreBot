import discord
import os
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="$",intents=intents)

valid_users_ids = []
team1 = []
team2 = []
score = {}

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def display_scoreboard(ctx):
    global score
    await ctx.channel.send("Voyons voir qui a perdu le plus de partie...")

    sorted_score = {}
    sorted_keys = sorted(score,key=score.get)

    for w in sorted_keys:
        sorted_score[w] = score[w]
        
    for name in sorted_score:
        await ctx.channel.send(name+" : "+str(sorted_score[name]))

@bot.command()
async def logout(ctx):
    await ctx.channel.send("C'est off bye.")
    await bot.logout()

@bot.command()
async def make_teams(ctx):
    global team1
    global team2

    #Add the channel id's to build teams from them
    channel1_id = None
    channel2_id = None

    channel1 = bot.get_channel(channel1_id)
    channel2 = bot.get_channel(channel2_id)

    team1 = []
    team2 = []

    for member in channel1.members:
        team1.append(member.id)
    
    for member in channel2.members:
        team2.append(member.id)

@bot.command()
async def add_user(ctx, user_id):
    if user_id not in valid_users:   
        valid_users.append(user_id)

@bot.command()
async def show_valid_users(ctx):
    global valid_users

    for user_id in valid_users:
        await ctx.channel.send(bot.get_user(user_id).name)

@bot.command()
async def show_teams(ctx):
    global team1
    global team2 

    await ctx.channel.send("Team 1 :")
    for player in team1:
        await ctx.channel.send(bot.get_user(player).name)
    await ctx.channel.send("Team 2 :")
    for player in team2:
        await ctx.channel.send(bot.get_user(player).name)
    
@bot.command()
async def add_win(ctx,team):
    global team1
    global team2

    if team in ["team1","1","Team1"]:
        await ctx.channel.send("Victoire de team 1")
        for user_id in team1:
            if bot.get_user(user_id).name not in score:
                score[bot.get_user(user_id).name] = 1
            else:
                score[bot.get_user(user_id).name] += 1

    if team in ["team2","2","Team2"]:
        await ctx.channel.send("Victoire de team 2")
        for user_id in team2:
            if bot.get_user(user_id).name not in score:
                score[bot.get_user(user_id).name] = 1
            else:
                score[bot.get_user(user_id).name] += 1

# replace by your discord secret key
key = None
bot.run(key)