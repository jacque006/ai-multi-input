#!/usr/bin/python3

import asyncio
from enum import Enum
import logging

log = logging.getLogger(__name__)

class Priority(Enum):
    HIGH = 0
    NORMAL = 1
    LOW = 2

async def processMessageWorker(name, queue):
    log.debug(f"starting {name}")
    while True:
        (priority, msg) = await queue.get()

        log.debug(f"worker {name} recieved message '{msg}' with priority {priority}")

        queue.task_done()

        await asyncio.sleep(1)

async def createMessageWorker(name, queue):
    log.debug(f"starting {name}")
    while True:
        await asyncio.sleep(5)

        if queue.empty():
            msg = 'Did you get that thing I sent ya?'
            priority = Priority.LOW
            await queue.put((priority, msg))
            log.info(f"worker {name} created message '{msg}' with priority {priority}")

async def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    log.info("running")

    queue = asyncio.PriorityQueue()
    tasks = []

    log.debug("starting tasks")

    processMsgTask = asyncio.create_task(processMessageWorker('process-msg-worker', queue))
    createMsgTask = asyncio.create_task(createMessageWorker('create-msg-worker', queue))
    tasks.extend([processMsgTask, createMsgTask])

    await asyncio.sleep(1)

    await asyncio.gather(*tasks, return_exceptions=True)

    log.info('done')

if __name__ == "__main__":
    asyncio.run(main())