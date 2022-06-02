from datetime import datetime

import discord

from objects import actions
from objects.Command import Command
from objects.Config import Config
from objects.actions import About

intents = discord.Intents.default()

client = discord.Client(intents=intents)
start = datetime.now()


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

    # Let's go!!!
    elif message.content.startswith('!panko'):

        # Where the message originated from
        if not hasattr(message.channel, 'guild'):
            source = message.channel
        else:
            source = message.channel.guild

        # The message input text
        elements = message.content.split(' ')
        command = Command(elements[1])

        # Divergent, one-off logic = bad :(
        if command.action == 'about':
            response = About(source).do(uptime=datetime.now() - start,
                                        guild_count=len(client.guilds))
            await message.channel.send(embed=response.message)
            return

        # Find the appropriate action and do it
        for action in actions.AVAILABLE:
            if command.action == action.tag:
                response = action(source).do(*command.args)
                if response.reaction is not None:
                    await message.add_reaction(response.reaction)
                if response.message is not None:
                    await message.channel.send(embed=response.message)


client.run(config.token)
