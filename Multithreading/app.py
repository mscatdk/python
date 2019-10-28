from concurrent.futures import ThreadPoolExecutor
import threading
import random
import logging
import logging.config
import time

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

logger = logging.getLogger('app')

def when_finished(_fut):
    logger.info("Result: %s", _fut.result())

def task(msg):
    logger.info("Starting task...")
    for i in range(10):
        logger.info(msg)
        time.sleep(1)


def main():
    executor = ThreadPoolExecutor(max_workers=3)
    task1 = executor.submit(task, "ping")
    task2 = executor.submit(task, "pong")
    task1.add_done_callback(when_finished)
    task2.add_done_callback(when_finished)
    logger.info("Waiting for threads to complete...")

if __name__ == '__main__':
    main()