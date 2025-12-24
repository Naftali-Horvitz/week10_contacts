from fastapi import FastAPI
from data_interactor import *
import uvicorn


db_crud = DataInteractor()


app = FastAPI(title="Items API", version="1.0.0")

@app.get("/contacts")
async def all_contacts():
    return db_crud.get_all()

@app.post("/contacts")
async def create_contact(contact: Contact):
    return db_crud.add_contact(contact.model_dump())
        
@app.put("/contacts/{id}")
async def put_contact(id: int, contact: PutContact):
    return db_crud.update_contact(id, contact.model_dump())

    
@app.delete("/contacts/{id}")
async def delete_contact(id: int):
    return db_crud.del_contact(id)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)