from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import csv


class Paise (BaseModel):
    id: int
    nombre: str
    region: str


paises_lista = []


with open('CountryTable.csv') as archivo:
    reader = csv.reader(archivo)
    for i, row in enumerate(reader):
        if (i != 0):  # Imite el primer elemento porque es el encabezado
            aux = Paise(id=i, nombre=row[1], region=row[3])
            paises_lista.append(aux)

#CRUD-router
routerPaises = APIRouter()

#Get con Filtro Path
@routerPaises.get("/{_region}/",status_code=status.HTTP_200_OK)
async def read(_region: str):
    paisessolo = filter(lambda pais:  pais.region == _region, paises_lista)
    try:
        return list(paisessolo)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
'''
@routerPaises.get("/{_region}/{id}",status_code=status.HTTP_200_OK)
async def read(_region: str):
    paises_por_region = filter(lambda paises:  paises.region == _region, paises_lista)
    pais_por_id = filter(lambda pais: pais.id == id, list(paises_por_region))
    try:
        return list(pais_por_id)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
'''
'''
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
        '''