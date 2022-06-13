import tensorflow as tf
import numpy as np
from PIL import Image
import os
import streamlit as st

st.write(os.getcwd())

model = tf.keras.models.load_model('../static/model5.h5')

uploaded_file = st.file_uploader("Upload Image", 'gif')

#image = Image
# if uploaded_file:

#     image = Image.open(uploaded_file) #.convert('RGB')
#     #image_array  = tf.keras.preprocessing.image.img_to_array(image)
#     image = tf.image.resize(image, (51,51,1))
#     image = image / 255
#     # image = tf.expand_dims(image, axis = 0)

#     result = model.predict(image)

#     st.write(result)


def predictor(img_path):

    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(51,51,1), color_mode='grayscale')

    img = tf.keras.preprocessing.image.img_to_array(img)

    img = np.expand_dims(img,axis = 0)

    prediction = model.predict(img)

    return prediction[0][0]

if uploaded_file is not None:

    #if save_uploaded_file(uploaded_file):

    # display the image

    display_image = Image.open(uploaded_file)

    st.image(display_image)

    prediction = predictor(os.path.join('../static/images',uploaded_file.name))

    os.remove('../static/images/'+uploaded_file.name)

    # deleting uploaded saved picture after prediction

    # drawing graphs

    st.text(f'Prediction: {prediction}')
