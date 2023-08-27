import uvicorn
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()


class Place(BaseModel):
    name: str
    description: Optional[str] = None
    coffee: bool
    wifi: bool
    food: bool
    lat: float
    lng: float

    class Config:
        # orm_mode = True
        from_attributes = True


@app.post('/places/')
async def create_place_view(place: Place):
    return place


@app.get('/')
async def root():
    return {'mes': 'Hello World!'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
