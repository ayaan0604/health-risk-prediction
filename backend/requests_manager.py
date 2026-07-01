from pydantic import BaseModel, Field
from enum import Enum
from typing import Annotated


class Gender(str, Enum):
    male = "male"
    female = "female"

class Prediction_Request(BaseModel):
    age : Annotated[int, Field(..., gt=0, lt=120, description="Age of the person")]
    smoke: Annotated[bool, Field(..., description="is the person a smoker?")]
    active: Annotated[bool, Field(..., description="is the person physically active")]
    alco: Annotated[bool, Field(..., description="does the person drink alchohol")]
    gender : Annotated[Gender, Field(..., description="Can be male / female")]
    water_intake : Annotated[int, Field(..., gt=0, lt=15, description="daily water intake (liters)")]
    caloric_food : Annotated[bool, Field(..., description="Does the person consume high calory food regularly?")]
    meals : Annotated[int, Field(..., gt=0, lt=6, description="Number of meals taken in a day (0 to 5)")]
    height_cm : Annotated[int, Field(..., gt=0, description="Height of the person (in centimeters)")]
    weight : Annotated[int, Field(..., gt=0, description="weight of the person in kgs")]

    def to_input_features(self):
        height_meters = self.height_cm/100
        bmi = self.weight/(height_meters ** 2)

        data = {
            "age" : self.age,
            "bmi" : round(bmi,2),
            "active" : int(self.active),
            "alco" : int(self.alco),
            "male" : int(self.gender == Gender.male),
            "female" : int(self.gender == Gender.female),
            "water_intake" : self.water_intake,
            "caloric_food" : int(self.caloric_food),
            "meals" : self.meals,
            "smoke" : int(self.smoke)
        }

        return data
