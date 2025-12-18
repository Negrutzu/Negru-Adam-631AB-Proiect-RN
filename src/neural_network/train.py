import os
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

IMG_SIZE = (128, 128)
BATCH_SIZE = 32
EPOCHS = 20  
DATA_DIR = "data"
MODELS_DIR = "models"
RESULTS_DIR = "results"

def create_model(num_classes):
    model = models.Sequential([
        layers.Input(shape=(128, 128, 1)),
        layers.Rescaling(1./255), # Normalizare 0-1
        
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def main():
    print("Se încarcă datele...")
    train_ds = tf.keras.utils.image_dataset_from_directory(
        f"{DATA_DIR}/train",
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        color_mode='grayscale',
        shuffle=True
    )
    
    val_ds = tf.keras.utils.image_dataset_from_directory(
        f"{DATA_DIR}/validation",
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        color_mode='grayscale'
    )

    class_names = train_ds.class_names
    print(f"Clase detectate: {class_names}")

    model = create_model(len(class_names))
    
    if not os.path.exists(MODELS_DIR): os.makedirs(MODELS_DIR)
    if not os.path.exists(RESULTS_DIR): os.makedirs(RESULTS_DIR)

    callbacks = [
        EarlyStopping(monitor='val_loss', patience=5, verbose=1),
        ModelCheckpoint(f"{MODELS_DIR}/trained_model.h5", save_best_only=True, monitor='val_loss')
    ]

    print("Începe antrenarea...")
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=EPOCHS,
        callbacks=callbacks
    )

    hist_df = pd.DataFrame(history.history)
    hist_df.to_csv(f"{RESULTS_DIR}/training_history.csv", index=False)
    print(f"Istoric salvat în {RESULTS_DIR}/training_history.csv")
    print(f"Model salvat în {MODELS_DIR}/trained_model.h5")

if __name__ == "__main__":
    main()