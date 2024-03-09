from discord.ext import commands
import discord

from typing import Any
import os
import logging
import tomllib

class Lauren(commands.AutoShardedBot):
    discord.utils.setup_logging(level=logging.INFO)
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("!"),
            intents=discord.Intents.all(),
        )
        self.logger = logging.getLogger("lauren")
        self.config: dict[Any, Any] = tomllib.load(open("./src/core/config.toml"))
        self.owner_ids: set[int] = set(self.config.get("owner_ids"))

    async def on_ready(self):
        self.logger.info("Lauren is ready!")
    
    async def _load_extensions(self) -> None:
        """Method for loading all extensions at once. Can be used in non-startup context"""
        for ext in os.listdir("src/cogs"):
            if ext.endswith(".py"):
                try:
                    await self.load_extension(f"cogs.{ext[:-3]}")
                    self.logger.info(f"Loaded {ext}")
                except commands.ExtensionFailed as e:
                    self.logger.warn(f"Failed loading {ext}")
    
    async def setup(self) -> None: 
        self.logger.info("Starting Lauren now...")

        await self._load_extensions()
        await self.start(self.config.get("token"))
