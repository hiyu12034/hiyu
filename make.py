import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print("접속완료")

@client.event
async def on_message(message):
        if message.content.startswith("/파일"):
                pic = message.content.split(" ") [1]
                await message.channel.send(file=discord.File(pic))
import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print("접속완료")

@client.event
async def on_message(message):
        if message.content.startswith("/파일"):
                pic = message.content.split(" ") [1]
                await message.channel.send(file=discord.File(pic))
        if message.content.startswith("/파일"):
                pic = message.content.split(" ") [1]
                await message.channel.send(file=discord.File(pic))



client.run("NzMxMTc4OTkwNDMzMzM3MzY2.XwiRlg.sQiy_7NF6UrfJZaApSPbqAlpXnk")


client.run("NzMxMTc4OTkwNDMzMzM3MzY2.XwiRlg.sQiy_7NF6UrfJZaApSPbqAlpXnk")