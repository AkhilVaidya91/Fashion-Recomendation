import streamlit as st
import os
import pandas as pd
import tensorflow as tf
import numpy as np
from keras.applications import vgg16
from keras.preprocessing import image
from keras.layers import GlobalMaxPooling2D
import base64
from st_clickable_images import clickable_images
import random
# import google.generativeai as genai
# genai.configure(api_key="AIzaSyDQL2Q6kgbFTkBNRtobvvGHqEYZEa1tojM")
from keyword_filter import search_keywords, extract_keywords
from streamlit_extras.switch_page_button import switch_page

height, width, channels = 100, 100, 3
model = vgg16.VGG16(weights='imagenet', include_top=False, input_shape=(height, width, channels))
model.trainable = False
ext_model = tf.keras.Sequential([model, GlobalMaxPooling2D()])

df = pd.read_csv('styles.csv')

st.set_page_config(page_title="Fashion Valley", page_icon="👗", layout="wide")
st.title('Product details')

with open("image_selected.txt", "r+") as file:
    inp = file.read()
    file.truncate(0)

images_folder_path = 'images'
img_path = os.path.join(images_folder_path, inp)
title = df[df['id'] == int(inp.split('.')[0])]['productDisplayName'].values[0]
st.subheader(f'Name:  {title}')
st.markdown('**Price: Rs.** ' + str(random.randint(800, 2000)))
# st.markdown("<h4>f'Price: {str(random.randint(800, 2000))}</h4>", unsafe_allow_html=True)
st.image(img_path, caption='selected image', width=300)

st.subheader('Similar products')
img = image.load_img(img_path, target_size=(height, width))
img = np.expand_dims(img, axis=0)
img = img[0]
img = np.array(img)
embed = ext_model.predict(np.expand_dims(img, axis=0))
df_sample_image = pd.DataFrame(embed)
df_embeddings = pd.read_csv('embeddings_44k.csv', index_col=False)
from sklearn.neighbors import NearestNeighbors

nn_model = NearestNeighbors(n_neighbors=7, algorithm='brute', metric='cosine')
nn_model.fit(df_embeddings)
distances, indices = nn_model.kneighbors(embed)
similar_indices = indices[0][1:]
image_dir = os.listdir('images')

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

row_images = []

for idx in similar_indices:
    image_path = os.path.join('images', image_dir[idx])
    row_images.append(image_path)
clicked = clickable_images(
[f'data:image/png;base64,{get_img_as_base64(image)}' for image in row_images],
div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
img_style={"margin": "2px", "height": "200px"},
)
row_images = []

######

img_path = os.path.join('images', image_dir[idx])
st.subheader('Based on your previous purchases:')

img = image.load_img(img_path, target_size=(height, width))
img = np.expand_dims(img, axis=0)
img = img[0]
img = np.array(img)
embed = ext_model.predict(np.expand_dims(img, axis=0))
df_sample_image = pd.DataFrame(embed)
from sklearn.neighbors import NearestNeighbors
distances, indices = nn_model.kneighbors(embed)
similar_indices = indices[0][1:]
image_dir = os.listdir('images')

row_images = []

for idx in similar_indices:
    image_path = os.path.join('images', image_dir[idx])
    row_images.append(image_path)
clicked = clickable_images(
[f'data:image/png;base64,{get_img_as_base64(image)}' for image in row_images],
div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
img_style={"margin": "2px", "height": "200px"},
)
row_images = []

#####

st.subheader('Recomended items to complete your outfit')


# input_string = title
# model = genai.GenerativeModel('gemini-pro')
# prompt = "Generate a complete outfit for the following clothing: " + input_string + "follow the following format for output: topwear: <>\n bottomwear: <>,\n footwear: <>. include only one appreal per category."
# response = model.generate_content(prompt)
# search_prompt = str(response.text)
# st.text(search_prompt)








# search_prompt = search_prompt.split(":")
# topwear_prompt = search_prompt[1]
# bottomwear_prompt = search_prompt[2]
# footwear_prompt = search_prompt[3]

# topwear_prompt = extract_keywords(topwear_prompt)
# bottomwear_prompt = extract_keywords(bottomwear_prompt)
# footwear_prompt = extract_keywords(footwear_prompt)

# image_folder = "images"
# image_files = [filename for filename in os.listdir(image_folder) if filename.endswith(".jpg")]
# search_results = search_keywords(bottomwear_prompt, df)
# row_images = []

# for image_file in search_results:
#     image_path = os.path.join(image_folder, image_file)
#     row_images.append(image_path)
# clicked = clickable_images(
# [f'data:image/png;base64,{get_img_as_base64(image)}' for image in row_images],
# div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
# img_style={"margin": "2px", "height": "200px"},
# )
# row_images = []

# if clicked > -1:
#     image_selected = search_results[clicked] ## image_name.jpg
#     with open("image_selected.txt", "w") as file:
#         file.write(image_selected)
#     # st.experimental_set_query_params(clicked = image_selected)
#     switch_page("description_page")