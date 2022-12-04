import discord
from discord.ext import commands
import responses
import botToken

#I created a seperate file to hold the bot token since I don't want the token to go public
token = botToken.TOKEN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)



