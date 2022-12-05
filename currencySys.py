import discord
from discord.ext import commands
import random
import pickle
import os
import botToken

token = botToken.TOKEN

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix="cash ",intents=discord.Intents.all())




    


dataFile = "data.json"

class Data():
    def __init__(self, wallet):
        self.wallet = wallet


    @client.event
    async def on_ready():
        print("Logged in as {0.user}".format(client))


    @client.command()
    async def work(message):
        memberData = loadMemberData(message.author.id)

        memberData.wallet += 1
        await message.channel.send("You went to virtual work now you made 1 (currency)")

        saveMemberData(message.author.id, memberData)

    @client.command()
    async def bal(message):
        memberData = loadMemberData(message.author.id)

        embedVar = discord.Embed(title="{member}'s Balance".format(member=message.author.display_name))
        embedVar.add_field(name="Wallet", value=str(memberData.wallet))
        await message.channel.send(embed=embedVar)

        
    def loadData():
        if os.path.isfile(dataFile):
            with open(dataFile, "rb") as file:
                return pickle.load(file)

        else:
            return dict()

    def loadMemberData(memberID):
        data = loadData()

        if memberID not in data:
            return Data(0,0)

        return data[memberID]

    def saveMemberData(memberID, memberData):
        data = loadData()

        data[memberID] = memberData

        with open(dataFile, "wb") as file:
            pickle.dump(data, file)





client.run(token)