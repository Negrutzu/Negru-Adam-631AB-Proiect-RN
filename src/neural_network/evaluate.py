import os
import json
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix

DATA_DIR = "data"
MODELS_DIR = "models"
DOCS_DIR = "docs"
RESULTS_DIR = "results"
IMG_SIZE = (128, 128)

def main():
    model_path = f"{MODELS_DIR}/trained_model.h5"
    if not os.path.exists(model_path):
        print("Modelul antrenat nu există! Rulează train.py întâi.")
        return
        
    model = tf.keras.models.load_model(model_path)
    print("Model încărcat.")

    test_ds = tf.keras.utils.image_dataset_from_directory(
        f"{DATA_DIR}/test",
        image_size=IMG_SIZE,
        batch_size=32,
        color_mode='grayscale',
        shuffle=False
    )
    class_names = test_ds.class_names

    print("Se evaluează pe setul de test...")
    y_true = []
    y_pred = []

    for images, labels in test_ds:
        preds = model.predict(images, verbose=0)
        y_true.extend(labels.numpy())
        y_pred.extend(np.argmax(preds, axis=1))

    report = classification_report(y_true, y_pred, target_names=class_names, output_dict=True)
    
    metrics = {
        "test_accuracy": report["accuracy"],
        "test_f1_macro": report["macro avg"]["f1-score"]
    }
    with open(f"{RESULTS_DIR}/test_metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)
    print(f"Metrici salvate: Acc={metrics['test_accuracy']:.2f}, F1={metrics['test_f1_macro']:.2f}")

    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.savefig(f"{DOCS_DIR}/confusion_matrix.png")
    print(f"Matricea de confuzie salvată în {DOCS_DIR}/confusion_matrix.png")

    try:
        import pandas as pd
        hist = pd.read_csv(f"{RESULTS_DIR}/training_history.csv")
        plt.figure(figsize=(10, 4))
        plt.plot(hist['loss'], label='Train Loss')
        plt.plot(hist['val_loss'], label='Val Loss')
        plt.title('Curba de Învățare (Loss)')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        plt.savefig(f"{DOCS_DIR}/loss_curve.png")
        print(f"Curba de loss salvată în {DOCS_DIR}/loss_curve.png")
    except:
        print("Nu s-a putut genera Loss Curve (lipsește training_history.csv)")

if __name__ == "__main__":
    main()