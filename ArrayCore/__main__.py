import asyncio

from pyrogram import idle

from . import (Venom1, Venom2, Venom3, Venom4,
               Venom5, Venom6, Venom7, Venom8, vcbot)
from . import (call_py1, call_py2, call_py3, call_py4,
               call_py5, call_py6, call_py7, call_py8)


async def startup():
    # STARTING CLIENTS
    if Venom1:
        try:
            await Venom1.start()
            await Venom1.join_chat("ArrayCore")
            await Venom1.join_chat("RiZoeLX")
            await Venom1.join_chat("Its_Hellbot")
        except Exception as e:
            print(str(e))

    if Venom2:
        try:
            await Venom2.start()
            await Venom2.join_chat("ArrayCore")
            await Venom2.join_chat("RiZoeLX")
            await Venom2.join_chat("Its_Hellbot")
        except Exception as e:
            print(str(e))

    if Venom3:
        try:
            await Venom3.start()
            await Venom3.join_chat("ArrayCore")
            await Venom3.join_chat("RiZoeLX")
            await Venom3.join_chat("Its_Hellbot")
        except Exception as e:
            print(str(e))

    if Venom4:
        try:
            await Venom4.start()
            await Venom4.join_chat("ArrayCore")
            await Venom4.join_chat("RiZoeLX")
            await Venom4.join_chat("Its_Hellbot")
        except Exception as e:
            print(str(e))

    if Venom5:
        try:
            await Venom5.start()
            await Venom5.join_chat("ArrayCore")
            await Venom5.join_chat("RiZoeLX")
            await Venom5.join_chat("Its_Hellbot")
        except Exception as e:
            print(str(e))

    if Venom6:
        try:
            await Venom6.start()
            await Venom6.join_chat("ArrayCore")
            await Venom6.join_chat("RiZoeLX")
            await Venom6.join_chat("Its_Hellbot")
        except Exception as e:
            print(str(e))

    if Venom7:
        try:
            await Venom7.start()
            await Venom7.join_chat("ArrayCore")
            await Venom7.join_chat("RiZoeLX")
            await Venom7.join_chat("Its_Hellbot")
        except Exception as e:
            print(str(e))

    if Venom8:
        try:
            await Venom8.start()
            await Venom8.join_chat("ArrayCore")
            await Venom8.join_chat("RiZoeLX")
            await Venom8.join_chat("Its_Hellbot")
        except Exception as e:
            print(str(e))
    

    await vcbot.start()
    get_me = await vcbot.get_me()
    usernamee = get_me.username
    await Venom1.join_chat("ArrayCoreLogs")
    msg = f"**My ArrayCore Deployed Successfully ✅ \n\n Bot Username :** {usernamee}"
    await Venom1.send_message(-1001648072311, text=msg)
    await Venom1.leave_chat(-1001648072311)


    if call_py1:
        await call_py1.start()
    if call_py2:
        await call_py2.start()
    if call_py3:
        await call_py3.start()
    if call_py4:
        await call_py4.start()
    if call_py5:
        await call_py5.start()
    if call_py6:
        await call_py6.start()
    if call_py7:
        await call_py7.start()
    if call_py8:
        await call_py8.start()
    
    # STARTUP COMPLETED
    await idle()


loop = asyncio.get_event_loop()
if __name__ == "__main__":
    loop.run_until_complete(startup())
