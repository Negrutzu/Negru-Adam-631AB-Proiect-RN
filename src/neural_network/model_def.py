import os
import tensorflow as tf
from tensorflow.keras import layers, models

def create_and_save_model():
    model = models.Sequential([
        layers.Input(shape=(128, 128, 1)),
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(5, activation='softmax') # 5 clase: aripa, capota, etc.
    ])
    
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    if not os.path.exists("models"):
        os.makedirs("models")
    
    model.save("models/untrained_model.h5")
    print("✅ Model definit și salvat cu succes în 'models/untrained_model.h5'")

if __name__ == "__main__":
    create_and_save_model()