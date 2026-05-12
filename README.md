**Aegis — Deepfake Detection System**


**Overview**

Aegis is an AI-powered deepfake detection system designed to identify manipulated videos using deep learning and computer vision techniques. 
The project focuses on detecting inconsistencies in facial features and synthetic artifacts commonly found in AI-generated media.

The system processes uploaded videos, extracts facial frames using OpenCV, and classifies them as Authentic or Deepfake using a Convolutional Neural Network (CNN). 
The model is deployed through an interactive Streamlit web application for real-time testing and demonstration.

**Motivation**

The rise of AI-generated media has increased the spread of misinformation, identity manipulation, and digital impersonation. 
Aegis was developed to explore how machine learning can be used to detect synthetic media and improve trust in digital content.

**Dataset**

The model was trained on publicly available deepfake datasets containing both authentic and manipulated videos.

**Preprocessing Steps**

Extracted video frames using OpenCV
Resized and normalized images
Removed corrupted frames
Balanced authentic and manipulated samples
Split data into training, validation, and testing sets

**Model**

*CNN Architecture*

The model uses a Convolutional Neural Network to learn spatial patterns and visual inconsistencies in facial regions.

*Key Components*

Convolutional Layers
ReLU Activation
Max Pooling
Dropout Regularization
Fully Connected Layers
Softmax/Sigmoid Output

**Performance**

Validation Accuracy	 ~92%

Inference Optimization    30% Faster

Frames Processed	  10,000+

**Challenges Faced**

Handling imbalanced datasets

Reducing false positives

Detecting high-quality deepfakes

Optimizing inference speed for real-time usability

Managing noisy and low-resolution frames


**Future Improvements**


Temporal modeling using LSTMs or Transformers

Real-time webcam detection

Vision Transformer (ViT)-based architecture

Explainable AI visualizations
Audio-visual multimodal deepfake detection
Cloud deployment for scalable inference
