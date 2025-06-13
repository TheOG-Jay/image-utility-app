import streamlit as st
import cv2
import numpy as np
from PIL import Image

def cartoonify(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
    )
    color = cv2.bilateralFilter(img, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

def run():
    st.header("🎨 Cartoonify Your Image")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="cartoon_upload")

    if uploaded_file:
        image = Image.open(uploaded_file)
        img_np = np.array(image)
        img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

        cartoon = cartoonify(img_cv)
        cartoon_rgb = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)

        st.image([image, cartoon_rgb], caption=["Original", "Cartoonified"], use_column_width=True)

        # Save option
        cartoon_pil = Image.fromarray(cartoon_rgb)
        st.download_button("📥 Download Cartoon Image", data=cv2.imencode('.png', cartoon_rgb)[1].tobytes(),
                           file_name="cartoonified.png", mime="image/png")
