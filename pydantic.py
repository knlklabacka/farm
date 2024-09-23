from enum import Enum
from typing import List
from pydantic import BaseModel, ValidationError


invalid_car = Car(
  brand="Lancia",
  fuel="PETROL",
  year="something",
  countries=["Italy", "France"]
)

print(invalid_car.json())