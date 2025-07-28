from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.brasilapi import router as brasilapi_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(brasilapi_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Brasil API FastAPI application!"}