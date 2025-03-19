import os
from config.config import Config

import aiohttp
import revolt
from revolt.ext import commands

class Client(commands.CommandsClient):
    async def get_prefix(self, message: revolt.Message):
        return Config.prefix 

async def main() -> None:
    async with aiohttp.ClientSession() as session:
        client = Client(session, Config.token)
            
        for filename in os.listdir('src/cogs'):
            if filename.endswith('.py'):
                try:
                    client.load_extension(f'cogs.{filename[:-3]}')
                except Exception as e:
                    print(f'Error: {e}')
        try:
            await client.start()
        except Exception as e:
            print(f'Error: {e}')