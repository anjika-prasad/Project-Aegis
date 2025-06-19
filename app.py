import streamlit as st

st.set_page_config(page_title="Deepfake analyser", layout="wide")  # wide layout

st.markdown("""
    <style>
    
    body {
        background-color: #fff0f5;
    }
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
        color:#880e4f;
    }
    
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
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
    <div class="taskbar">
        <div><strong style='font-size: 20px;'>💖 Deepfake Analyzer</strong></div>
        <div>
            <a href="#upload">Upload</a>
            <a href="#results">Results</a>
            <a href="#about">About</a>
        </div>
    </div>
""", unsafe_allow_html=True)





st.markdown("<h1 style='color:#880e4f;'>Deepfake Detector</h1>", unsafe_allow_html=True)
st.write("Upload a video to get started.")


col1,spacer, col2 = st.columns([2,1,2])




with col1:
    st.markdown(f"""
        <div class="pink-card">
            <h3 style='color:#880e4f;'>Upload</h3>
            <p style='color:#880e4f; font-weight:bold;'>Upload a video file</p>
        </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Video Upload Label", label_visibility="collapsed")


st.markdown("<hr style='border:1px solid #bbb;'>", unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="pink-card">
            <h3 style='color:#880e4f;'>Results</h3>
            <p style='color:#880e4f; font-weight:bold;'>Results will appear here</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<h3 style='color:#880e4f;'>About This Project</h3>", unsafe_allow_html=True)  
st.write("A deepfake analysis project by Team Aegis.")  

