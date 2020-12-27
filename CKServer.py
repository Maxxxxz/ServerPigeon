import discord
from discord.ext import commands
from discord.ext.commands import Bot, Cog

import apiRequests

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

    # Perhaps use psutil?
    @commands.command(name="usage")
    async def _usageInfo(self, ctx):
        apiRequests.doPost()

        emb=discord.Embed(title="Server Pigeon", description="Usage information", color=0x0000ff)
        emb.set_author(name="Server Pigeon", url="https://github.com/Maxxxxz")
        emb.add_field(name="server 1", value="usage", inline=True)
        emb.add_field(name="server 2", value="usage", inline=True)
        emb.add_field(name="Pigeon PC", value="usage", inline=True)
        emb.set_footer(text="Created by Maxxxxz")

        await ctx.send(embed=emb)

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

    #############################################################
    # General

    @commands.command(name="help")
    async def _help(self, ctx):
        emb=discord.Embed(title="", description="Commands for Server Pigeon", color=0x0000ff)
        emb.set_author(name="Server Pigeon", url="https://github.com/Maxxxxz")
        # emb.set_thumbnail(url="")
        emb.add_field(name=self.bot.command_prefix + "help", value="Displays this message", inline=False)
        emb.add_field(name=self.bot.command_prefix + "power {on/off}", value="Powers the remote PC on or off (omit for status)", inline=False)
        emb.add_field(name=self.bot.command_prefix + "locked", value="Shows the locked status of the remote PC", inline=False)
        emb.add_field(name=self.bot.command_prefix + "lock", value="Locks the remote PC commands to admins only", inline=False)
        emb.add_field(name=self.bot.command_prefix + "unlock", value="Unlocks the remote PC commands to admins only", inline=False)
        emb.add_field(name=self.bot.command_prefix + "usage", value="Shows the usage information for both the server PC and Server Pigeon's home.", inline=False)
        emb.set_footer(text="Created by Maxxxxz")

        await ctx.send(embed=emb)

    #############################################################

def setup(bot):
    bot.add_cog(CKServer(bot))
