from fastapi import FastAPI
from enum import Enum
app= FastAPI()

class AvailableCuisines(str, Enum):
    indian="indian"
    italian="italian"

food_items = {
    'indian' : ["rajma", "chaval"],
    'italian' : ["pizza", "pasta"]
}

@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine)

coupon_code={
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/get_coupon/{code}")
async def get_items(code: int):
    return {'dicount percentage': coupon_code.get(code)}
