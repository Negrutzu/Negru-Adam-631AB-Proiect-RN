import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image, ImageOps
import os

st.set_page_config(page_title="SIA Piese Auto", layout="centered")

st.title("SIA Piese Auto - Etapa 5")
st.write("Modul de clasificare cu inferenta reala")

model_path = "models/trained_model.h5"
LABELS = ['aripa', 'capota', 'portbagaj', 'usa_dreapta', 'usa_stanga']

@st.cache_resource
def load_model():
    if os.path.exists(model_path):
        return tf.keras.models.load_model(model_path)
    return None

model = load_model()

if model is None:
    st.error("Modelul nu a fost gasit.")
    st.stop()

uploaded_file = st.file_uploader("Incarca imagine", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('L')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(image, caption='Imagine Originala', use_container_width=True)
    
    invert = st.checkbox("Inverseaza Culorile", value=True)
    
    if invert:
        image = ImageOps.invert(image)
        with col1:
            st.image(image, caption='Imagine Procesata', use_container_width=True)

    if st.button("Identifica Piesa"):
        img_resized = image.resize((128, 128))
        img_array = np.array(img_resized)
        
        img_batch = np.expand_dims(img_array, axis=0) 
        img_batch = np.expand_dims(img_batch, axis=-1)

        input_data = img_batch.astype('float32')
        
        preds = model.predict(input_data)
        
        probs = preds[0]
        if not np.isclose(np.sum(probs), 1.0, atol=1e-5):
            probs = tf.nn.softmax(preds[0]).numpy()
            
        class_idx = np.argmax(probs)
        predicted_label = LABELS[class_idx]
        confidence = 100 * probs[class_idx]

        st.divider()
        with col2:
            st.subheader(f"Rezultat: {predicted_label}")
            st.write(f"Incredere: {confidence:.2f}%")
            
            st.write("Statistici per clasa:")
            for i, label in enumerate(LABELS):
                st.progress(float(probs[i]), text=f"{label}: {probs[i]*100:.1f}%")