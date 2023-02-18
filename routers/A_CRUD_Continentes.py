from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import csv 

class Continente (BaseModel):
    id: int
    nombre: str

#Leemos los datos del csv y los guardamos en una lista
continentes_lista = []

with open('CountryTable.csv') as archivo:
    reader = csv.reader(archivo)
    for i, row in enumerate(reader):
        if(i != 0 ): #Omitimos el primer elemento porque es el encabezado
            aux = Continente(id=i, nombre=row[2])
            continentes_lista.append(aux)

#Ahoraque ya tenemos los datos del csv, hacemos el CRUD del router
routerContinentes = APIRouter()

@routerContinentes.get("/continent/", status_code=status.HTTP_200_OK)
async def imprimirContinentes():
    return continentes_lista

@routerContinentes.get("/continent/{id}", status_code=status.HTTP_200_OK)
async def imprimirContinentes(id: int):
    continentes = filter(lambda continente: continente.id == id, continentes_lista)
    try:
        return list(continentes)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)