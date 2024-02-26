import discord
import asyncio
from discord.ext import commands
from discord.ui import Button, View, MentionableSelect
from discord import Message
from dotenv import load_dotenv
from DB.verifyClaims import has_claimed
from DB.postTwitterUsername import postTweeterUsername
from utils.allotPoints import allotPointsToInteraction
from DB.getTweetUsername import getTweeterUsername
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
@bot.command()
async def addTweet(ctx, title:str, tweetId:str, description:str, imgUrl:str):

    embedMsg = discord.Embed(
        title=title, 
        url="https://twitter.com/BakeStake/status/"+str(tweetId), 
        description=description, 
        color=discord.Color.blue()
    )
    embedMsg.set_thumbnail(url=imgUrl)
    embedMsg.set_footer(text="SNB Xstream will reward you with points on following interactions")

    likeButton = Button(label="Like ❤️", style=discord.ButtonStyle.green, row=4,url="https://twitter.com/intent/like?tweet_id="+tweetId)
    commentButton = Button(label="Comment 💬", style=discord.ButtonStyle.secondary, row=4, url="https://twitter.com/intent/post?in_reply_to="+tweetId)
    rtButton = Button(label="RT 🔁", style=discord.ButtonStyle.blurple, row=4, url="https://twitter.com/intent/retweet?tweet_id="+tweetId)

    view = View()
    view.add_item(likeButton)
    view.add_item(commentButton)
    view.add_item(rtButton)

    await ctx.send("A New Tweet out now, LFG raid it",embed=embedMsg,view=view)

@bot.command()
async def openClaims(ctx, tweetId):

    claimLike = Button(label="Claim ❤️ points", style=discord.ButtonStyle.green, row=3)
    claimCmnt = Button(label="Claim 💬 points", style=discord.ButtonStyle.secondary, row=3)
    claimRT = Button(label="Claim 🔁 points", style=discord.ButtonStyle.blurple, row=3)

    view = View()

    view.add_item(claimLike)
    view.add_item(claimCmnt)
    view.add_item(claimRT)

    async def claimLikeCallback(interaction:discord.interactions):
        print(interaction.user.name)
        await interaction.response.send_message("lemme check if "+interaction.user.name+" like it",ephemeral=True)
        username = await getTweeterUsername(interaction.user.name)
        if username == None:
            await interaction.followup.send("Link twitter username using /linkTwitter" ,ephemeral=True)
        res = await has_claimed(interaction.user.name, tweetId, 0)
        if(res == False):
            ponts = await allotPointsToInteraction(0, tweetId, username, interaction.user.name)
            if ponts == 0:
                await interaction.followup.send("haven't liked tweet with "+username+" id",ephemeral=True)
            else:
                await interaction.followup.send("credited your points @"+interaction.user.name,ephemeral=True)
        else:
            await interaction.followup.send("Already claimed points @"+interaction.user.name,ephemeral=True)
        
    
    async def claimCmntCallback(interaction:discord.interactions):
        await interaction.response.send_message("lemme check if "+interaction.user.name+" commented on it",ephemeral=True)
        username = await getTweeterUsername(interaction.user.name)
        if username == None:
            await interaction.followup.send("Link twitter username using /linkTwitter",ephemeral=True)
        res = await has_claimed(interaction.user.name, tweetId, 1)
        if(res == False):
            ponts = await allotPointsToInteraction(1, tweetId, username, interaction.user.name)
            if ponts == 0:
                await interaction.followup.send("haven't commented on tweet with "+username+" id",ephemeral=True)
            else:
                await interaction.followup.send("credited your points @"+interaction.user.name,ephemeral=True)
        else:
            await interaction.followup.send("Already claimed points @"+interaction.user.name)

    async def claimRTCallback(interaction:discord.interactions):
        await interaction.response.send_message("lemme check if "+interaction.user.name+" RT it",ephemeral=True)
        username = await getTweeterUsername(interaction.user.name)
        if username == None:
            await interaction.followup.send("Link twitter username using /linkTwitter",ephemeral=True)
        res = await has_claimed(interaction.user.name, tweetId, 2)
        if(res == False):
            ponts = await allotPointsToInteraction(2, tweetId, username, interaction.user.name)
            if ponts == 0:
                await interaction.followup.send("haven't RTed tweet  "+username+" id",ephemeral=True)
            else:
                await interaction.followup.send("credited your points @"+interaction.user.name,ephemeral=True)
        else:
            await interaction.followup.send("Already claimed points @"+interaction.user.name,ephemeral=True)

    claimLike.callback = claimLikeCallback 
    claimCmnt.callback = claimCmntCallback
    claimRT.callback = claimRTCallback

    await ctx.send("Claim the points for your raiding it",view=view)

@bot.command(pass_context=True)
async def linkTwitter(ctx, username):
    await postTweeterUsername(ctx.message.author.name, username)
    await ctx.reply("Registered twitter")



bot.run(os.getenv("BOT_TOKEN"))

