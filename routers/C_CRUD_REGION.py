
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import csv

class RegionesTOTAL (BaseModel):
    id: int 
    nombre: str
    continent: str
    region: str

regionestotal_lista = []  #guaradamos los datos del csv en una lista


with open('CountryTable.csv') as archivo:
    reader = csv.reader(archivo)
    for i, row in enumerate(reader):
        if(i !=0 ): #Imite el primer elemento porque es el encabezado
            aux = RegionesTOTAL(id=i, nombre=row[2], continent=row[3])
            regionestotal_lista.append(aux)

#CRUD-router
routerRegiones = APIRouter()

#Get:
@routerRegiones.get("/regionestotal/",status_code=status.HTTP_200_OK)
async def read():
    return regionestotal_lista

#Get con Filtro Path
@routerRegiones.get("/regionestotal/{id}",status_code=status.HTTP_200_OK)
async def read(id: int):#Esta variable tiene que ser la misma que en la línea 57
    regionestotal = filter(lambda region: id.id == id, regionestotal_lista)
    try:
        return list(regionestotal)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


#Post (Create). 
@routerRegiones.post("/regionestotal/", response_model= RegionesTOTAL, status_code=status.HTTP_201_CREATED)
async def create(regiontotal:RegionesTOTAL): 
    for aux in regionestotal_lista:
        if aux.id == id.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Esta region ya existe")
    else:
        regionestotal_lista.append(regiontotal)
        return regiontotal

#Put 
@routerRegiones.put("/regionestotal/", response_model= RegionesTOTAL, status_code=status.HTTP_201_CREATED)
async def update(regiontotal:RegionesTOTAL):
    found=False #Usamos bandera found para verificar si hemos encontrado lo solicitado
    for index, aux in enumerate(regionestotal_lista):
        if aux.id == id.id: 
        regionestotal_lista[index] = regiontotal 
        found=True

    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return regiontotal

#Delete  
@routerRegiones.put("/regionestotal/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id:int):
    found=False #Usamos bandera found para verificar si hemos encontrado lo solicitado
    for index, aux in enumerate(regionestotal_lista):
        if aux.id == id.id: 
        del regionestotal_lista[index]
        found=True

    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

