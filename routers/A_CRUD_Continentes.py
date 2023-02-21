from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import csv 

class Continente (BaseModel):
    id: int
    continente: str

continentes_lista=[
                Continente(id = 1, continente = "Asia"),
                Continente(id = 2, continente = "Europe"),
                Continente(id = 3, continente = "Africa"),
                Continente(id = 4, continente = "North America"),
                Continente(id = 5, continente = "Antarctica"),
                Continente(id = 6, continente = "Oceania")
                ]

################### Ahoraque ya tenemos los datos del csv, hacemos el CRUD del router ########################
routerContinentes = APIRouter()

#Get
@routerContinentes.get("/continent/", status_code=status.HTTP_200_OK)
async def continentes():
    return continentes_lista

@routerContinentes.get("/continent/{id}", status_code=status.HTTP_200_OK)
async def continentes(id: int):
    continentes = filter(lambda continente: continente.id == id, continentes_lista)
    try:
        return list(continentes)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

#Post
@routerContinentes.post("/continent/", response_model=Continente, status_code=status.HTTP_201_CREATED)
async def continentes(continente:Continente):
    for aux in continentes_lista:
        if aux.id == continente.id:  #Si el Id de los usuarios en la lista es igual al Id del usuario nuevo
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="El continente ya existe")
    else:
        continentes_lista.append(continente)
        return continente

#Put
@routerContinentes.put("/continent/", response_model=Continente, status_code=status.HTTP_201_CREATED)
async def continentes(continente: Continente):
    
    found=False
    
    for index, aux in enumerate(continentes_lista):
        if aux.id == continente.id:
           continentes_lista[index] = continente  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return continente
    
#Delete
@routerContinentes.delete("/continent/{id}", status_code=status.HTTP_204_NO_CONTENT)#El código 204 por naturaleza no devuelve nada, solo indica el éxito
async def continentes(id:int):
    
    found=False
    
    for index, aux in enumerate(continentes_lista):
        if aux.id ==id:
           del continentes_lista[index]
           found=True
       
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)