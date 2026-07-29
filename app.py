import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import (
    preprocess_input,
    decode_predictions,
)
from tensorflow.keras.preprocessing.image import img_to_array

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Image Classification",
    page_icon="🖼️",
    layout="centered",
)

st.title("🖼️ Image Classification using MobileNetV2")
st.write("Upload an image and let the AI predict what it contains.")

# -------------------------------
# Load Model
# -------------------------------
@st.cache_resource
def load_model():
    model = MobileNetV2(weights="imagenet")
    return model

model = load_model()

# -------------------------------
# Upload Image
# -------------------------------
uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    # Resize image
    resized_image = image.resize((224, 224))

    image_array = img_to_array(resized_image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = preprocess_input(image_array)

    # Prediction
    with st.spinner("Predicting..."):
        predictions = model.predict(image_array)
        decoded_predictions = decode_predictions(predictions, top=5)[0]

    st.success("Prediction Complete!")

    st.subheader("Top 5 Predictions")

    for i, (_, label, probability) in enumerate(decoded_predictions, start=1):
        st.write(f"**{i}. {label}** — {probability * 100:.2f}%")