import tensorflow as tf
import numpy as np
from PIL import Image
import os
import streamlit as st
import random

# command = streamlit run my_app/streamlit_app.py from the root of the directory

prediction_title = '''<p style="font-family:sans-serif; color: white; font-size: 42px;">Dr. Sue's Office 👩‍🚀 </p>'''
st.markdown(prediction_title, unsafe_allow_html=True)

st.markdown(""":collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision:""" )

pred_para_1 = '''<p style="font-family:sans-serif; font-size: 18px; color: white; ">Hi there, welcome to my office! I'm
        Dr. Susan Panova, but you can just call me Sue.<p>'''
st.markdown(pred_para_1, unsafe_allow_html=True)

pred_para_2 = '''<p style="font-family:sans-serif; font-size: 18px; color: white; ">I hear you've got some images you suspect
*might* depict a supernova? Why don't you upload a few and I'll tell you if I think they are, and I'll do it in
a fraction of the time a human astronomer could!<p>'''
st.markdown(pred_para_2, unsafe_allow_html=True)

model = tf.keras.models.load_model('static/hs_model.h5')

print(model.summary())

uploaded_file = st.file_uploader("", "png")

if uploaded_file:

    image = Image.open(uploaded_file).convert('RGB')
    image_array  = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.image.resize(image_array, [51, 51])
    image = image / 255
    image = tf.expand_dims(image, axis = 0)
    result = model.predict(image)[0][0]

    supernova = ["Woohoo!! That's definitely a supernova, congrats!", "Yup, looks like a supernova to me", "Oh yeah, that's a big ol' supernova"]
    not_supernova = ["Hmmm... I'm afraid this doesn't look like a supernova to me", "Nope! Not a supernova this time", "This doesn't look ANYTHING like a supernova - try again!"]

    if result >= 0.5:
        st.markdown(f"Sue's prediction {round(result,4)}: '{(random.choice(not_supernova))}'")
    else:
        st.markdown(f"Sue's prediction {round(result,4)}: '{(random.choice(supernova))}'")

    #st.write(image)

main_bg = "my_app/pages/sn_2018gv-hubble.gif"

import base64

@st.cache
def load_image(path):
    with open(path, 'rb') as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    return encoded

def background_image_style(path):
    encoded = load_image(path)
    style = f'''
    <style>
    .stApp {{
        background-image: url("data:image/gif;base64,{encoded}");
        background-size: cover; opacity: 1
    }}
    </style>
    '''
    return style

st.write(background_image_style(main_bg), unsafe_allow_html=True)



    #st.markdown(result)


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
