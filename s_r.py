import streamlit as st
import time

# Page setup
st.set_page_config(page_title="For My Love Susri ❤", page_icon="💖", layout="centered")

# 🌌 Background (night sky with stars)
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1950&q=80");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
[data-testid="stHeader"], [data-testid="stToolbar"] {
    background: rgba(0,0,0,0);
}
h1, h2, h3, h4, h5, h6, p, div {
    color: #fff !important;
    text-align: center;
}
.love-text {
    font-size: 40px;
    font-weight: bold;
    color: #ff3366;
    text-shadow: 2px 2px 10px #000;
}
.heart {
    font-size: 60px;
    animation: float 3s infinite ease-in-out;
}
@keyframes float {
    0% {transform: translateY(0);}
    50% {transform: translateY(-20px);}
    100% {transform: translateY(0);}
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 🎵 Romantic background music
st.audio("https://cdn.pixabay.com/audio/2023/03/03/audio_4cc1bb1531.mp3", autoplay=True)

# ❤ Main content
st.markdown("<h1 class='love-text'>I Love You Susri ❤</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color:pink;'>You’re my shining star in the night sky 🌟</h2>", unsafe_allow_html=True)

# 💞 Floating hearts animation
hearts = "💖 💞 💕 💓 💗 ❤ 💘"
for i in range(5):
    st.markdown(f"<h1 style='text-align:center;'>{hearts}</h1>", unsafe_allow_html=True)
    time.sleep(0.5)

st.markdown("<p style='margin-top:40px;'>Made with 💖 only for you, Susri.</p>", unsafe_allow_html=True)
