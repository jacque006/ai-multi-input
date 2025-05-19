import asyncio
from logger import log
from priority import Priority
from pynput import keyboard

# TODO Record full voice input from mic
# - Holding space starts primary mic record
# - Releasing space end recording and sends
async def voice_input_task(queue):
    log.debug("starting voice input task")

    loop = asyncio.get_event_loop()

    def handle_press(key):
        if key != keyboard.Key.space:
            return

        # TODO Get voice input
        msg = 'Hear the power of my voice!'

        # https://stackoverflow.com/a/64659149
        loop.call_soon_threadsafe(queue.put_nowait, (Priority.HIGH, msg))

    keyboard.Listener(on_press=handle_press).start()

    while True:
        await asyncio.sleep(1)
