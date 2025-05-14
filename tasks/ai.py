import asyncio
from logger import log

async def ai_task(queue):
    log.debug(f"starting ai task")
    while True:
        (priority, msg) = await queue.get()

        log.debug(f"recieved message '{msg}' with priority {priority}")

        # TODO pipe message to LLM instance

        queue.task_done()

        await asyncio.sleep(1)
