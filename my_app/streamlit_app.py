import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from pages.prediction import *


sns.set_theme(style="darkgrid")
sns.set()


# uploaded_file = st.file_uploader("Upload Image")

supernova_title = '<p style="font-family:sans-serif; color: white; font-size: 42px;">Supernova Classification</p>'
st.markdown(supernova_title, unsafe_allow_html=True)
#st.title("Supernova Classification")
st.markdown(""":collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision:""")
first_para = '''<p style="font-family:sans-serif; font-size: 18px; color: white; ">This project was created by 4 students
        from the Le Wagon Data Science Bootcamp.
        Our model's name is Sue, or Dr Susan Panova if you're nasty.
        Using Sue, we will be able to look at telescopic images
        of space to detect whether there is a supernova present or not.</p>'''
st.markdown(first_para, unsafe_allow_html=True)

second_para = '''<p style="font-family:sans-serif; color: white; font-size: 18px;">This is important for astronomers as supernovae are the largest
        explosion that humans know of. As a result, massive amounts of dark energy
        and matter are released. Dark energy and dark matter make up around 95% of
        the universe and still remain the biggest mystery of space.<p>'''
st.markdown(second_para, unsafe_allow_html=True)

# text over upload button "Upload Image"

main_bg = "/Users/Doug/code/celiapearson/supernova_group_project/my_app/pages/sn_2018gv-hubble.gif"

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
