import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
import os
import asyncio

default_settings = {"AUTODEL": True}

class DM:
    """DM a user."""

    def __init__(self, bot):
        self.bot = bot
        self.settings = fileIO("data/DM/settings.json", "load")
    
    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def dmSet(self, ctx, choice : str=None):
        """Sets whether or not to delete the comand when it is typed
            
            Options:
            off - turns off deleting
            on - turns on deleting"""
        options = {"off": False, "on": True}
        server = ctx.message.server
        if choice.lower() not in options:
            await send_cmd_help(ctx)
            return
        else:
            self.settings[server.id]["AUTODEL"] = options[choice.lower()]
            fileIO("data/welcome/settings.json", "save", self.settings)
    

    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def dm(self, ctx, user : discord.Member, format_msg):
        """DM a user."""
        channel = ctx.message.channel
        await self.bot.send_message(user, format_msg)
        await self.bot.purge_from(channel, limit=1)

def check_folders():
    if not os.path.exists("data/DM"):
        print("Creating data/welcome folder...")
        os.makedirs("data/DM")

def check_files():
    f = "data/DM/settings.json"
    if not fileIO(f, "check"):
        print("Creating welcome settings.json...")
        fileIO(f, "save", {})
    else: #consistency check
        current = fileIO(f, "load")
        for k,v in current.items():
            if v.keys() != default_settings.keys():
                for key in default_settings.keys():
                    if key not in v.keys():
                        current[k][key] = default_settings[key]
                        print("Adding " + str(key) + " field to welcome settings.json")
        fileIO(f, "save", current)


def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(DM(bot))

