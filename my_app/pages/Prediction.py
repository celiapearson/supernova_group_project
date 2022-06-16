import tensorflow as tf
import numpy as np
from PIL import Image
import os
import streamlit as st
import random
import base64

### STRUCTURE/BG ###

main_bg = "my_app/background_image3.jpg"

@st.cache(suppress_st_warning=True)
def load_image(path):
    with open(path, 'rb') as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    return encoded

@st.cache(suppress_st_warning=True)
def background_image_style(path):
    encoded = load_image(path)
    style = f'''
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover
    }}
    </style>
    '''
    return style

@st.cache(suppress_st_warning=True)
def write_bg(main_bg):
    st.write(background_image_style(main_bg), unsafe_allow_html=True)

write_bg(main_bg)


### CONTENT ###

prediction_title = '''<p style="font-family:Verdana; color: white; font-size: 42px;">
    Dr. Sue's Office 👩‍🚀 </p>'''
st.markdown(prediction_title, unsafe_allow_html=True)

pred_para_1 = '''<p style="font-family:Verdana; font-size: 18px; color: white; ">
    Hi there, welcome to my office! I'm
    Dr. Susan Panova, but you can just call me Sue.<p>'''
st.markdown(pred_para_1, unsafe_allow_html=True)

pred_para_2 = '''<p style="font-family:Verdana; font-size: 18px; color: white; ">
    I hear you've got some images you suspect <b>might</b> depict a supernova?
    Why don't you upload a few and I'll tell you if I think they are, and not
    to brag but I'll do it in a fraction of the time a human astronomer could!<p>'''
st.markdown(pred_para_2, unsafe_allow_html=True)

model = tf.keras.models.load_model('static/hs_model.h5')
uploaded_file = st.file_uploader("", "png")

if uploaded_file:

    image = Image.open(uploaded_file).convert('RGB')
    image_array  = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.image.resize(image_array, [51, 51])
    image = image / 255
    image = tf.expand_dims(image, axis = 0)
    result = model.predict(image)[0][0]

    supernova = ["Woohoo!! That's definitely a supernova, congrats!", "Yup, looks like a supernova to me", "Oh yeah, that's a big ol' supernova"]
    not_sure = ["This one's tricky, take a quick coffee break and we'll have another look!", "Probably best to consult an astronomer here...", "Could go either way... sorry"]
    not_supernova = ["Hmmm... I'm afraid this doesn't look like a supernova to me", "Nope! Not a supernova this time", "This doesn't look ANYTHING like a supernova - try again!"]

    if result >= 0.6:
        st.markdown(f""" ### Sue's prediction: Supernova :star2: ({round(float(result),4)}) — she says...
                    '{(random.choice(supernova))}'""")
        st.balloons()
    elif result <= 0.4:
        st.markdown(f""" ### Sue's prediction: Not a supernova :disappointed: ({round(float(result),4)}) — she says...
                    '{(random.choice(not_supernova))}'""")
    else:
        st.markdown(f""" ### Sue's prediction: Inconclusive :thinking_face: ({round(float(result),4)}) — she says...
                    '{(random.choice(not_sure))}'""")
