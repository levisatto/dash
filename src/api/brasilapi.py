from fastapi import APIRouter
import httpx

router = APIRouter()

@router.get("/brazil/cities/{city_name}")
async def get_city_data(city_name: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://brasilapi.com.br/api/ibge/municipios/v1/{city_name}")
        response.raise_for_status()
        return response.json()

@router.get("/brazil/cep/{cep}")
async def get_address_by_cep(cep: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://brasilapi.com.br/api/cep/v1/{cep}")
        response.raise_for_status()
        return response.json()