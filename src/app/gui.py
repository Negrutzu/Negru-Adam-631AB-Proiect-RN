import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image
import os

st.title("🚗 SIA Piese Auto - Etapa 4")
st.write("Modul de clasificare (Arhitectură funcțională)")

model_path = "models/untrained_model.h5"

if os.path.exists(model_path):
    model = tf.keras.models.load_model(model_path)
    st.success("Sistem inițializat. Model RN încărcat.")
else:
    st.error("Modelul lipseste! Rulează mai întâi 'src/neural_network/model_def.py'")
    st.stop()

uploaded_file = st.file_uploader("Încarcă o imagine cu o piesă", type=["png", "jpg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imaginea încărcată', width=300)
    
    if st.button("Identifică Piesa"):
        img_array = np.array(image)
        img_resized = cv2.resize(img_array, (128, 128))
        
        if len(img_resized.shape) == 3:
            img_gray = cv2.cvtColor(img_resized, cv2.COLOR_RGB2GRAY)
        else:
            img_gray = img_resized
            
        input_data = img_gray.reshape(1, 128, 128, 1) / 255.0
        
        pred = model.predict(input_data)
        clasa = np.argmax(pred)
        
        labels = ["Aripă", "Capotă", "Portbagaj", "Ușă Dreapta", "Ușă Stânga"]
        rezultat = labels[clasa] if clasa < 5 else "Necunoscut"
        
        st.header(f"Rezultat: {rezultat}")
        st.warning("Atenție: Modelul este neantrenat (rezultat aleatoriu).")