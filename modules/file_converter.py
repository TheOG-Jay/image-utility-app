### modules/file_converter.py
import streamlit as st
from PIL import Image
import fitz  # PyMuPDF
import io

def run():
    st.markdown("### 📄 File Type Converter")
    option = st.radio("Choose Conversion Type", ["PDF to Image", "Image to PDF"])

    if option == "PDF to Image":
        pdf_file = st.file_uploader("Upload a PDF", type=["pdf"], label_visibility="collapsed")
        if pdf_file:
            images = convert_pdf_to_images(pdf_file)
            for i, img in enumerate(images):
                st.image(img, caption=f"Page {i+1}", use_column_width=True)
                st.download_button(f"📥 Download Page {i+1}", data=convert_image(img), file_name=f"page_{i+1}.png", mime="image/png")

    else:  # Image to PDF
        image_files = st.file_uploader("Upload Images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
        if image_files:
            images = [Image.open(img).convert("RGB") for img in image_files]
            pdf_bytes = convert_images_to_pdf(images)
            st.download_button("📥 Download PDF", data=pdf_bytes, file_name="converted.pdf", mime="application/pdf")

def convert_pdf_to_images(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    images = []
    for page in doc:
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        images.append(img)
    return images

def convert_images_to_pdf(images):
    buf = io.BytesIO()
    images[0].save(buf, format="PDF", save_all=True, append_images=images[1:])
    return buf.getvalue()

def convert_image(image):
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    return buf.getvalue()
