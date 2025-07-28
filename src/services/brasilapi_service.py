import httpx

BASE_URL = "https://brasilapi.com.br/api/"

async def fetch_data(endpoint: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}{endpoint}")
        response.raise_for_status()
        return response.json()

async def get_cities():
    return await fetch_data("ibge/municipios/v1") 

async def get_states():
    return await fetch_data("ibge/estados/v1") 

async def get_zip_code_info(zip_code: str):
    return await fetch_data(f"cep/v1/{zip_code}") 