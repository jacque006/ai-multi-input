import asyncio
from logger import log
from priority import Priority
import pytchat

async def youtube_chat_task(queue, video_id):
    if not video_id:
        log.debug("no video id provided, skipping youtube chat task")
        return

    log.debug(f"starting youtube chat task for video {video_id}")

    chat = pytchat.create(video_id=video_id)
    while chat.is_alive():
        log.debug("checking chat messages")
        for c in chat.get().sync_items():
            msg = f"{c.datetime} [{c.author.name}]-{c.message} {c.amountString}"
            await queue.put((Priority.Normal, msg))

        await asyncio.sleep(1)

    try:
        chat.raise_for_status()
    except pytchat.ChatDataFinished:
        log.warning("YouTube chat data finished")
    except Exception as err:
        log.error(err)

    log.debug(f"ending youtube chat task for video {video_id}")
