from datetime import datetime

import discord

from objects import actions
from objects.Command import Command
from objects.Config import Config, Secret
from objects.actions import About

intents = discord.Intents.default()

client = discord.Client(intents=intents)
start = datetime.now()


config = Config()
secret = Secret()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):

    # The command issued via the inbound message
    command = None

    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    # Trigger #1
    elif message.content.startswith('!panko') and len(message.content) > 6:
        elements = message.content.split(' ')
        command = Command(elements[1])

    # Trigger #2
    elif message.content.startswith('$') and len(message.content) > 1:
        command_str = message.content[1:].strip()
        command = Command(command_str)

    # Let's go!!!
    if command is not None:

        # Where the message originated from
        if not hasattr(message.channel, 'guild'):
            source = message.channel
        else:
            source = message.channel.guild

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

client.run(secret.token)
