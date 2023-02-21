from fastapi import FastAPI, HTTPException, status
from routers import E_CRUD_Paises
import csv
from pydantic import BaseModel

app = FastAPI()

app.include_router(E_CRUD_Paises.routerPaises)