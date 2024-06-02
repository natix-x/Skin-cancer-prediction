from app.blueprints.home import home
from flask import render_template
from tensorflow.keras.models import load_model
from keras.preprocessing import image
from flask import request, jsonify
import numpy as np
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
MODEL_PATH = os.path.join(project_root, 'model', 'CNN_final_model.keras')  # get model path

my_model = load_model(MODEL_PATH)  # load CNN model

CLASS_NAMES = {
    0: "actinic keratoses or Bowen's disease",
    1: "basal cell carcinoma",
    2: "benign keratosis-like lesions",
    3: 'dermatofibroma',
    4: 'melanoma',
    5: 'malanocytic nevi',
    6: 'vascular lesion'
}  # define class names


def model_predict(img_path, model):
    """
    makes prediction of the model based on input image
    :param img_path: path to input image
    :param model: model to make the prediction
    :return: predictions
    """
    img = image.load_img(img_path, target_size=(128, 128))  # load image in desired size
    x = image.img_to_array(img)
    x = x / 255.
    preds = model.predict(x)
    return preds


@home.route("/", methods=["GET", "POST"])
@home.route("/predict/", methods=["GET", "POST"])
def home_page():
    if request.method == 'POST':
        if 'file' not in request.files:  # check if an image file posted
            return jsonify({"error": "No file part"})

        file = request.files['file']

        if file:
            file_path = os.path.join("/tmp", file.filename)
            file.save(file_path)

            preds = model_predict(file_path, my_model)

            os.remove(file_path)
            pred_class = np.argmax(preds, axis=-1)[0]
            pred_class_name = CLASS_NAMES[pred_class]  # get the class name

            return jsonify({"prediction": pred_class_name})
    return render_template("home/home.html")
