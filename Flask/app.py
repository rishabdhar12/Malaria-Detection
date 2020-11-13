from __future__ import division, print_function
import sys
import glob
import os
import numpy as np
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import preprocess_input

app = Flask(__name__)

model = load_model('final_model.h5')


def model_predict(image_path, model):
    img = image.load_img(image_path, target_size=(224,224))
    
    x = image.img_to_array(img)
    x = x/255
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    
    predictions = model.predict(x)
    predictions = np.argmax(predictions, axis=1)
    if predictions == 0:
        print('Infected')
    else:
        print('Not Infected')
        
    return predictions


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        
        predictions = model.predict(file_path, model)
        result = predictions
        return result
    return None

if __name__ == '__main__':
    app.run(debug=True)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    