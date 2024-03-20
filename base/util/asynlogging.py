from queue import SimpleQueue
import asyncio
import logging
import logging.handlers

queue = SimpleQueue()
queue_handler = logging.handlers.QueueHandler(queue)
listener = logging.handlers.QueueListener(
    queue,
    logging.StreamHandler(),
    logging.FileHandler('app.log'),
)
logger = logging.getLogger('main')
logger.addHandler(queue_handler)

async def main():
    logger.info('App started')
    
    logger.info('App finished')

listener.start()
try:
    asyncio.run(main())
finally:
    listener.stop()