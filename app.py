import streamlit as st
import numpy as np
import cv2
import os
import tempfile
from tensorflow.keras.models import load_model
from mtcnn import MTCNN

# Set Streamlit page config
st.set_page_config(page_title="Deepfake analyser", layout="wide")

# 💅 Custom CSS
st.markdown("""
    <style>
    body { background-color: #fff0f5; }
    body, .stTextInput, .stFileUploader label, .stMarkdown, .stText {
        color: #880e4f;
    }
    .main {
        background-color: #fff0f5;
        padding: 0;
    }
    .pink-card {
        background-color: #ffe6f0;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(216, 27, 96, 0.2);
        border: 1px solid #f8bbd0;
        color: #880e4f;
    }
    .taskbar {
        background-color: #ffe6f0;
        padding: 15px 30px;
        border-radius: 0 0 12px 12px;
        color: #880e4f;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'Segoe UI', sans-serif;
        border-bottom: 2px solid #f8bbd0;
    }
    .taskbar a {
        color: #880e4f;
        margin: 0 10px;
        font-size: 18px;
        text-decoration: none;
        font-weight: 600;
        position: relative;
        transition: color 0.2s ease-in-out;
    }
    .taskbar a:not(:last-child)::after {
        content: "|";
        color: #d81b60;
        margin-left: 15px;
        margin-right: 10px;
        font-weight: 400;
    }
    .taskbar a:hover {
        text-decoration: underline;
        color: #d81b60;
    }
    </style>
""", unsafe_allow_html=True)

# 🧠 Load model and detector
model = load_model("deepfake_cnn_model.h5")
detector = MTCNN()

# 💻 Taskbar
st.markdown("""
    <div class="taskbar">
        <div><strong style='font-size: 20px;'>💖 Deepfake Analyzer</strong></div>
        <div>
            <a href="#upload">Upload</a>
            <a href="#results">Results</a>
            <a href="#about">About</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# 🎯 Title
st.markdown("<h1 style='color:#880e4f;'>Deepfake Detector</h1>", unsafe_allow_html=True)
st.write("Upload a video to get started.")

# 📦 Upload + Results cards
col1, spacer, col2 = st.columns([2, 0.5, 2])

with col1:
    st.markdown("""
        <div class="pink-card">
            <h3 style='color:#880e4f;'>Upload</h3>
            <p style='color:#880e4f; font-weight:bold;'>Upload a video file</p>
        </div>
    """, unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Video Upload Label", label_visibility="collapsed", type=["mp4", "avi", "mov"])

with col2:
    st.markdown("""
        <div class="pink-card">
            <h3 style='color:#880e4f;'>Results</h3>
            <p style='color:#880e4f; font-weight:bold;'>Results will appear here</p>
        </div>
    """, unsafe_allow_html=True)

# 🔍 Face Extraction & Prediction Logic
def extract_faces_from_video(video_path, max_faces=10):
    cap = cv2.VideoCapture(video_path)
    faces = []
    count = 0
    while cap.isOpened() and count < max_faces:
        ret, frame = cap.read()
        if not ret:
            break
        detections = detector.detect_faces(frame)
        for face in detections:
            x, y, w, h = face['box']
            x, y = max(0, x), max(0, y)
            face_img = frame[y:y+h, x:x+w]
            try:
                face_img = cv2.resize(face_img, (64, 64))
                faces.append(face_img)
                count += 1
                break
            except:
                continue  # Skip bad crops

        if count >= max_faces:
            break
    cap.release()
    return faces

# 🎥 Process uploaded video
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
        temp_video.write(uploaded_file.read())
        temp_path = temp_video.name

    with st.spinner("Analyzing video..."):
        faces = extract_faces_from_video(temp_path, max_faces=10)

        if not faces:
            st.error("No faces detected. Try a clearer video.")
        else:
            faces_np = np.array(faces) / 255.0
            preds = model.predict(faces_np)
            avg_prob = np.mean(preds)

            st.subheader("🎯 Prediction:")
            if avg_prob > 0.5:
                st.error(f"⚠️ This video is likely a **DEEPFAKE** ({avg_prob:.2f} confidence)")
            else:
                st.success(f"✅ This video is likely **REAL** ({1 - avg_prob:.2f} confidence)")

    os.remove(temp_path)

# 🧾 About section
st.markdown("<hr style='border:1px solid #bbb;'>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#880e4f;'>About This Project</h3>", unsafe_allow_html=True)
st.write("A deepfake detection project by Team Aegis using face-based CNN classification with MTCNN + CustomCNN.")
