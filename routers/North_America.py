
#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, status
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel
import csv
            
class Regiones (BaseModel):
    Id: int
    Region:str

regiones_lista=[
                Regiones(Id = 1, Region = "Caribbean"),
                Regiones(Id = 2, Region = "North America"),
                Regiones(Id = 3, Region = "Central America"),
                ]

routerRegiones = APIRouter()

 
    #code,name,continent,region,surface_area,independence_year,population,life_expectancy,
#gnp,gnp_old,local_name,government_form,head_of_state,capital,code2

#Función Get:
@routerRegiones.get("/north_america/",status_code=status.HTTP_200_OK)
async def north_america():
    return regiones_lista

@routerRegiones.get("/north_america/{id}", status_code=status.HTTP_200_OK)
async def north_america(id: int):
    region = filter(lambda regiones: regiones.Id == id, regiones_lista)
    try:
        return list(region)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    
#Función Post (Create). Es decir, crea un nuevo usuario. Implementamos también el código de respuesta
@routerRegiones.post("/north_america/", response_model=Regiones, status_code=status.HTTP_201_CREATED)
async def north_america(region:Regiones):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for saved_regiones in regiones_lista:
        if saved_regiones.Id == region.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="La region ya existe")
    else:
        regiones_lista.append(region)
        return region
    
    #http://127.0.0.1:8000/usersclass/

    #***Put (update). Es decir, de un usuario que YA EXISTE, lo va a modificar
@routerRegiones.put("/north_america/", response_model=Regiones, status_code=status.HTTP_201_CREATED)
async def north_america(region:Regiones):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_regiones in enumerate(regiones_lista):
        if saved_regiones.Id == region.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           regiones_lista[index] = region  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        #return {"error":"No se ha actualizado el usuario"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return region
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@routerRegiones.delete("/north_america/{id}", status_code=status.HTTP_204_NO_CONTENT) #Aquí no es necesario poner todo el usuario, con el id basta para eoncontrarlo y eliminarlo
async def north_america(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_regiones in enumerate(regiones_lista):
        if saved_regiones.Id == id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del regiones_lista[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           #El código 204 por naturaleza no devuelve nada, solo indica el éxito
       
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        
    
