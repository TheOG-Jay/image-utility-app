import streamlit as st
from PIL import Image
import io

def run():
    st.subheader("📉 Image Compression")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="compress_upload")
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_column_width=True)

        quality = st.slider("Select Compression Quality", 10, 95, 75, key="compress_quality")

        buffer = io.BytesIO()
        image.save(buffer, format="JPEG", quality=quality)
        buffer.seek(0)

        st.image(buffer, caption=f"Compressed Image (Quality {quality})", use_column_width=True)

        st.download_button(
            label="📥 Download Compressed Image",
            data=buffer,
            file_name="compressed.jpg",
            mime="image/jpeg",
            key="compress_download"
        )
