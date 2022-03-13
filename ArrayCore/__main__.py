import asyncio

from pyrogram import idle

from . import Venom1
from . import call_py

async def startup():
    # STARTING CLIENTS
    if Venom1:
        try:
            await Venom.start()
            await Venom.join_chat("ArrayCore")
        except Exception as e:
            print(str(e))


    await vcbot.start()

    if call_py:
        await call_py.start()
    await idle()

loop = asyncio.get_event_loop()
if __name__ == "__main__":
    loop.run_until_complete(startup())
