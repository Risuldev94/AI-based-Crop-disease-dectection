# backend/detector.py

import tensorflow as tf

from backend.utils.image_utils import preprocess_image
from backend.labels import CLASS_NAMES

model = tf.keras.models.load_model("backend/model/disease_model.h5")


def detect_disease(image_path):
    img = preprocess_image(image_path)

    predictions = model.predict(img)

    index = predictions.argmax()
    confidence = float(predictions.max())

    result = {
        "disease": CLASS_NAMES[index],
        "confidence": round(confidence * 100, 2)
    }

    return result
