from enum import Enum
from typing import List
from pydantic import BaseModel, ValidationError

class Fuel(str, Enum):
  PETROL = 'PETROL'
  DIESEL = 'DIESEL'
  LPG = 'LGP'

class Car(BaseModel):
  brand: str
  model: str
  year: int
  fuel: Fuel
  countries: List[str]
  note: str="No note"


car = Car(
  brand="Lancia",
  model="Musa",
  fuel="PETROL",
  year="2006",
  countries=["Italy", "France"]
)

print(car.json())
# try:
# invalid_car = Car(
#   brand="Lancia",
#   fuel="PETROL",
#   year="something",
#   countries=["Italy", "France"]
# )
# except ValidationError as e:
#    print(e)

# print(invalid_car.json())