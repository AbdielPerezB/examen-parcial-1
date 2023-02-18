from fastapi import FastAPI, HTTPException, status
from routers import A_CRUD_Continentes

app = FastAPI()

app.include_router(A_CRUD_Continentes.routerContinentes)