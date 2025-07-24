import streamlit as st
import time
import os
from pathlib import Path
import base64


def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()

    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Page config
st.set_page_config(page_title="🎉 Happy Birthday Mamoni 🎂", layout="centered")

# Set background
set_background(r"C:\Users\subha\Downloads\assets\bday2.jpg")




# --- Title and Header ---
st.title("🎂 Happy Birthday Mamoni! 🎉")
st.markdown("এই বিশেষ দিনটি ভালোবাসা, আনন্দ আর আশীর্বাদে ভরে উঠুক। আমরা তোমার জন্য গর্বিত ও কৃতজ্ঞ। 💐❤️")

# --- Audio Playback ---
balloon_animation = """
<style>
.balloons-container {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 9999;
    pointer-events: none;
    overflow: hidden;
}
.balloon {
    position: absolute;
    bottom: -100px;
    width: 60px;
    height: 80px;
    background-color: red;
    border-radius: 30px 30px 30px 30px;
    animation: floatUp 8s ease-in infinite;
}
.balloon::after {
    content: "";
    position: absolute;
    top: 80px;
    left: 29px;
    width: 2px;
    height: 30px;
    background: #555;
}
@keyframes floatUp {
    0% {
        transform: translateY(0) rotate(0deg);
        opacity: 1;
    }
    100% {
        transform: translateY(-120vh) rotate(15deg);
        opacity: 0;
    }
}
</style>

<div class="balloons-container">
  <div class="balloon" style="left:10%; background-color:#FF6F91; animation-delay: 0s;"></div>
  <div class="balloon" style="left:30%; background-color:#FF9671; animation-delay: 2s;"></div>
  <div class="balloon" style="left:50%; background-color:#FFC75F; animation-delay: 4s;"></div>
  <div class="balloon" style="left:70%; background-color:#D65DB1; animation-delay: 1s;"></div>
  <div class="balloon" style="left:85%; background-color:#845EC2; animation-delay: 3s;"></div>
</div>
"""

st.markdown(balloon_animation, unsafe_allow_html=True)
audio_path = Path(r"C:\Users\subha\Downloads\assets\Happy Birthday Mamoni (1).mp3")
if audio_path.exists():
    with open(audio_path, "rb") as audio_file:
        st.audio(audio_file.read(), format="audio/mp3")
else:
    st.warning("🎵 Birthday song not found in 'assets'.")

# --- Slideshow of JPEG Images ---
image_folder = Path(r"C:\Users\subha\Downloads\assets")
image_files = sorted(image_folder.glob("*.jpeg"))

if not image_files:
    st.error("🖼️ No JPEG images found in the 'assets' folder.")
else:
    placeholder = st.empty()
    slideshow_speed = 3  # seconds per image

    for img_path in image_files:
        placeholder.image(str(img_path), use_container_width=True, caption=f"❤️ Mamoni - {img_path.stem}")
        time.sleep(slideshow_speed)

# --- Floating Balloon Animation ---


# --- Final Message ---
st.success('''✨ মামণি, সামনে আসা বছরটা হোক ভালোবাসা আর শান্তিতে ভরপুর।
তুমি আমাদের জীবনের অমূল্য রত্ন — তোমার গুরুত্ব ভাষায় প্রকাশ করা যায় না 💖''')
