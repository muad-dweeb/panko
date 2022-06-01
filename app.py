import discord
from discord import Emoji

from objects import Commands
from objects.Config import Config

intents = discord.Intents.default()

client = discord.Client(intents=intents)


config = Config()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith('!panko'):
        elements = message.content.split(' ')
        selection = elements[1]
        args = list()
        if len(elements) > 2:
            args = elements[2:]
        for command in Commands.AVAILABLE:
            if selection in command.tags:
                response = command().do(*args)
                if response.reaction is not None:
                    await message.add_reaction(response.reaction)
                if response.message is not None:
                    await message.channel.send(response.message)


client.run(config.token)