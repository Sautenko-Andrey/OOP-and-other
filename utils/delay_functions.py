import asyncio

async def delay(sleeping_time:int):
    print(f'Я засыпаю на {sleeping_time} секунд...')
    await asyncio.sleep(sleeping_time)
    print(f'Сон в течении {sleeping_time} секунд закончился!')
    return sleeping_time

