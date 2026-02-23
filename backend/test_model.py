import tensorflow as tf
import numpy as np
import cv2

model = tf.keras.models.load_model("model/disease_model.h5")

img = cv2.imread("sample_leaf.jpg")  # put one test image here
img = cv2.resize(img, (224,224))
img = img / 255.0
img = np.expand_dims(img, axis=0)

prediction = model.predict(img)

print("Predicted class index:", prediction.argmax())
print("Confidence:", prediction.max())
