from app.blueprints.home import home
from flask import render_template, request, jsonify
import numpy as np
import os

# tf environment configuration
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1"

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..")
)
MODEL_PATH = os.path.join(
    project_root, "model", "CNN_final_model.keras"
)  # get model path

my_model = load_model(MODEL_PATH)  # load CNN model

CLASS_NAMES = {
    0: "rogowacenie słoneczne/choroba Bowena",
    1: "rak podstawnokomórkowy",
    2: "łagodne rogowacenia",
    3: "dermatofibroma",
    4: "czerniak",
    5: "znamię barwnikowe",
    6: "naczyniowa zmiana skórna",
}  # define class full names in polish


def model_predict(img_path, model):
    """
    loads the image and prepares it to be an input for my model,
    makes prediction of the model based on input image
    :param img_path: path to input image
    :param model: model to make the prediction
    :return: predictions
    """
    img = image.load_img(img_path, target_size=(128, 128))  # load image in desired size
    x = image.img_to_array(img)
    x = np.true_divide(x, 255.0)
    x = np.expand_dims(x, axis=0)
    preds = model.predict(x)
    return preds


@home.route("/", methods=["GET", "POST"])
@home.route("/predict/", methods=["POST"])
def home_page():
    if request.method == "POST":
        if "file" not in request.files:
            return jsonify({"error": "No file part"})

        file = request.files["file"]
        if file:
            file_path = os.path.join("/tmp", file.filename)
            file.save(file_path)  # save img temporarily

            preds = model_predict(file_path, my_model)  # predict
            os.remove(file_path)  # remove img

            # format predictions with class names and probabilities
            results = {CLASS_NAMES[i]: float(pred) for i, pred in enumerate(preds[0])}
            return jsonify({"prediction": results})

    return render_template("home/home.html")
