import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from pages.prediction import *


sns.set_theme(style="darkgrid")
sns.set()


# uploaded_file = st.file_uploader("Upload Image")

supernova_title = '<p style="font-family:sans-serif; font-size: 42px;">Supernova Classification!!!!!</p>'
st.markdown(supernova_title, unsafe_allow_html=True)
#st.title("Supernova Classification!!!!!")
st.markdown(""":collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision::collision::collision::collision:
            :collision:""")
first_para = '''<p style="font-family:sans-serif; font-size: 18px;">This project was created by 4 students
        from the Le Wagon Data Science Bootcamp.
        Using Dr. Susan Panova, we will be able to look at telescopic images
        of space to detect whether there is a supernova present or not.</p>'''
st.markdown(first_para, unsafe_allow_html=True)

st.text("""This is important for astronomers as supernovae are the largest
        explosion that humans know of. As a result, massive amounts of dark energy
        and matter are released. Dark energy and dark matter make up around 95% of
        the universe and still remain the biggest mystery of space.""")

# text over upload button "Upload Image"
