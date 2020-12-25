import discord
from discord.ext import commands
from discord.ext.commands import Bot

# Cog for all CKServer commands
class CKServer(commands.Cogs):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def 