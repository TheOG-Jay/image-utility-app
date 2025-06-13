### modules/background_remover.py
import streamlit as st
from PIL import Image
from rembg import remove
import io

def run():
    st.markdown("### 📤 Upload Your Image")
    uploaded_file = st.file_uploader("Choose an image to remove background", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

    if uploaded_file:
        input_image = Image.open(uploaded_file).convert("RGB")
        output_image = remove(input_image)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 🖼️ Original Image")
            st.image(input_image, use_column_width=True)

        with col2:
            st.markdown("#### 🧼 Background Removed")
            st.image(output_image, use_column_width=True)

        st.download_button("📥 Download Result", data=convert_image(output_image), file_name="bg_removed.png", mime="image/png")

def convert_image(image):
    byte_arr = io.BytesIO()
    image.save(byte_arr, format='PNG')
    return byte_arr.getvalue()
