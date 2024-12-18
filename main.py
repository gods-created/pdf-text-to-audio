import asyncio
from loguru import logger
from os.path import exists 
from minions import (
    get_text_from_pdf,
    create_mp3_record
)

async def main(file_path: str) -> None:
    if not exists(file_path):
        logger.error('File not found')
        return
    
    text = get_text_from_pdf(file_path)
    if not text:
        logger.error('No text data in file')
        return
    
    # logger.debug(text)

    response = create_mp3_record(text)
    logger.debug(response)

    return

if __name__ == '__main__':
    try:
        file_path = input('File path: ')

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(
            main(
                file_path
            )
        )
        loop.close()

    except (KeyboardInterrupt, Exception, ) as e:
        logger.error(str(e))