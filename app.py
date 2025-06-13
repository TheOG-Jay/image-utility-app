import streamlit as st
import os
import importlib

st.set_page_config(page_title="Image Utility Hub", layout="wide")

# Glow title
st.markdown("""
    <style>
    .glow-title {
        position: absolute;
        top: 10px;
        left: 20px;
        font-size: 48px;
        font-weight: bold;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #fff;
        text-shadow: 
            0 0 5px #0ff, 
            0 0 10px #0ff, 
            0 0 20px #0ff, 
            0 0 40px #0ff;
        animation: glowPulse 2s ease-in-out infinite alternate;
        z-index: 9999;
    }

    @keyframes glowPulse {
        from {
            text-shadow:
                0 0 5px #0ff,
                0 0 10px #0ff,
                0 0 20px #0ff,
                0 0 40px #0ff;
        }
        to {
            text-shadow:
                0 0 10px #00f,
                0 0 20px #00f,
                0 0 30px #0ff,
                0 0 50px #0ff;
        }
    }
    </style>

    <div class="glow-title">✨ImageLab Pro✨</div>
""", unsafe_allow_html=True)

# Spacer for visual layout
st.title(" ")

# Load modules from 'modules' folder
MODULE_DIR = "modules"

if not os.path.exists(MODULE_DIR):
    st.error(f"❌ The folder '{MODULE_DIR}' does not exist. Please create it.")
    st.stop()

modules = [f.replace(".py", "") for f in os.listdir(MODULE_DIR) if f.endswith(".py") and f != "__init__.py"]

if not modules:
    st.warning("No tools found in the 'modules' folder.")
    st.stop()

tabs = st.tabs([f"🔹 {name.replace('_', ' ').title()}" for name in modules])

for tab, module_name in zip(tabs, modules):
    with tab:
        try:
            module = importlib.import_module(f"{MODULE_DIR}.{module_name}")
            if hasattr(module, "run") and callable(module.run):
                module.run()
            else:
                st.warning(f"⚠️ `{module_name}.py` does not have a `run()` function.")
        except Exception as e:
            st.error(f"❌ Failed to load `{module_name}`: {e}")

# Background Image
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1503264116251-35a269479413");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
""", unsafe_allow_html=True)

# Custom styling for tabs
st.markdown("""
    <style>
    section[data-testid="stTabs"] > div {
        background-color: #111;
        border-radius: 10px;
        padding: 8px;
    }

    button[data-baseweb="tab"] {
        background-color: #222 !important;
        color: #0ff !important;
        font-weight: bold;
        border: 2px solid #0ff !important;
        border-radius: 10px !important;
        margin: 4px !important;
        padding: 12px 20px !important;
        transition: all 0.3s ease-in-out;
        font-size: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 48px;
    }

    button[data-baseweb="tab"]:hover {
        background-color: #00f2ff !important;
        color: #000 !important;
        transform: scale(1.05);
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #0ff !important;
        color: #000 !important;
        box-shadow: 0 0 10px #0ff;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
    .stSelectbox > div[data-baseweb="select"] {
        background-color: #111;
        border: 2px solid #0ff;
        border-radius: 10px;
    }
    .stFileUploader {
        background-color: #1a1a1a;
        border-radius: 10px;
        padding: 8px;
    }
    .stButton button {
        background-color: #0ff;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 16px;
    }
    .stButton button:hover {
        background-color: #00e0e0;
        color: #000;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)
