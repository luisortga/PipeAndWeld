# Multi core

import time
import asyncio
import aiohttp

async def check_api(session: aiohttp.ClientSession, api: str) -> str:
    """
    Función asincrónica que verifica el estado de una API.
    """
    
    try:
        async with session.get(api) as response:
            if response.status == 200:
                return f'Successful {api} esta funcionando correctamente.'
            else:
                return f'Error: {api} respondió con el código de estado {response.status}.'
    except aiohttp.ClientError:
        return f'Error {api} no esta caído'

async def main():
    start = time.time()
    
    apis = [
        "https://api.github.com",
        "https://api.stackexchange.com",
        "https://api.twitter.com",
        "https://api.spotify.com",
        "https://api.openweathermap.org",
        "https://api.coinbase.com",
        "https://api.reddit.com",
        "https://api.nasa.gov",
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [check_api(session, api) for api in apis]
        
        result = await asyncio.gather(*tasks) # * desempaqueta la lista de tareas en argumentos separados para asyncio.gather
        for res in result:
                print(res)
    
    
    end = time.time()
    print(f"Tiempo total: {end - start} segundos")
    
if __name__ == "__main__":
    asyncio.run(main())