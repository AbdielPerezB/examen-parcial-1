
#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, status
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel
            
class Region (BaseModel):
    Id: int
    Region:str

regiones_lista=[
                Region(Id = 1, Region = "Antarctica"),
                Region(Id = 2, Region = "Central Africa"),
                Region(Id = 3, Region = "Eastern Africa"),
                Region(Id = 4, Region = "Western Africa"),
                Region(Id = 5, Region = "Southern Africa"),
                Region(Id = 6, Region = "Northern Africa"),
                Region(Id = 7, Region = "Middle East"),
                Region(Id = 8, Region = "Southern and Central Asia"),
                Region(Id = 9, Region = "Southeast Asia"),
                Region(Id = 10, Region = "Eastern Asia"),
                Region(Id = 11, Region = "Southern Europe"),
                Region(Id = 12, Region = "Western Europe"),
                Region(Id = 13, Region = "Eastern Europe"),
                Region(Id = 14, Region = "Nordic Countries"),
                Region(Id = 15, Region = "Baltic Countries"),
                Region(Id = 16, Region = "British Islands"),
                Region(Id = 17, Region = "Caribbean"),
                Region(Id = 18, Region = "North America"),
                Region(Id = 19, Region = "Central America"),
                Region(Id = 20, Region = "Australia and New Zealand"),
                Region(Id = 21, Region = "Polynesia"),
                Region(Id = 22, Region = "Melanesia"),
                Region(Id = 23, Region = "Micronesia"),
                Region(Id = 24, Region = "Micronesia/Caribbean")
                ]

routerRegiones = APIRouter()

#Función Get:
@routerRegiones.get("/continent/region/",status_code=status.HTTP_200_OK)
async def regiones():
    return regiones_lista

@routerRegiones.get("/continent/region/{id}", status_code=status.HTTP_200_OK)
async def regiones(id: int):
    region = filter(lambda regiones: regiones.Id == id, regiones_lista)
    try:
        return list(region)[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    
#Función Post (Create). Es decir, crea un nuevo usuario. Implementamos también el código de respuesta
@routerRegiones.post("/continent/region/", response_model=Region, status_code=status.HTTP_201_CREATED)
async def regiones(region:Region):
    
    for saved_regiones in regiones_lista:
        if saved_regiones.Id == region.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="La region ya existe")
    else:
        regiones_lista.append(region)
        return region

#***Put (update). Es decir, de un usuario que YA EXISTE, lo va a modificar
@routerRegiones.put("/continent/region/", response_model=Region, status_code=status.HTTP_201_CREATED)
async def regiones(region:Region):
    
    found=False
    
    for index, saved_regiones in enumerate(regiones_lista):
        if saved_regiones.Id == region.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           regiones_lista[index] = region  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return region

#***Delete
@routerRegiones.delete("/continent/region/{id}", status_code=status.HTTP_204_NO_CONTENT) #Aquí no es necesario poner todo el usuario, con el id basta para eoncontrarlo y eliminarlo
async def regiones(id:int):
    
    found=False
    
    for index, saved_regiones in enumerate(regiones_lista):
        if saved_regiones.Id == id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del regiones_lista[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           #El código 204 por naturaleza no devuelve nada, solo indica el éxito
       
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        
    