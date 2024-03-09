from discord.ext import commands
from core.bot import Lauren
import discord

class Base(commands.Cog):
    def __init__(self, bot: Lauren):
        self.bot = bot
    
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx: commands.Context, *cogs: str): 
        """Method for loading cog/extensions. Seperate by spaces"""
        for cog in cogs:
            if not cog.startswith("cogs."):
                cog = f"cogs.{cog}"
            try:
                await self.bot.load_extension(cog)
                await ctx.send("👌")
            except commands.ExtensionError as e:
                await ctx.send(f"Loading failed | {e}")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, *cogs: str): 
        """Method for reloading cog/extensions. Seperate by spaces"""
        for cog in cogs:
            if not cog.startswith("cogs."):
                cog = f"cogs.{cog}"
            try:
                await self.bot.reload_extension(cog)
                await ctx.send("👌")
            except commands.ExtensionError as e:
                await ctx.send(f"Loading failed | {e}")

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx: commands.Context, *cogs: str): 
        """Method for unloading cog/extensions. Seperate by spaces"""
        for cog in cogs:
            if not cog.startswith("cogs."):
                cog = f"cogs.{cog}"
            try:
                await self.bot.unload_extension(cog)
                await ctx.send("👌")
            except commands.ExtensionError as e:
                await ctx.send(f"Unloading failed | {e}")

async def setup(bot: Lauren):
    await bot.add_cog(Base(bot))