from fastapi import APIRouter
import httpx

router = APIRouter()


@router.get("/brazil/cep/{cep}")
async def get_address_by_cep(cep: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://brasilapi.com.br/api/cep/v1/{cep}")
        response.raise_for_status()
        return response.json()
    

@router.get("/brazil/moedas")
async def get_currency():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://brasilapi.com.br/api/cambio/v1/moedas")
        response.raise_for_status()
        return response.json()
    


@router.get("/brazil/trade")
async def get_trade(moeda: str, data: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://brasilapi.com.br/api/cambio/v1/cotacao/{moeda}/{data}")
        response.raise_for_status()
        return response.json()
    