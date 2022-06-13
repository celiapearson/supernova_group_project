# import os

# import numpy as np

# from tensorflow.keras.models import load_model

# from tensorflow.keras.preprocessing.image import load_img,img_to_array

# from PIL import Image

# current_path = os.getcwd()

# category_path = os.path.join(current_path, '../static/images.gif')

# predictor_model = load_model('../static/model5.h5')

# def save_uploaded_file(uploaded_file):

#     try:

#         with open(os.path.join('../static/images',uploaded_file.name),'wb') as f:

#             f.write(uploaded_file.getbuffer())

#         return 1

#     except:

#         return 0

# def predictor(img_path):

#     img = load_img(img_path, target_size=(51,51,1), color_mode='grayscale')

#     img = img_to_array(img)

#     img = np.expand_dims(img,axis = 0)

#     prediction = predictor_model.predict(img)

#     return prediction[0][0]

# if uploaded_file is not None:

#     if save_uploaded_file(uploaded_file):

#         # display the image

#         display_image = Image.open(uploaded_file)

#         st.image(display_image)

#         prediction = predictor(os.path.join('static/images',uploaded_file.name))

#         os.remove('static/images/'+uploaded_file.name)

#         # deleting uploaded saved picture after prediction

#         # drawing graphs

#         st.text(f'Prediction: {prediction}')
