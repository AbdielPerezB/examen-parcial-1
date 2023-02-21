
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import csv

class Region (BaseModel):
    id: int 
    region: str
    continent: str

regionestotal_lista = []


with open('CountryTable.csv') as archivo:
    reader = csv.reader(archivo)
    for i, row in enumerate(reader):
        if(i !=0 ): #Omite el primer elemento porque es el encabezado
            #[0]=code, [1]=name, [2]=continent, [3]=region, [4]=surface_area, [5]=independence_year, [6]=population, 
            # [7]=life_expectancy, [8]gnp, [9]=gnp_old, [10]=local_name, [11]=government_form, [12]=head_of_state
            # [13]=capital, [14]=code2
            aux = Region(id=i, region = row[3], continent=row[2])
            regionestotal_lista.append(aux)

#CRUD-router
routerRegiones = APIRouter()

#Get:
@routerRegiones.get("/continent/region/",status_code=status.HTTP_200_OK)
async def regiones():
    return regionestotal_lista

#Get con Filtro Path
@routerRegiones.get("/continent/region/{_id}",status_code=status.HTTP_200_OK)
async def regiones(_id: int):
    regionestotal = filter(lambda region: region.id == _id, regionestotal_lista)
    try:
        return list(regionestotal)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


#Post (Create). 
@routerRegiones.post("/continent/region/", response_model= Region, status_code=status.HTTP_201_CREATED)
async def regiones(nuevaRegion:Region): 
    for aux in regionestotal_lista:
        if aux.id == nuevaRegion.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Esta region ya existe")
    else:
        regionestotal_lista.append(nuevaRegion)
        return nuevaRegion
'''
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

'''