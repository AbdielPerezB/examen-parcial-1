from fastapi import FastAPI, HTTPException, status

from routers import A_CRUD_Continentes_SinRepetir, Africa, Antarctica, asia, Europe, North_America, Oceania, Regiones
from pydantic import BaseModel

app = FastAPI()

app.include_router(asia.routerRegiones)
app.include_router(North_America.routerRegiones)
app.include_router(Africa.routerRegiones)
app.include_router(Antarctica.routerRegiones)
app.include_router(Oceania.routerRegiones)
app.include_router(Europe.routerRegiones)
app.include_router(Regiones.routerRegiones)