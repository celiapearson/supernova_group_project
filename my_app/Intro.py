import streamlit as st
from pages.Prediction import *
import base64

main_bg = "my_app/background_image3.jpg"

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
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover
    }}
    </style>
    '''
    return style

st.write(background_image_style(main_bg), unsafe_allow_html=True)


### CONTENT ###

supernova_title = '''<p style="font-family:Verdana; color: white; font-size: 42px;">
    Identifying Supernovas using Deep Learning ⭐💥</p>'''
st.markdown(supernova_title, unsafe_allow_html=True)

first_para = '''<p style="font-family:Verdana; font-size: 18px; color: white">
    Supernovas (or supernovae) are likely to hold the keys to humankind's
    understanding of dark energy - a mysterious force that forms 95% of the
    universe's total energy and appears to be immune to gravitational forces.</p>'''
st.markdown(first_para, unsafe_allow_html=True)

first_para2 = '''<p style="font-family:Verdana; font-size: 18px; color: white">
    This means that the study of supernovas could ultimately lead us to knowing
    the fate of the universe... and even the meaning of life itself.....<br><hr></p>'''
st.markdown(first_para2, unsafe_allow_html=True)

sue_header = '''<p style="font-family:Verdana; color: white; font-size: 28px;">
    The Model (aka Sue)</p>'''
st.markdown(sue_header, unsafe_allow_html=True)

second_para = '''<p style="font-family:Verdana; color: white; font-size: 18px">
    Our Deep Learning model's name is Sue (or Dr. Susan Panova, to use her legal
    name), and she was trained on over 180,000 telescopic images extraterrestrial
    artifacts, and as a result can succesfully identify which images depict
    supernovas!<p>'''
st.markdown(second_para, unsafe_allow_html=True)

third_para = '''<p style="font-family:Verdana; color: white; font-size: 18px">
    Click below to proceed to Sue's office and see what she
    thinks of our images...<p>'''

st.markdown(third_para, unsafe_allow_html=True)

st.write(f'''
    <a target="_self" href="http://localhost:8501/Prediction">
        <button>
            to Dr. Panova's Office
        </button>
    </a>
    ''',
    unsafe_allow_html=True
)

fourth_para = '''<p style="font-family:Verdana; color: white; font-size: 14px">
    <hr>This project was created by students of the Le Wagon Data Science Bootcamp
    in London.<p>'''
st.markdown(fourth_para, unsafe_allow_html=True)

fifth_para = '''<p style="font-family:Verdana; color: white; font-size: 14px">
    Special thanks to: Mark, Luke, Kenza and Ollie<p>'''
st.markdown(fifth_para, unsafe_allow_html=True)

sixth_para = '''<p style="font-family:Verdana; color: white; font-size: 14px">
    Citations....<p>'''
st.markdown(sixth_para, unsafe_allow_html=True)
