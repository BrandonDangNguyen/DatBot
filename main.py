import discord
import random

TOKEN = "OTI1MDg5ODMyMjQwMjgzNzE5.YcoDCw.WwF8QCCsEjJQcLMVEJ-tag9blg4"

client = discord.Client()

@client.event
async def on_ready():
    print("we have logged in as {0.user}". format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return

    if message.channel.name == "general":
        if user_message.lower() == "hello":
            await message.channel.send(f"Hello {username}")
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f"See you later {username}!")

    if user_message.lower() == "!hi":
        await message.channel.send(f"Hello {username}")
        return
client.run(TOKEN)


