from fastapi import FastAPI, HTTPException, status
from routers import A_CRUD_Continentes, D_CRUD_PAIS

app = FastAPI()

app.include_router(A_CRUD_Continentes.routerContinentes)
app.include_router(D_CRUD_PAIS.routerPaises)