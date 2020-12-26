import discord
from discord.ext import commands
from discord.ext.commands import Bot

# Cog for all CKServer commands
class CKServer(commands.Cogs):
    def __init__(self, bot):
        self.bot = bot

    # def setup(bot):
    #     self.bot.add_cog(CKServer(bot))

    @commands.command(name="showservices")
    async def _showservices(ctx, arg):
        await ctx.send(arg)