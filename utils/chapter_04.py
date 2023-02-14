from aiohttp import ClientSession

async def page_status(session:ClientSession,url:str):
    HEADERS = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'
    }
    async with session.get(url) as result:
        return result.status