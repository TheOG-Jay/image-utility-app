import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import textwrap
import io

def run():
    st.header("🖼 Meme Generator")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    top_text = st.text_input("Top Text", "Life before bugs...")
    bottom_text = st.text_input("Bottom Text", "...and after 🐛")

    def load_font(size):
        try:
            return ImageFont.truetype("assets/impact.ttf", size)
        except:
            return ImageFont.load_default()

    def draw_text(draw, text, y, image_width, font):
        lines = textwrap.wrap(text.upper(), width=25)
        for line in lines:
            bbox = font.getbbox(line)
            w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
            x = (image_width - w) / 2
            draw.text((x, y), line, font=font, fill="white", stroke_width=2, stroke_fill="black")
            y += h
        return y

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        draw = ImageDraw.Draw(image)
        font_size = max(32, image.height // 8)
        try:
           font = ImageFont.truetype("arial.ttf", size=font_size)
        except:
           font = ImageFont.load_default()
        draw_text(draw, top_text, 10, image.width, font)
        draw_text(draw, bottom_text, image.height - int(image.height / 5), image.width, font)
        st.image(image, use_column_width=True)

        buf = io.BytesIO()
        image.save(buf, format="PNG")
        st.download_button("📥 Download Meme", data=buf.getvalue(), file_name="meme.png", mime="image/png")


    