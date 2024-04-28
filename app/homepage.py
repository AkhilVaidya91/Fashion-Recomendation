import streamlit as st
import pandas as pd
from keyword_filter import search_keywords, extract_keywords
import os
import base64
from st_clickable_images import clickable_images
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

st.set_page_config(page_title="Fashion Valley", page_icon="👗", layout="wide")

img_yellow = Image.open("test.jpg")
img_yellow1 = Image.open("bg_image.jpg")

with open("style1.css","r") as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

img_yellow = Image.open("test.jpg")
img_yellow1 = Image.open("bg_image_3.png") # 1980x258

with st.container():
    st.image(img_yellow1)
    st.write("##")
    st.markdown('<h1 style="text-align: center;">Welcome to Fashion Valley</h1>', unsafe_allow_html=True)
    st.write("##")
    st.write("##")
    st.markdown('<h4 style="text-align: center;">A One-Stop solution to your Every Clothing Need.</h4>', unsafe_allow_html=True)
    st.write("---")

# page_bg_img = '''
# <style>
# body {
# background-image: url("https://images.pexels.com/photos/845434/pexels-photo-845434.jpeg?auto=compress&cs=tinysrgb&w=800");
# background-size: cover;
# }
# </style>
# '''

# st.markdown(page_bg_img, unsafe_allow_html=True)

# App Title and Subtitle
# st.header("Fashion Valley")
# st.subheader("Where Beauty Meets Fashion")

df = pd.read_csv('styles.csv')

st.subheader("Search for a product")
search_query = st.text_input(" ")
serc_token = extract_keywords(search_query)

image_folder = "images"
image_files = [filename for filename in os.listdir(image_folder) if filename.endswith(".jpg")]
search_results = search_keywords(serc_token, df)

# Define clickable images
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

row_images = []

for image_file in search_results:
    image_path = os.path.join(image_folder, image_file)
    row_images.append(image_path)
clicked = clickable_images(
[f'data:image/png;base64,{get_img_as_base64(image)}' for image in row_images],
div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
img_style={"margin": "2px", "height": "200px"},
)
row_images = []

if clicked > -1:
    image_selected = search_results[clicked] ## image_name.jpg
    with open("image_selected.txt", "w") as file:
        file.write(image_selected)
    # st.experimental_set_query_params(clicked = image_selected)
    switch_page("description_page")
st.write("---")

with st.container():
    st.write("##")
    st.markdown('<h2 style="text-align: center;">Bestsellers</h2>', unsafe_allow_html=True)
    # show images of 5-6 top rated items and make it clickable or smth idk
    
    search_results = []
    history = pd.read_csv('bestsellers.csv')
    history_img_ids = history['id']
    for element in history_img_ids:
        img_id = str(element) + '.jpg'
        search_results.append(img_id)


    row_images = []

    for image_file in search_results:
        image_path = os.path.join(image_folder, image_file)
        row_images.append(image_path)
    clicked = clickable_images(
    [f'data:image/png;base64,{get_img_as_base64(image)}' for image in row_images],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "2px", "height": "200px"},
    )
    row_images = []

    if clicked > -1:
        image_selected = search_results[clicked] ## image_name.jpg
        with open("image_selected.txt", "w") as file:
            file.write(image_selected)
            # st.experimental_set_query_params(clicked = image_selected)
        switch_page("description_page")

    st.write("---")

with st.container():
    image_column , text_column= st.columns(2)
    with text_column:
        st.subheader("Create a Custom Outfit")
        st.write("##")
        # add a button here linking to the outfit page
        st.write("##")
        st.write("Choose a top or bottom as your starting piece, and let us suggest complementary clothing to craft your perfect ensemble!")
    st.write("##")
    with image_column:
        st.image(img_yellow)
    #st.write("---")
    st.write("##")
with st.container():
    st.markdown('<h3 style="text-align: center; position: relative; color: red; margin: 200px;  margin-bottom: -100px" id="abc">Explore recommendations based on your past purchases</h3>', unsafe_allow_html=True)
    st.write("##")
    # add some reccs based on history here
    st.write("##")
    st.write("---")



## loading images from history
search_results = []
history = pd.read_csv('user.csv')
history_img_ids = history['img']
for element in history_img_ids:
    img_id = str(element) + '.jpg'
    search_results.append(img_id)


row_images = []

for image_file in search_results:
    image_path = os.path.join(image_folder, image_file)
    row_images.append(image_path)
clicked = clickable_images(
[f'data:image/png;base64,{get_img_as_base64(image)}' for image in row_images],
div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
img_style={"margin": "2px", "height": "200px"},
)
row_images = []

if clicked > -1:
    image_selected = search_results[clicked] ## image_name.jpg
    with open("image_selected.txt", "w") as file:
        file.write(image_selected)
        # st.experimental_set_query_params(clicked = image_selected)
    switch_page("description_page")

################################################
