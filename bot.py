import discord
from discord.ext import commands
import responses
import botToken
from botFunctions import *

#I created a seperate file to hold the bot token since I don't want the token to go public


token = botToken.TOKEN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def calc(ctx):
        def check(msg):
            return len(msg.content) >= 1 and msg.author != bot.user

        await ctx.send("Number 1: ")
        num_1 = await bot.wait_for("message", check=check)
        await ctx.send("Operator: ")
        operator = await bot.wait_for("message", check=check)
        await ctx.send("number 2: ")
        num_2 = await bot.wait_for("message", check=check)
        try:
            num_1 = float(num_1.content)
            operator = operator.content
            num_2 = float(num_2.content)
        except:
            await ctx.send("There was an invalid input")
            return
        output = None
        if operator == "+":
            output = num_1 + num_2
        elif operator == "-":
            output = num_1 - num_2
        elif operator == "/":
            output = num_1 / num_2
        elif operator == "*":
            output = num_1 * num_2
        else:
            await ctx.send("There was an invalid input")
            return
        await ctx.send("Answer: " + str(output))





bot.run(token)



