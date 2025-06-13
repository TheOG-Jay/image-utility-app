import streamlit as st
from PIL import Image
from io import BytesIO

# ... your filter functions here ...

def run():
    st.markdown(
        "<h2 style='text-align: center; color: cyan; font-size: 36px;'>🎨 Image Filter Studio</h2>",
        unsafe_allow_html=True,
    )

    # 🎚️ Select filter always visible
    filter_option = st.selectbox(
        "🔧 Choose a filter:",
        (
            "Retro",
            "Sepia",
            "Pixel Art",
            "Black & White with Tint",
            "Soft Glow",
            "Comic Book Style",
            "Duotone"
        )
    )

    uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)

        # Apply selected filter
        if filter_option == "Retro":
            filtered_image = apply_retro(image)
        elif filter_option == "Sepia":
            filtered_image = apply_sepia(image)
        elif filter_option == "Pixel Art":
            filtered_image = apply_pixel_art(image)
        elif filter_option == "Black & White with Tint":
            filtered_image = apply_bw_tint(image)
        elif filter_option == "Soft Glow":
            filtered_image = apply_soft_glow(image)
        elif filter_option == "Comic Book Style":
            filtered_image = apply_comic(image)
        elif filter_option == "Duotone":
            filtered_image = apply_duotone(image)
        else:
            filtered_image = image

        # 📊 Layout: side-by-side view
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**🖼 Original**")
            st.image(image, use_column_width=True)
        with col2:
            st.markdown(f"**✨ {filter_option} Filter Applied**")
            st.image(filtered_image, use_column_width=True)

        # 📥 Download button
        buf = BytesIO()
        filtered_image.save(buf, format="PNG")
        st.download_button("⬇️ Download Filtered Image", buf.getvalue(), "filtered.png", "image/png")

    else:
        st.info("📁 Please upload an image to preview the filter.")
