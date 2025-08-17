import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

model = load_model("../models/denoiser.keras")

st.title("Advanced Image Denoising Autoencoder")
uploaded_file = st.file_uploader("Upload an image", type=["jpg","png","jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    img = img.resize((32,32))
    img_array = np.array(img)/255.
    noisy = img_array + np.random.normal(0,0.05,img_array.shape)
    noisy = np.clip(noisy,0,1)
    denoised = model.predict(noisy[np.newaxis,...])[0]

    st.image(noisy, caption="Noisy Image", use_column_width=True)
    st.image(denoised, caption="Denoised Image", use_column_width=True)
    st.image(img_array, caption="Original Image", use_column_width=True)
