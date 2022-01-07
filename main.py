import discord
import os

from discord.ext import commands
from discord.ext.commands import bot
from dotenv import load_dotenv
from neuralintents import GenericAssistant
import nltk
nltk.download("omw-1.4")

chatbot = GenericAssistant("intents.json")
chatbot.train_model()
chatbot.save_model()

client = discord.Client()

load_dotenv()
TOKEN = os.getenv("OTI1MDg5ODMyMjQwMjgzNzE5.YcoDCw.AffDTUvhwXCLtjbyekw6HGYe3Vg")


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")
    if message.author == client.user:
        return

    if message.content.startswith("#Dat"):
        response = chatbot.request(message.content[5:])
        await message.channel.send(response)





client.run("OTI1MDg5ODMyMjQwMjgzNzE5.YcoDCw.AffDTUvhwXCLtjbyekw6HGYe3Vg")

