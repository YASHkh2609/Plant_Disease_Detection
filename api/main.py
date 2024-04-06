# from fastapi import FastAPI, File, UploadFile
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
# import requests
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://127.0.0.1:3001",  # Adjusted the origin URL
# ]

# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["GET", "POST"],  # Allow the required HTTP methods
#     allow_headers=["*"],
# )

# endpoint= "http://localhost:8601/v1/models/disease_model:predict"

# CLASS_NAMES = ["Early Blight", "Late Blight","Healthy"]

# @app.get("/ping")
# async def  ping():
#     return "Hello, I'm alive!"

# def read_file_as_image(data) -> np.ndarray:
#     return Image.open(BytesIO(data))

# @app.post("/predict")
# async def predict(
#     file: UploadFile= File(...)
# ):
#     image= read_file_as_image(await file.read())
#     img_batch=np.expand_dims(image, 0)

#     json_data={
#         "instances":img_batch.tolist()
#     }

#     response = requests.post(endpoint, json=json_data)
#     prediction= np.array(response.json()["predictions"][0])

#     predicted_class=CLASS_NAMES[np.argmax(prediction)]
#     conf = np.max(prediction)
#     return{
#         'class': predicted_class,
#         'confidence': float(conf)
#     }

# if __name__== "__main__":
#     uvicorn.run(app, host='localhost', port=8000)
from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware to allow all origins, methods, and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

endpoint = "http://localhost:8601/v1/models/disease_model:predict"
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

@app.get("/ping")
async def ping():
    return "Hello, I'm alive!"

def read_file_as_image(data) -> np.ndarray:
    return Image.open(BytesIO(data))

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    json_data = {"instances": img_batch.tolist()}

    response = requests.post(endpoint, json=json_data)
    prediction = np.array(response.json()["predictions"][0])

    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    conf = np.max(prediction)
    return {
        'class': predicted_class,
        'confidence': float(conf)
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
