import tensorflow as tf

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from tensorflow.keras import preprocessing
from PIL import Image


import numpy as np

MODEL = tf.keras.models.load_model('UAVvaste_model.h5')

app = FastAPI()


@app.get('/')
async def index():
    return {"Message": "This is Index"}


@app.post("/predictimage")
async def UploadImage(file: bytes = File(...)):
    with open('image.jpg','wb') as image:
        image.write(file)
        image = Image.open("./image.jpg") 

        test_image = image.resize((180,180))
        test_image = preprocessing.image.img_to_array(test_image)
        test_image = test_image / 255.0
        test_image = np.expand_dims(test_image, axis=0)

        class_names = {0 : 'background', 1 :'litter'}    
        predictions = MODEL.predict(test_image)
        scores = tf.nn.softmax(predictions[0])
        scores = scores.numpy()
        image.close()
    
    return f"{class_names[np.argmax(scores)]} with a { (100 *       np.max(scores)).round(2) } % confidence."