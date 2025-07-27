import streamlit as st
import time
from pathlib import Path
import base64
import folium
from streamlit_folium import st_folium

# --- Background Image ---
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

# --- Page Config ---
st.set_page_config(page_title="🎉 Happy Birthday Mamoni 🎂", layout="centered")
set_background("bday3.jpg")

# --- Title and Birth Info ---
st.title("🎂 Happy Birthday Mamoni! 🎉")
st.markdown("এই বিশেষ দিনটি ভালোবাসা, আনন্দ আর আশীর্বাদে ভরে উঠুক। আমরা তোমার জন্য গর্বিত ও কৃতজ্ঞ। 💐❤️")

from datetime import datetime, timedelta

# --- Birthday Info ---
st.markdown("""
<h3 style='text-align: center; color: #ff69b4; font-weight: bold;'>
🕘 জন্মের সময়: রাত ৯টা, শুক্রবার, ২৮ জুলাই ১৯৭২
</h3>
""", unsafe_allow_html=True)

# --- Countdown to Next Birthday ---
today = datetime.now()
current_year = today.year
next_birthday = datetime(current_year, 7, 28, 21)  # 28 July at 9 PM

# If birthday this year has passed, set it for next year
if today > next_birthday:
    next_birthday = datetime(current_year + 1, 7, 28, 21)

# Calculate time difference
time_remaining = next_birthday - today
days = time_remaining.days
hours, rem = divmod(time_remaining.seconds, 3600)
minutes, seconds = divmod(rem, 60)

# Display the countdown
st.markdown(f"""
<div style='text-align: center; font-size: 20px; color: #f63366; margin-top: -10px;'>
🎉 <b>🎉 জন্মের সময় বাকি:</b><br>
🗓️ {days} দিন {hours} ঘন্টা {minutes} মিনিট {seconds} সেকেন্ড ⏳
</div>
""", unsafe_allow_html=True)


# --- Ribbons in Corners ---
st.markdown("""
<style>
.ribbon-wrap { position: fixed; z-index: 9999; pointer-events: none; }
.ribbon {
  width: 150px; height: 30px;
  background: linear-gradient(45deg, #ff69b4, #ff1493);
  color: white; text-align: center;
  line-height: 30px; font-weight: bold; font-size: 14px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.3);
}
.ribbon-top-left    { top: 20px; left: -40px; transform: rotate(-45deg); }
.ribbon-top-right   { top: 20px; right: -40px; transform: rotate(45deg); }
.ribbon-bottom-left { bottom: 20px; left: -40px; transform: rotate(45deg); }
.ribbon-bottom-right{ bottom: 20px; right: -40px; transform: rotate(-45deg); }
</style>
<div class="ribbon-wrap ribbon-top-left"><div class="ribbon">🎉 Mamoni</div></div>
<div class="ribbon-wrap ribbon-top-right"><div class="ribbon">Happy B'day 🎂</div></div>
<div class="ribbon-wrap ribbon-bottom-left"><div class="ribbon">With Love 💖</div></div>
<div class="ribbon-wrap ribbon-bottom-right"><div class="ribbon">Forever 💐</div></div>
""", unsafe_allow_html=True)

# --- Balloons ---
st.markdown("""
<style>
.balloons-container {
  position: fixed; bottom: 0; left: 0; width: 100%; height: 100%;
  z-index: 9999; pointer-events: none; overflow: hidden;
}
.balloon {
  position: absolute; bottom: -100px;
  width: 60px; height: 80px;
  border-radius: 30px;
  animation: floatUp 8s ease-in infinite;
}
.balloon::after {
  content: ""; position: absolute; top: 80px; left: 29px;
  width: 2px; height: 30px; background: #555;
}
@keyframes floatUp {
  0% { transform: translateY(0) rotate(0deg); opacity: 1; }
  100% { transform: translateY(-120vh) rotate(15deg); opacity: 0; }
}
</style>
<div class="balloons-container">
  <div class="balloon" style="left:10%; background-color:#FF6F91;"></div>
  <div class="balloon" style="left:30%; background-color:#FF9671;"></div>
  <div class="balloon" style="left:50%; background-color:#FFC75F;"></div>
  <div class="balloon" style="left:70%; background-color:#D65DB1;"></div>
  <div class="balloon" style="left:85%; background-color:#845EC2;"></div>
</div>
""", unsafe_allow_html=True)

# --- Falling Ribbons ---
st.markdown("""
<style>
@keyframes fall {
  0% { transform: translateY(-120px) rotate(0deg); opacity: 1; }
  100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
}
.ribbon-container {
  position: fixed; top: 0; left: 0;
  width: 100vw; height: 100vh;
  pointer-events: none; z-index: 9998;
}
.ribbon {
  position: absolute; top: -60px;
  width: 12px; height: 60px;
  border-radius: 5px;
  opacity: 0.9;
  animation: fall 6s linear infinite;
}
.ribbon:nth-child(1) { left: 10%; background-color: #FFD700; animation-delay: 0s; }
.ribbon:nth-child(2) { left: 25%; background-color: #FF69B4; animation-delay: 0.5s; }
.ribbon:nth-child(3) { left: 40%; background-color: #00FA9A; animation-delay: 1s; }
.ribbon:nth-child(4) { left: 55%; background-color: #FF6347; animation-delay: 1.5s; }
.ribbon:nth-child(5) { left: 70%; background-color: #7B68EE; animation-delay: 2s; }
.ribbon:nth-child(6) { left: 85%; background-color: #40E0D0; animation-delay: 2.5s; }
.ribbon:nth-child(7) { left: 15%; background-color: #FFB6C1; animation-delay: 3s; }
.ribbon:nth-child(8) { left: 60%; background-color: #98FB98; animation-delay: 3.5s; }
</style>
<div class="ribbon-container">
  <div class="ribbon"></div><div class="ribbon"></div>
  <div class="ribbon"></div><div class="ribbon"></div>
  <div class="ribbon"></div><div class="ribbon"></div>
  <div class="ribbon"></div><div class="ribbon"></div>
</div>
""", unsafe_allow_html=True)

# --- Map Section ---
st.subheader("📌 তোমার জন্মস্থান")

m = folium.Map(location=[22.5048, 87.4610], zoom_start=10, control_scale=True)

folium.Marker([22.5046, 87.4604], popup="Paschim Medinipur Tolkua", tooltip="Paschim Medinipur Tolkua",
              icon=folium.Icon(color="red", icon="heart")).add_to(m)

with st.container():
    st_folium(m, use_container_width=True, height=700)

st.markdown("""
<style>
iframe[title="streamlit_folium.st_folium"] {
    height: 700px !important;
    width: 100% !important;
    border: none;
}
@media only screen and (max-width: 600px) {
    iframe[title="streamlit_folium.st_folium"] {
        height: 600px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# --- Birthday Song ---
st.header("তোমার জন্য একটা গান")
audio_path = Path("আজকের এই দিনটা শুধু তোমার, (1).mp3")
if audio_path.exists():
    with open(audio_path, "rb") as f:
        st.audio(f.read(), format="audio/mp3")
else:
    st.warning("🎵 Birthday song not found!")

# --- Session State ---
if "slideshow_played" not in st.session_state:
    st.session_state.slideshow_played = False
if "show_letter" not in st.session_state:
    st.session_state.show_letter = False

# --- Slideshow ---
st.subheader("তোমার কিছু হারিয়ে যাওয়া ছবি")
image_files = [
    Path(f"WhatsApp Image 2025-07-24 at 9.42.52 AM ({i}).jpeg") for i in range(1, 3)
] + [
    Path("WhatsApp Image 2025-07-24 at 9.42.52 AM.jpeg"),
    Path("WhatsApp Image 2025-07-24 at 9.42.53 AM (1).jpeg"),
    Path("WhatsApp Image 2025-07-24 at 9.42.53 AM (2).jpeg"),
    Path("WhatsApp Image 2025-07-24 at 9.42.53 AM.jpeg"),
    Path("WhatsApp Image 2025-07-24 at 9.42.54 AM (1).jpeg"),
    Path("WhatsApp Image 2025-07-24 at 9.42.54 AM (2).jpeg"),
    Path("WhatsApp Image 2025-07-24 at 9.42.54 AM.jpeg"),
    Path("WhatsApp Image 2025-07-24 at 9.43.41 AM.jpeg")
]

if not st.session_state.slideshow_played:
    ph = st.empty()
    for img in image_files:
        ph.image(str(img), use_container_width=True, caption=f"❤️ Mamoni – {img.name}")
        time.sleep(3)
    st.session_state.slideshow_played = True
# --- Letter Trigger ---
if st.session_state.slideshow_played and not st.session_state.show_letter:
    st.markdown("""
    <style>
    @keyframes quake {
      0%, 100% { transform: translateX(0); }
      25% { transform: translateX(-5px); }
      50% { transform: translateX(5px); }
      75% { transform: translateX(-5px); }
    }
    .button-wrapper {
        text-align: center;
        margin-top: 40px;
    }
    #shake-button {
        font-size: 140px;
        background: none;
        border: none;
        cursor: pointer;
        animation: quake 0.8s infinite;
        color: #d6336c;
    }
    #shake-button:hover { color: #ff4d6d; }
    </style>
    """, unsafe_allow_html=True)

    with st.form("trigger_form"):
        st.markdown('<div class="button-wrapper"><button id="shake-button">💌</button></div>', unsafe_allow_html=True)
        submitted = st.form_submit_button("Click to open message")
        if submitted:
            st.session_state.show_letter = True
            st.rerun()

# --- Birthday Letter ---
if st.session_state.show_letter:
    st.markdown("""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
    confetti({ particleCount: 150, spread: 80, origin: { y: 0.3 } });
    </script>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        background-color: #fff8dc; 
        border: 2px solid #f1c40f; 
        border-radius: 12px; 
        padding: 20px; 
        box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
        max-width: 600px;
        margin: 30px auto;
        font-family: 'Georgia', serif;
        font-size: 20px;
        color: #333;
        line-height: 1.6;
        animation: fadeIn 1s ease-in-out;
    ">
        ✨ প্রিয় মামণি,<br><br>
        এই বিশেষ দিনে তোমাকে জানাই হৃদয়ভরা শুভেচ্ছা ও ভালোবাসা।<br><br>
        প্রতিটা মুহূর্ত তোমার মুখের হাসিতে ভরে উঠুক, আর আগামী দিনগুলো হোক আশীর্বাদময় ও শান্তিময়।<br><br>
        ❤️ ভালোবাসা ও শ্রদ্ধা সহ,<br>
        তোমার মানি 💖
    </div>
    """, unsafe_allow_html=True)
st.caption("Made with ❤️ love by [Mani ❤️]")