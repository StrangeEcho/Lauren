from discord.ext import commands
from core.bot import Lauren

import discord

class General(commands.Cog):
    def __init__(self, bot: Lauren):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Shows Lauren's WebSocket Protocol latency"""
        embed = discord.Embed(
            description="🏓 Pong!",
            color=discord.Color.green()
        )
        for shard, latency in self.bot.latencies:
            embed.add_field(
                name=f"Shard {shard}",
                value=f"Latency: `{round(latency * 1000)}ms`"
            )
        await ctx.send(embed=embed)
    
    @commands.command()
    async def say(self, ctx: commands.Context, *, msg: str):
        "Make Lauren say something"
        await ctx.send(msg)

async def setup(bot: Lauren):
    await bot.add_cog(General(bot))