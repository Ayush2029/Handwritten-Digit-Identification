# Handwritten-Digit-Identification

This project is a full-stack application for recognizing handwritten digits using the MNIST dataset. It consists of a trained CNN model, a FastAPI backend for inference, and a frontend HTML page for users to draw or upload digits for prediction. <br>

<h4>Features: </h4>
- Convolutional Neural Network (CNN) trained on MNIST <br>
- FastAPI backend for digit prediction via file upload <br>
- Responsive frontend with drawing pad and image upload <br>
- Confusion matrix, accuracy curves, and loss graphs in notebook <br>
- Fully local and offline-capable <br>

<h3> Installation </h3>
Make sure you have Python 3.8 or higher installed.<br>
1] Clone the repository: <br>
Run this in terminal: <br>
git clone https://github.com/Ayush2029/Handwritten-Digit-Identification.git <br>
cd Handwritten-Digit-Identification <br>
2] Install dependencies: <br>
Run this: <br>
pip install -r requirements.txt <br>

<h3>Train the Model</h3>
The project already contains a pre-trained model saved as model.h5. If you want to retrain the model:<br>
1] Open the MNIST.ipynb file using Jupyter Notebook: <br>
jupyter notebook MNIST.ipynb <br>
2] Run all cells. It will train the model and save it as model.h5 in the same folder as with digit_api.py.<br>

<h3>Run the API Server </h3>
Make sure model.h5 is present in the same directory as digit_api.py.<br>
Run this command in the terminal:<br>
uvicorn digit_api:app --reload <br>
<br>
Your FastAPI backend will start at:<br>
http://127.0.0.1:8000<br>

<h3>Use the Frontend</h3>
1] Open frontend.html in any modern web browser (e.g., Chrome).<br>
2] Draw a digit on the canvas or upload an image of a digit. <br>
3] Click on "Predict".<br>
4] The result will appear below. <br>
Note: Make sure the FastAPI backend is running before using the frontend page. The frontend sends predictions to: http://127.0.0.1:8000/predict/ <br>
