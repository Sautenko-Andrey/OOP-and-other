import asyncio
import aiohttp
from aiohttp import ClientSession
from utils import page_status
from utils import async_timed

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls=[
            'https://kinogo.biz/45085-ne-ta-devushka.html',
            'https://football.ua/england.html',
            'https://www.atbmarket.com/product/kava-280-g-jacobs-monarch-rozcinna-sublimovana',
            'https://www.atbmarket.com/product/kapusta-1-gat',
            'https://www.atbmarket.com/product/cibula-ripcasta-1gat',
            'https://www.atbmarket.com/product/casnik-import-1-gat',
            'https://www.groceryapp.com/'
        ]
        requests=[page_status(session,url) for url in urls]
        results=await asyncio.gather(*requests, return_exceptions=True)

        exceptions=[res for res in results if isinstance(res,Exception)]
        succsessfu_results=[res for res in results if not isinstance(res,Exception)]

        print(f'Все результаты: {results}')
        print(f'Завершились успешно: {succsessfu_results}')
        print(f'Завершились с исключением: {exceptions}')

asyncio.run(main())