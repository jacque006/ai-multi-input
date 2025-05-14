import asyncio
import keyboard
from logger import log
from priority import Priority

async def voice_input_task(queue):
    log.debug(f"starting voice input task")
    while True:
        await asyncio.sleep(1)

        try:
            if keyboard.is_pressed('space'):
                # TODO Get voice input
                msg = 'Hear the power of my voice!'
                priority = Priority.HIGH
                await queue.put((priority, msg))
                log.debug(f"sending voice input '{msg}'")
        except:
            # ignore other key presses
            pass
