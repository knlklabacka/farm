from typing import Dict
from pydantic import BaseModel
from fastapi import FastAPI, Path, Body

app = FastAPI()


class InsertCar(BaseModel):
    brand: str
    model: str
    year: int


class InsertUser(BaseModel):
    username: str
    name: str


@app.get("/cars/price")
async def cars_by_price(min_price: int = 0, max_price: int = 10000):
    return {"Message": f"Listing cars with prices between {min_price} and {max_price}"}


@app.post("/cars")
async def new_car(car: InsertCar, user: InsertUser, code: int=Body(None)):
    return {"car": car, "user": user, "code": code}
