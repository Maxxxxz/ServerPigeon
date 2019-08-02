import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import secret
import wakeonlan
import os

path_to_script = os.path.dirname(os.path.abspath(__file__))
logfile = os.path.join(path_to_script, "log\\pigeonlog.log")
print("Logfile located at: " + logfile)

client = commands.Bot(command_prefix='spc@')

prefix = 'spc@'

STORMOFF = False    #for keeping pc locked during a storm
LOCKED = False      #for keeping pc locked from potential abuse
#load STORMOFF and LOCKED vars from file to avoid bad time

def log(info):
    print(info)
    with open(logfile, "a+") as f:
        f.write(info + "\n")
         # import os
         # print(os.path.dirname(os.path.abspath("pigeonlog.txt")))
    print("saved")
    # save info to file

@client.event
async def on_ready():
    print('Logged in as ')
    print(client.user.name)
    print(client.user.id)
    print('-----')

def getStormStatus():
    return STORMOFF

def getLockStatus():
    return LOCKED

@client.event
async def on_message(message):
    author = message.author
    if message.author == client.user:
        return                  #return if auther is self
    if message.guild == None:
        lMsg = "{0.created_at}: {0.author} sent DM containing this text: ".format(message) + message.content
        log(lMsg)
        return                  #return if DM
    storm = getStormStatus()
    lock = getLockStatus()

    lMsg = "{0.created_at}: {0.author} did a command that does not exist: {0.content}".format(message)

    #also wrap up in elifs for speedier execution
        #this will require reworking START/STOP server commands
    #also check if message.author.id is in secret.users
    if message.content.startswith(prefix):
        message.content = message.content[4:]
        msgID = str(message.author.id)

        if msgID in secret.admins and message.content.startswith("LOCK"):
            lock = True
            msg = '{0.author.mention} Has locked the Server PC. Only an admin can unlock it.'.format(message)
            await message.channel.send(msg)
            lMsg = "{0.created_at}: {0.author} locked the server pc".format(message)

        if msgID in secret.admins and message.content.startswith("UNLOCK"):
            lock = False
            storm = False
            msg = '{0.author.mention} Has unlocked the Server PC. Users can now use commands.'.format(message)
            await message.channel.send(msg)
            lMsg = "{0.created_at}: {0.author} unlocked the server pc".format(message)

        if msgID in secret.admins and message.content.startswith('STORMOFF'):     #power off PC only admins
            storm = True
            msg = '{0.author.mention} Powered Server PC off. Only an admin can power it back on.'.format(message)
            #turn off server PC
            await message.channel.send(msg)
            lMsg = "{0.created_at}: {0.author} turned server pc off via STORMOFF".format(message)

        if message.content.startswith('POWERON'):
            if (not storm or not lock) or msgID in secret.admins:     #power on server pc if not storm OR if admin turns on
                wakeonlan.send_magic_packet(secret.macAdd)
                storm = False
                msg = '{0.author.mention} Powered Server PC on.'.format(message)
                await message.channel.send(msg)
                lMsg = "{0.author} turned on the server pc".format(message)
            else:
                msg = 'Server PC can only be turned on by and admin right now.'
                await message.channel.send(msg)
                lMsg = "{0.created_at}: {0.author} attempted to turn on PC, but was blocked by lock/stormoff".format(message)

        if not lock and message.content.startswith('POWEROFF'):
            msg = '{0.author.mention} Powered Server PC off (no work yet).'.format(message)
            #do server shutdown command here| sudo halt
            await message.channel.send(msg)

            lMsg = "{0.created_at}: {0.author} turned off server pc".format(message)

        if message.content.startswith('GETGAMES'):
            msg = "list of supported games will go here"
            await message.channel.send(msg)
            lMsg = "{0.created_at}: {0.author} got the list of games".format(message)

        if not lock and not storm:
            if message.content.startswith('STARTSERVER'):
                message.content = message.content[11:]
                if message.content in secret.games:
                    log(message.author + "started server: " + message.content)
                    msg = '{0.author.mention} Started server for {0.content}.'.format(message)
                    await message.channel.send(msg)
                    lMsg = "{0.created_at}: {0.author} started server for {0.content}".format(message)
                else:
                    msg = 'Server for {0.content} does not exist.'.format(message)
                    await message.channel.send(msg)
                    lMsg = "{0.created_at}: {0.author} tried to start non-existant server {0.content}".format(message)

            if message.content.startswith('STOPSERVER'):
                message.content = message.content[11:]
                if message.content in secret.games:
                    log(message.author + "stopped server: " + message.content)
                    msg = '{0.author.mention} Stopped server for {0.content}.'.format(message)
                    await message.channel.send(msg)
                    lMsg = "{0.created_at}: {0.author} stopped server for {0.content}".format(message)
                else:
                    msg = 'Server for {0.content} does not exist.'.format(message)
                    await message.channel.send(msg)
                    lMsg = "{0.created_at}: {0.author} tried to stop non-existant server {0.content}".format(message)


        if message.content.startswith('USAGEINFO'):
            msg = "usage info will go here"
            await message.channel.send(msg)
            lMsg = "{0.created_at}: {0.author} used Usage Info".format(message)

        if message.content.startswith('help') or message.content.startswith('Help'):
            msg = """\
            ```md
# Server Pigeon Commands:
# spc@POWERON         ->      Powers on the remote PC
# spc@POWEROFF        ->      Powers off the remote PC
# spc@STORMOFF        ->      Powers off the remote PC allowing only admins to restart
# spc@GETGAMES        ->      Lists all games servers are available for
# spc@STARTSERVER %   ->      Starts the server for game name %
# spc@STOPSERVER %    ->      Stops the server for game name %
# spc@USAGEINFO       ->      Displays current system usage info```
"""
            await message.channel.send(msg)
            lMsg = "{0.created_at}: {0.author} used Help".format(message)

        log(lMsg)

client.run(secret.secret)