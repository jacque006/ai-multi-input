import asyncio
from logger import log

async def youtube_chat_task(queue):
    log.debug("starting youtube chat task")
    while True:
        # TODO Read from Youtube chat

        await asyncio.sleep(1)
