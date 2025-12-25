from pydantic import BaseModel
from typing import Optional
class Contact(BaseModel):
    first_name: str
    last_name: str
    phone_number: str

class PutContact(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None