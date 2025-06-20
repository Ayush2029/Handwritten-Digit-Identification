from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
import tensorflow as tf
import io
import os

app = FastAPI(title="MNIST Digit Recognition API - New Logic")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
try:
    model_path = "model.h5"
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}. Please ensure 'model.h5' is in the correct directory.")
    model = tf.keras.models.load_model(model_path)
    print("TensorFlow model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None 

@app.get("/")
async def root():
    return {"message": "Welcome to the MNIST Digit Recognition API (New Logic)"}
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    if model is None:
        return JSONResponse(status_code=500, content={"error": "Model not loaded. Please check server logs."})
    try:
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("L").resize((28, 28))
        img_array = np.array(image).astype("float32") / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)
        prediction = model.predict(img_array)
        digit = int(np.argmax(prediction))
        return {"digit": digit}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Prediction failed: {str(e)}"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("digit_api:app", host="127.0.0.1", port=8000, reload=True)