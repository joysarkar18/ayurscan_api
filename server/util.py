import numpy as np
import tensorflow as tf
from keras.applications.vgg19 import preprocess_input, decode_predictions
import matplotlib.pyplot as plt

def process_image(path):
    img = tf.keras.utils.load_img(path, target_size=(256,256))
    i = tf.keras.utils.img_to_array(img)
    ims = preprocess_input(i)
    imgs = np.expand_dims(ims, axis=0)
    return imgs
    

def classify(path):
    img = process_image(path)


if __name__ == "__main__":
    process_image("E:\\My Projects\\Plant Detection\data\\Syzygium Jambos (Rose Apple)\\SJ-S-029.jpg")