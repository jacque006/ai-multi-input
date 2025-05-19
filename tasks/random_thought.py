import asyncio
from logger import log
from priority import Priority

async def random_thought_task(queue):
    log.debug("starting random thought task")
    while True:
        await asyncio.sleep(10)

        if queue.empty():
            # TODO Get random thought from a list or somewhere else
            msg = 'Did you get that thing I sent ya?'
            await queue.put((Priority.LOW, msg))
