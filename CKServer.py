import discord
from discord.ext import commands
from discord.ext.commands import Bot, Cog

# Cog for all CKServer commands
class CKCog(Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.bot.load_extension()

    #############################################################
    # General Service related commands

    @commands.command(name="showservices")
    async def _showServices(self, ctx, arg):
        await ctx.send(arg)

    @commands.command(name="startservice")
    async def _startService(self, ctx, arg):
        await ctx.send("Starting Service: {}".format(arg))

    @commands.command(name="stopservice")
    async def _stopService(self, ctx, arg):
        await ctx.send("Stopping Service: {}".format(arg))

    #############################################################

    #############################################################
    # Server PC Commands



    #############################################################
    
    #############################################################
    # Administrative

    @commands.command(name="power")
    async def _powercmd(self, ctx, arg:str=None):
        if arg is not None:
            if arg.lower() == "on":
                await ctx.send("Power on...")
            elif arg.lower() == "off":
                await ctx.send("Power off...")
            else:
                await ctx.send("Usage: {}power {{off/on}}. Omit status to see current status.".format(self.bot.command_prefix))
        else:
            # format once bot is its own class.
            await ctx.send("Server pc is {}".format("off/on"))

    @commands.command(name="locked")
    async def _lockstatus(self, ctx):
        await ctx.send("Is server locked: {}")#.format(self.bot.isLocked))

    @commands.command(name="lock")
    async def _lock(self, ctx):
        # Check here if user in admins
        await ctx.send("Locked Server.")
    
    @commands.command(name="unlock")
    async def _unlock(self, ctx):
        # Check here if user in admins
        await ctx.send("Unlocked Server.")

    #############################################################

def setup(bot):
    bot.add_cog(CKServer(bot))
