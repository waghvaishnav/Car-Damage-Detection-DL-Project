import streamlit as st
from PIL import Image
from model_helper import predict

# ---------------- UI ---------------- #
st.set_page_config(page_title="Car Damage Detection", layout="centered")

st.title("🚗 Vehicle Damage Detection System")

st.write("Upload a car image and the model will detect the damage type.")

# ---------------- UPLOAD ---------------- #
uploaded_file = st.file_uploader(
    "Upload Car Image",
    type=["jpg", "jpeg", "png"]
)

# ---------------- PREDICTION ---------------- #
if uploaded_file is not None:

    # Open image directly (NO temp file needed)
    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.write("🔍 Processing...")

    prediction = predict(image)

    st.success(f"Prediction: **{prediction}**")