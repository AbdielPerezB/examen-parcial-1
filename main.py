from fastapi import FastAPI, HTTPException, status
from routers import Regiones
import csv
from pydantic import BaseModel

app = FastAPI()

app.include_router(Regiones.routerRegiones)
