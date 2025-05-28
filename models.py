import pydantic
from pydantic import BaseModel

class Content(BaseModel):
    satid: int
    satname: str
    transactionscount: int

class Response(BaseModel):
    info: Content
    tle: str
        
