import streamlit as st
import numpy as np
from PIL import Image, ImageOps, ImageFilter
import pickle

# Load the model using pickle
with open("Digit_Recognizer.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Digit Recognizer", layout="centered")
st.title("🧠 Digit Recognizer with Decision Tree")
st.write("Upload a **28x28 grayscale** image of a digit (0-9).")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

def preprocess_image(image):
    # Convert to grayscale
    image = image.convert("L")
    # Resize to 28x28
    image = ImageOps.fit(image, (28, 28), method=Image.Resampling.LANCZOS)
    # Invert (white background, black digit)
    image = ImageOps.invert(image)
    # Flatten image to match model input (1, 784)
    img_array = np.array(image).reshape(1, -1)
    return img_array

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=150)

    # Preprocess and predict
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)

    st.subheader("🔢 Predicted Digit:")
    st.success(f"**{prediction[0]}**")
