import discord
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix='spc@')

prefix = 'spc@'

STORMOFF = False    #for keeping pc locked during a storm
LOCKED = False      #for keeping pc locked from potential abuse
#load STORMOFF and LOCKED vars from file to avoid bad time

client.run(secret.secret)