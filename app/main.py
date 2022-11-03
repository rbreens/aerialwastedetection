import tensorflow as tf

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

import numpy as np

MODEL = tf.keras.models.load_model('UAVvaste_model.h5')

app = FastAPI()


@app.get('/')
async def index():
    return {"Message": "This is Index"}


