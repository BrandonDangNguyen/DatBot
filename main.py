import discord
import random

TOKEN = ""

client = discord.Client()

common_words = ["nice", "wow", "...", "okay", "alright", "yeah"]

fun_words = ["lol", "lmao", "lolz", "lolzz,""lolzzz", "rofl", "lmafo", "\U0001F923"]

fun_replies = ["lol", "\U0001F923"]

h_r_u = ["how are you", "how r u", "hru", "how r you", "how are u"]


@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))


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
            return
        elif user_message.lower() == "hi dat bot":
            await message.channel.send(f"hi {username}!")
            return
        elif user_message.lower() == "bye dat bot":
            await message.channel.send(f"bye {username}")
            return
        elif user_message.lower() == "bye dat bot":
            await message.channel.send(f"bye {username}")
            return
        elif user_message.lower() == "@everyone":
            await message.channel.send("\U0001F621")
            return
        elif any(word in user_message.lower() for word in h_r_u):
            await message.channel.send("i'm doing pretty good")
            return
        elif any(word in user_message.lower() for word in fun_words):
            await message.channel.send(random.choice(fun_replies))
            return

        else:
            await message.channel.send(random.choice(common_words))
            return

    if user_message.lower() == "!hi":
        await message.channel.send(f"Hello {username}")
        return


client.run(TOKEN)

