import discord
from discord.ext import commands
import botToken
from botFunctions import *


#I created a seperate file to hold the bot token since I don't want the token to go public
token = botToken.TOKEN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

client = discord.Client(intents=intents)

banned_phrases = ["stupid", "man chester united sucks", "ronaldo sucks", "messi is better", "france", "france is the best country", "dark souls 2 is good"]

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

@client.event
async def on_message(msg):
    if msg.author != client.user:
        if msg.content.lower().startswith("?hi"):
            await msg.channel.send(f"Hi, {msg.author.display_name}")
        else:


            for text in banned_phrases:
                if "crow" not in str(msg.author.roles) and text in str(msg.content.lower()):

                    if msg.content.startswith("stupid") or msg.content.startswith("france"):
                        await msg.delete()
                        await msg.channel.send("No swearing on my christian minecraft server")
                        return
                    else:
                        respond = (f"LIAR THAT SIMPLY ISN'T TRUE {msg.author.mention}")
                        await msg.channel.send(respond)
                        return
            print("Testing an shit")
            

            # if msg.content == '?crowme':
            #     member = msg.author
            #     role = get(member.server.roles, name="crow")
            #     await ctx.send("Giving admin role")
            #     await client.add_roles(member, role)
            #     await ctx.send("Admin role was given")




# @bot.command()
# async def calc(ctx):
#         def check(msg):
#             return len(msg.content) >= 1 and msg.author != bot.user

#         await ctx.send("Number 1: ")
#         num_1 = await bot.wait_for("message", check=check)
#         await ctx.send("Operator: ")
#         operator = await bot.wait_for("message", check=check)
#         await ctx.send("number 2: ")
#         num_2 = await bot.wait_for("message", check=check)
#         try:
#             num_1 = float(num_1.content)
#             operator = operator.content
#             num_2 = float(num_2.content)
#         except:
#             await ctx.send("There was an invalid input")
#             return
#         output = None
#         if operator == "+":
#             output = num_1 + num_2
#         elif operator == "-":
#             output = num_1 - num_2
#         elif operator == "/":
#             output = num_1 / num_2
#         elif operator == "*":
#             output = num_1 * num_2
#         else:
#             await ctx.send("There was an invalid input")
#             return
#         await ctx.send("Answer: " + str(output))





# bot.run(token)
client.run(token)



