# modules/qr_generator.py

import streamlit as st
import qrcode
from io import BytesIO

def run():
    st.subheader("🔲 QR Code Generator")

    # Input from user
    data = st.text_input("Enter text or URL to generate QR code")

    if st.button("Generate QR Code") and data:
        # Generate QR Code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert image to BytesIO for Streamlit
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_img = buf.getvalue()

        # Display the QR Code
        st.image(byte_img, caption="Generated QR Code", use_column_width=False)

        # Download button
        st.download_button("⬇️ Download QR Code", data=byte_img, file_name="qr_code.png", mime="image/png")
