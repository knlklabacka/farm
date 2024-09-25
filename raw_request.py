import shutil

from fastapi import FastAPI, Request, Header, UploadFile, File, Form, HTTPException
from pydantic import BaseModel
from starlette import status

app = FastAPI()


class InsertCar(BaseModel):
    brand: str
    model: str
    year: int


@app.get("/")
async def raw_request(request: Request):
    return {
        "message": request.base_url,
        "all": dir(request)
    }


@app.get("/headers")
async def read_headers(user_agent: str | None = Header(None)):
    return {"User-Agent": user_agent}


@app.post("/upload")
async def upload(file: UploadFile = File(...), brand: str = Form(...), model: str = Form(...)):
    with open("saved_file.png", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "brand": brand,
        "model": model,
        "file_name": file.filename,
    }


@app.post("/carsmodel")
async def new_car_model(car: InsertCar):
    if car.year > 2022:
        raise HTTPException(
            status.HTTP_406_NOT_ACCEPTABLE,
            detail="The car doesn't exist yet!"
        )
    return {
        "message": car
    }
