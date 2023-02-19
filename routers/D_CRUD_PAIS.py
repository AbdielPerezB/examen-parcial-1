from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import csv


class Paises (BaseModel):
    id: int
    nombre: str
    code: str


paissolo_lista = []  # guaradamos los datos del csv en una lista


with open('routers/CountryTable.csv') as archivo:
    reader = csv.reader(archivo)
    for i, row in enumerate(reader):
        if (i != 0):  # Imite el primer elemento porque es el encabezado
            aux = Paises(id=i, nombre=row[2], code=row[2])
            paissolo_lista.append(aux)

#CRUD-router
routerPaises = APIRouter()

#Get:
@routerPaises.get("/Paises/",status_code=status.HTTP_200_OK)
async def read():
    return paissolo_lista

#Get con Filtro Path
@routerPaises.get("/Paises/{id}",status_code=status.HTTP_200_OK)
async def read(id: int):#Esta variable tiene que ser la misma que en la línea 57
    paisessolo = filter(lambda pais: id.id == id, paissolo_lista)
    try:
        return list(paisessolo)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


#Post (Create). 
@routerPaises.post("/Paises/", response_model= Paises, status_code=status.HTTP_201_CREATED)
async def create(pais:Paises): 
    for aux in paissolo_lista:
        if aux.id == id.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Este pais ya existe")
    else:
       paissolo_lista.append(pais)
    return pais

#Put 
@routerPaises.put("/Paises/", response_model= Paises, status_code=status.HTTP_201_CREATED)
async def update(pais:Paises):
    found=False #Usamos bandera found para verificar si hemos encontrado lo solicitado
    for index, aux in enumerate(paissolo_lista):
        if aux.id == id.id: 
           paissolo_lista[index] = pais 
        found=True

    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return pais

#Delete  
@routerPaises.put("/Paises/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id:int):
    found=False #Usamos bandera found para verificar si hemos encontrado lo solicitado
    for index, aux in enumerate(paissolo_lista):
        if aux.id == id.id: 
            del paissolo_lista[index]
        found=True

    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)