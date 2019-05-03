import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import secret


client = commands.Bot(command_prefix='spc@')

random = 0

prefix = 'spc@'


@client.event
async def on_ready():
    print('Logged in as ')
    print(client.user.name)
    print(client.user.id)
    print('-----')


@client.event
async def on_message(message):
    author = message.author
    if message.author == client.user:
        return                  #return if auther is self
    if message.guild == None:
        return                  #return if DM, definitely don't want these to be used by everyone


    if message.content.startswith(prefix):
        message.content = message.content[4:]
        if message.content.startswith('POWERON'):
            msg = '{0.author.mention} Powered Server PC on (no work yet)'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('POWEROFF'):
            msg = '{0.author.mention} Powered Server PC off (no work yet)'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('love') or message.content.startswith('Love'):
            msg = 'Love, love, love. :purple_heart: to {0.author.mention}'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('help') or message.content.startswith('Help'):
            msg = """\
            ```
Server Pigeon Commands:
spc@POWERON         ->      Powers on the remote PC
spc@POWEROFF        ->      Powers off the remote PC
spc@STORMOFF        ->      Powers off the remote PC allowing only admins to restart
spc@GETGAMES        ->      Lists all games servers are available for
spc@STARTSERVER #   ->      Starts the server for game name #
spc@STOPSERVER #    ->      Stops the server for game name #
spc@USAGEINFO       ->      Displays current system usage info
            ```\
            """
            await message.channel.send(msg)


client.run(secret.secret)