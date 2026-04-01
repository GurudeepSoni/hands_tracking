import cv2
import streamlit as st

st.title("🖐️ Hand Detection (No Mediapipe)")

uploaded_file = st.file_uploader("Upload video", type=["mp4", "avi"])

if uploaded_file:
    file_bytes = uploaded_file.read()
    
    with open("temp.mp4", "wb") as f:
        f.write(file_bytes)

    cap = cv2.VideoCapture("temp.mp4")
    FRAME_WINDOW = st.image([])

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Simple threshold (fake hand segmentation)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        FRAME_WINDOW.image(thresh, channels="GRAY")

    cap.release()
