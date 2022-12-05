import discord
from discord.ext import commands
import botToken


#I created a seperate file to hold the bot token since I don't want the token to go public
token = botToken.TOKEN

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

banned_phrases = ["stupid", "man chester united sucks", "ronaldo sucks", 
                  "messi is better", "france", "dark souls 2 is good", "innit", "spoon"]

annoying_phrases = ["no you", "no u", "nou"]



@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

@client.event
async def on_message(msg):
    #Prevents infinite loop of bot messaging itself
    if msg.author != client.user:

        #Messages anyone who's sentance starts with hi
        if msg.content.lower().startswith("hi"):
            await msg.channel.send(f"Hi, {msg.author.display_name}")

        #If any says the phrase give me admin
        #The bot gives them the admin role
        elif msg.content == "give me admin":
            member = msg.author
            role = discord.utils.get(member.guild.roles, name="Admin")
            await member.add_roles(role)

        else:

            # If anyone says a word or sentance from the banned phrases dictionary 
            # The bot deletes the message and may respond
            for text in banned_phrases:
                #IF they don't have the crow role and they say a banned phrasae
                if "crow" not in str(msg.author.roles) and text in str(msg.content.lower()):
                    # For stupid and france specifically it will delete your sentance
                    # And respond with a message
                    if msg.content.startswith("stupid") or msg.content.startswith("france"):
                        await msg.delete()
                        await msg.channel.send("No swearing on my christian minecraft server")
                        return
                    else:
                        # If someone says any of the other banned phrases
                        # They will be messaged and mentioned 
                        respond = (f"LIAR THAT SIMPLY ISN'T TRUE {msg.author.mention}")
                        await msg.channel.send(respond)
                        return

            # Message for me to see if client is ran
            print("On message command has been ran")

            # Goes through annoying phrases 
            for phrase in annoying_phrases:
                if phrase in str(msg.content.lower()):
                    # messages and @'s if anyone says nou
                    if msg.content.startswith("nou"):
                        await msg.channel.send(f"Nobody says that {msg.author.mention}")
                        return
                    else:
                        #Messages and @'s for the other annoying phrases
                        response = (f"No u {msg.author.mention}")
                        await msg.channel.send(response)
                        return

#Handles events for people who join the server
@client.event
async def on_member_join(member):
    # Message for me to see if client is ran
    print("Somebody joined")
    
    #If someone joins the server the bot gives welocme message
    channel = member.guild.system_channel
    await channel.send(f'Welcome new kid{member.mention}!')
    
    #Gives the user the crow role
    role = discord.utils.get(member.guild.roles, name="crow")
    await member.add_roles(role)

    #Gives them a nickname of their name + Bird at the end
    await member.edit(nick=f"{member.name} Bird")




#Allows the bot to go online and function
# bot.run(token)
client.run(token)



