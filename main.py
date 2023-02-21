from fastapi import FastAPI, HTTPException, status
from routers import A_CRUD_Continentes_SinRepetir

app = FastAPI()

app.include_router(A_CRUD_Continentes_SinRepetir.routerContinentes)

#hola