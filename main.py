from fastapi import FastAPI, HTTPException, status
from routers import A_CRUD_Continentes_SinRepetir, Africa, Antarctica, asia, Europe, North_America, Oceania
from pydantic import BaseModel

app = FastAPI()

