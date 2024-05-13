
import streamlit as st
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Function to resize image
def resize_image(img, max_size=(800, 600)):

    img.thumbnail(max_size, Image.ANTIALIAS)
    return img

with open("designing.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)


# Custom CSS for styling
st.markdown("""
<style>
    .title {
        font-size: 36px;
        color: #333;
        text-align: center;
        margin-bottom: 30px;
    }
    .subheader {
        font-size: 24px;
        color: white;
        margin-bottom: 20px;
    }
    .header {
        font-size: 20px;
        color: #666;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    body {
        background-color: #f0f0f0; /* Fallback background color */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
    }
</style>
""", unsafe_allow_html=True)

st.title("Dominant Colour Extraction")
st.markdown("<p class='subheader'>Upload an image and select the number of colours to extract</p>", unsafe_allow_html=True)

img = st.file_uploader('Choose an image')

if img is not None:
    st.markdown("<h2 class='header'>Original Image</h2>", unsafe_allow_html=True)
    st.image(img)

    x = st.slider('Pick number of colours', 1, 10)

    # Read and resize the image
    input_img = Image.open(img)
    resized_img = resize_image(input_img)

    # Convert resized image to numpy array
    img_array = np.array(resized_img)

    # KMEANS CODE
    n = img_array.shape[0] * img_array.shape[1]
    all_pixels = img_array.reshape((n, 3))

    model = KMeans(n_clusters=x)
    model.fit(all_pixels)

    centers = model.cluster_centers_.astype('uint8')

    new_img = np.zeros((n, 3), dtype='uint8')

    for i in range(n):
        group_idx = model.labels_[i]
        new_img[i] = centers[group_idx]

    new_img = new_img.reshape(*img_array.shape)

    st.markdown("<h2 class='header'>Modified Image</h2>", unsafe_allow_html=True)
    st.image(new_img)
