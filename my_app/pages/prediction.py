import tensorflow as tf
import numpy as np
from PIL import Image
import os
import streamlit as st

# command = streamlit run my_app/streamlit_app.py from the root of the directory
model = tf.keras.models.load_model('static/DenseNet121.h5')

uploaded_file = st.file_uploader("Upload Image", "gif")

if uploaded_file:

    image = Image.open(uploaded_file) #.convert('RGB')
    image_array  = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.image.resize(image_array, (51, 51))
    image = image / 255
    image = tf.expand_dims(image, axis = 0)
    result = model.predict(image)[0][0]

#supernova = ["Woohoo!! That's definitely a supernova, congrats!", "Yup, looks like a supernova to me", "Oh yeah, that's a big ol' supernova"]
#not_supernova = ["Hmmm... I'm afraid this doesn't look like a supernova to me", "Nope! Not a supernova this time", "This doesn't look ANYTHING like a supernova - try again!"]

    # if result >= 0.5:
    #     f"Sue's prediction {result}: '{(random.choice(not_supernova))}'"
    # else:
    #     f"Sue's prediction {result}: '{(random.choice(supernova))}'"

    st.markdown(result)


# def predictor(img_path):

#     img = tf.keras.preprocessing.image.load_img(img_path, target_size=(51,51,1), color_mode='grayscale')

#     img = tf.keras.preprocessing.image.img_to_array(img)

#     img = np.expand_dims(img,axis = 0)

#     prediction = model.predict(img)

#     return prediction[0][0]

# if uploaded_file is not None:

#     #if save_uploaded_file(uploaded_file):

#     # display the image

#     display_image = Image.open(uploaded_file)

#     st.image(display_image)

#     prediction = predictor(os.path.join('../static/images',uploaded_file.name))


#     os.remove('../static/images/'+uploaded_file.name)

#     # deleting uploaded saved picture after prediction

#     # drawing graphs

#     st.text(f'Prediction: {prediction}')
