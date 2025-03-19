import time
from revolt.ext import commands


class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx: commands.Context):
        start_time = time.time()
        msg = None
        try:
            msg = await ctx.send('Pong!')
            end_time = time.time()
            latency = round((end_time - start_time) * 1000)
            await msg.edit(content=f'Pong! :ping_pong: **{latency}**ms')
        except Exception as e:
            print(f'Error: {e}')

def setup(client) -> None:
    try:
        client.add_cog(Utilities(client))
    except Exception as e:
        print(f'Error: {e}')
