from core.bot import Lauren
import asyncio

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    asyncio.run(Lauren().setup())