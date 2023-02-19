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

################### Ahoraque ya tenemos los datos del csv, hacemos el CRUD del router ########################
routerContinentes = APIRouter()

#Get
@routerContinentes.get("/continent/", status_code=status.HTTP_200_OK)
async def read():
    return continentes_lista

@routerContinentes.get("/continent/{id}", status_code=status.HTTP_200_OK)
async def read(id: int):
    continentes = filter(lambda continente: continente.id == id, continentes_lista)
    try:
        return list(continentes)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

#Post
@routerContinentes.post("/continent/", response_model=Continente, status_code=status.HTTP_201_CREATED)
async def create(continente:Continente):
    for aux in continentes_lista:
        if aux.id == continente.id:  #Si el Id de los usuarios en la lista es igual al Id del usuario nuevo
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="El continente ya existe")
    else:
        continentes_lista.append(continente)
        return continente

#Put
@routerContinentes.put("/continent/", response_model=Continente, status_code=status.HTTP_201_CREATED)
async def update(continente: Continente):
    
    found=False
    
    for index, saved in enumerate(continentes_lista):
        if saved.id == continente.id:
           continentes_lista[index] = continente  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return continente