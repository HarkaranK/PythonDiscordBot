import discord
from discord.ext import commands
import botToken
from botFunctions import *


#I created a seperate file to hold the bot token since I don't want the token to go public
token = botToken.TOKEN

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
# bot = commands.Bot(command_prefix='>', intents=intents)

client = discord.Client(intents=intents)
# client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

banned_phrases = ["stupid", "man chester united sucks", "ronaldo sucks", 
                  "messi is better", "france", "dark souls 2 is good"]

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

@client.event
async def on_message(msg):
    if msg.author != client.user:
        if msg.content.lower().startswith("?hi"):
            await msg.channel.send(f"Hi, {msg.author.display_name}")

        elif msg.content == "give me admin":
            member = msg.author
            role = discord.utils.get(member.guild.roles, name="Admin")
            await member.add_roles(role)

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


@client.event
async def on_member_join(member):
    print("Somebody joined")
    channel = member.guild.system_channel
    await channel.send(f'Welcome new kid{member.mention}!')
    
    role = discord.utils.get(member.guild.roles, name="crow")
    await member.add_roles(role)

    await member.edit(nick=f"{member.name} Bird")





# bot.run(token)
client.run(token)



