from typing import Dict

from fastapi import FastAPI, Path, Body

app = FastAPI()


@app.get("/cars/price")
async def cars_by_price(min_price: int = 0, max_price: int = 10000):
    return {"Message": f"Listing cars with prices between {min_price} and {max_price}"}


@app.post("/cars")
async def new_car(data: Dict = Body(...)):
    print(data)
    return {"message": data}
