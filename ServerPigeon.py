import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import wakeonlan
import os

import load
from CKServer import *

path_to_script = os.path.dirname(os.path.abspath(__file__))
logfile = os.path.join(path_to_script, "log\\pigeonlog.log")
print("Logfile located at: " + logfile)

prefix = 'spc@'

client = commands.Bot(command_prefix=prefix, help_command=None)

# client.load_extension('.CKServer')
client.add_cog(CKCog(client))

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

#             await message.channel.send(msg)
#             lMsg = "{0.created_at}: {0.author} used Help".format(message)
#         log(lMsg)

load.load()

client.run(load.TOKEN)