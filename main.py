#!/usr/bin/python3

import asyncio
from logger import init, log
from tasks.ai import ai_task
from tasks.random_thought import random_thought_task
from tasks.voice_input import voice_input_task
from tasks.youtube_chat import youtube_chat_task

async def main():
    init()
    log.info("running")

    queue = asyncio.PriorityQueue()
    tasks = []

    log.debug("starting tasks")

    tasks.append(asyncio.create_task(ai_task(queue)))
    tasks.append(asyncio.create_task(random_thought_task(queue)))
    tasks.append(asyncio.create_task(voice_input_task(queue)))
    tasks.append(asyncio.create_task(youtube_chat_task(queue)))

    await asyncio.sleep(1)

    await asyncio.gather(*tasks, return_exceptions=True)

    log.info('done')

if __name__ == "__main__":
    asyncio.run(main())
