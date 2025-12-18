# 📘 README – Etapa 5: Configurarea și Antrenarea Modelului RN

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Negru Adam-Andrei-Pablo
**Link Repository GitHub:** https://github.com/Negrutzu/Negru-Adam-631AB-Proiect-RN
**Data predării:** 18.12.2025

---

## Scopul Etapei 5

Această etapă corespunde punctului 6. Configurarea și antrenarea modelului RN din lista de 9 etape.

Obiectiv principal: Antrenarea efectivă a modelului CNN definit în Etapa 4 pentru clasificarea formelor geometrice ale pieselor auto, evaluarea performanței pe setul de test și integrarea în interfața Streamlit.

Pornire obligatorie:

State Machine definit și justificat

Cele 3 module funcționale (Data Logging, RN, UI)

100% date originale sintetice generate programatic

---

## PREREQUISITE – Verificare Etapa 4 (OBLIGATORIU)

- [X] **State Machine** definit și documentat în `docs/state_machine.*`
- [X] **Contribuție 100% date originale originale** în `data/generated/` (verificabil)
- [X] **Modul 1 (Data Logging)** funcțional - produce CSV-uri
- [X] **Modul 2 (RN)** cu arhitectură definită dar NEANTRENATĂ (`models/untrained_model.h5`)
- [X] **Modul 3 (UI/Web Service)** funcțional cu model dummy
- [X] **Tabelul "Nevoie → Soluție → Modul"** complet în README Etapa 4

---

## Pregătire Date pentru Antrenare 

Setul de date a fost generat programatic și organizat conform structurii cerute:

data/train/: 700 imagini (140 per clasă)

data/validation/: 150 imagini (30 per clasă)

data/test/: 150 imagini (30 per clasă)

S-au folosit aceiași parametri de preprocesare:

Format: Grayscale (128x128x1)

Normalizare: Strat intern Rescaling(1./255)

Split: 70% / 15% / 15%

---

##  Cerințe Structurate pe 3 Niveluri

### Nivel 1 – Obligatoriu pentru Toți (70% din punctaj)

Completați **TOATE** punctele următoare:

Nivel 1 – Obligatoriu pentru Toți
1. Antrenare model: S-a antrenat arhitectura CNN pe dataset-ul de 1000 imagini originale.

2. Epoci: 20 (cu Early Stopping activat).

3. Împărțire: Stratificată 70/15/15.

4. Metrici test set:

  - Acuratețe: 1.0 (100%)

  - F1-score (macro): 1.0

#### Tabel Hiperparametri și Justificări (OBLIGATORIU - Nivel 1)

Completați tabelul cu hiperparametrii folosiți și **justificați fiecare alegere**:

| **Hiperparametru** | **Valoare Aleasă** | **Justificare** |
|--------------------|-------------------|-----------------|
| Learning rate | 0.001 | Valoare standard pentru Adam optimizer care asigură o convergență stabilă pe date sintetice. |
| Batch size | Ex: 32 | Compromis optim între viteza de antrenare și stabilitatea gradientului pentru dimensiunea setului de date. |
| Number of epochs | 20 | S-a folosit Early Stopping; antrenarea s-a oprit la epoca 7 deoarece modelul a atins performanța maximă. |
| Optimizer | Adam | Algoritm adaptiv eficient pentru extragerea trăsăturilor geometrice din imagini grayscale. |
| Loss function | Sparse Categorical Crossentropy | Adecvată pentru clasificarea multi-class unde etichetele sunt reprezentate prin numere întregi. |
| Activation functions | ReLU (hidden), Softmax (output) | ReLU pentru evitarea dispariției gradientului, Softmax pentru distribuția de probabilitate a celor 5 clase. |


---

### Nivel 2 – Recomandat (85-90% din punctaj)


1. Early Stopping: Implementat pentru a opri antrenarea la epoca 7, prevenind overfitting-ul.

2. Grafic loss și val_loss: Salvează în docs/loss_curve.png.

3. Analiză erori: Completată în secțiunea dedicată.

### Nivel 3 – Bonus (până la 100%)

1. Early Stopping: Implementat pentru a opri antrenarea la epoca 7, prevenind overfitting-ul.

2. Grafic loss și val_loss: Salvează în docs/loss_curve.png.

3. Analiză erori: Completată în secțiunea dedicată.

## Verificare Consistență cu State Machine (Etapa 4)

| **Stare din Etapa 4** | **Implementare în Etapa 5** |
|-----------------------|-----------------------------|
| `IDLE` | Interfața Streamlit așteaptă încărcarea fișierului | 
| `PREPROCESS` | Resize 128x128 și conversie Grayscale în gui.py |
| `INFERENCE` | Predicție realizată de modelul încărcat din trained_model.h5 |
| `DISPLAY_RESULT` | Afișare etichetă clasă și scor de încredere (Confidence). |


## Analiză Erori în Context Industrial (OBLIGATORIU Nivel 2)

1. Pe ce clase greșește cel mai mult modelul?
Pe datele sintetice acuratețea este maximă, însă modelul poate prezenta confuzii între usa_stanga și usa_dreapta. Cauza probabilă este simetria geometrică a celor două piese, care diferă doar prin orientare, necesitând trăsături foarte specifice pentru diferențiere.

2. Ce caracteristici ale datelor cauzează erori?
Modelul este sensibil la inversia culorilor (piese albe pe fundal negru vs negru pe alb) și la normalizarea pixelilor. Dacă datele de intrare nu respectă contrastul folosit la antrenare, performanța scade drastic.

3. Ce implicații are pentru aplicația industrială?
Identificarea greșită a unei uși pe partea opusă a caroseriei cauzează erori critice în linia de asamblare automatizată. False negative-urile (piese neidentificate) sunt preferabile în fața false positive-urilor (piese identificate greșit) pentru a evita montajul eronat.

4. Ce măsuri corective propuneți?
   1. Implementarea unui buton de "Inversare Culori" în interfață pentru adaptarea la diverse condiții de iluminare.

   2. Augmentarea setului de date cu rotații și variații de luminozitate pentru a simula reflexiile metalice reale.

   3. Controlul strict al fundalului în zona de inspecție vizuală pentru a menține consistența cu setul de antrenare.

## Structura Repository-ului la Finalul Etapei 5

**Clarificare organizare:** Vom folosi **README-uri separate** pentru fiecare etapă în folderul `docs/`:

```
proiect-rn-negru-adam/
├── README.md
├── etapa4_arhitectura_sia.md
├── etapa5_antrenare_model.md
│
├── docs/
│   ├── state_machine.png
│   ├── loss_curve.png
│   ├── confusion_matrix.png
│   └── screenshots/
│       ├── inference_real.png
│       └── ui_demo.png
│
├── data/
│   ├── raw/
│   ├── train/
│   ├── validation/
│   └── test/
│
├── src/
│   ├── neural_network/
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   └── model_def.py
│   └── app/
│       └── gui.py
│
├── models/
│   ├── untrained_model.h5
│   └── trained_model.h5
│
├── results/
│   ├── training_history.csv
│   └── test_metrics.json
│
└── requirements.txt
```

---

## Instrucțiuni de Rulare (Actualizate față de Etapa 4)

### 1. Setup mediu (dacă nu ați făcut deja)

```bash
pip install -r requirements.txt
```

### 2. Pregătire date (DACĂ ați adăugat date noi în Etapa 4)

```bash
python3 src/preprocessing/process_data.py
```

### 3. Antrenare model

```bash
python3 src/neural_network/train.py

# Output obtinut:
# Epoch 1/20 - accuracy: 0.7752 - loss: 0.5681 - val_accuracy: 1.0000 - val_loss: 7.9473e-10
# ...
# Epoch 7/20 - accuracy: 1.0000 - loss: 0.0000e+00 - val_accuracy: 1.0000 - val_loss: 0.0000e+00
# Epoch 7: early stopping
# Model saved to models/trained_model.h5
```

### 4. Evaluare pe test set

```bash
python3 src/neural_network/evaluate.py

# Output obtinut:
# Test Accuracy: 1.0
# Test F1-score (macro): 1.0
# Metrics saved to results/test_metrics.json
# Confusion matrix saved to docs/confusion_matrix.png
```

### 5. Lansare UI cu model antrenat

```bash
streamlit run src/app/gui.py
```

**Testare în UI:**

   1. Incarcare imagine din data/test/.

   2. Verificare predictie (trebuie sa fie corecta cu incredere ridicata).

   3. Screenshot salvat in docs/screenshots/inference_real.png.

---

## Checklist Final – Bifați Totul Înainte de Predare

Prerequisite Etapa 4
[x] State Machine documentat in docs/state_machine.png

[x] Contributie 100% date originale

[x] Cele 3 module din Etapa 4 functionale

Preprocesare si Date
[x] Dataset generat si preprocesat

[x] Split train/val/test: 70/15/15%

[x] Scaler folosit consistent

Antrenare Model - Nivel 1
[x] Model antrenat de la zero

[x] Antrenare oprita la epoca 7 (Early Stopping)

[x] Tabel hiperparametri completat

[x] Metrici test set: Accuracy 1.0, F1 1.0

[x] Model salvat in models/trained_model.h5

[x] results/training_history.csv generat

Integrare UI si Demonstratie - Nivel 1
[x] Model antrenat incarcat in gui.py

[x] UI realizeaza inferenta reala

[x] Screenshot in docs/screenshots/inference_real.png

Documentatie Nivel 2
[x] Early stopping implementat

[x] Grafic loss salvat in docs/loss_curve.png

[x] Analiza erori industriala completata

[x] Metrici Nivel 2 atinse (Accuracy 1.0)

Verificari Tehnice
[x] requirements.txt actualizat

[x] Path-uri relative folosite in cod

[x] Verificare anti-plagiat respectata

[x] Tag git creat corespunzator

---

## Livrabile Obligatorii (Nivel 1)

Asigurați-vă că următoarele fișiere există și sunt completate:

1. **`docs/etapa5_antrenare_model.md`** (acest fișier) cu:
   - Tabel hiperparametri + justificări (complet)
   - Metrici test set raportate (accuracy, F1)
   - (Nivel 2) Analiză erori context industrial (4 paragrafe)

2. **`models/trained_model.h5`** (sau `.pt`, `.lvmodel`) - model antrenat funcțional

3. **`results/training_history.csv`** - toate epoch-urile salvate

4. **`results/test_metrics.json`** - metrici finale:

```json
{
  "test_accuracy": 1.0,
  "test_f1_macro": 1.0
}
```

5. **`docs/screenshots/inference_real.png`** - demonstrație UI cu model antrenat

6. **(Nivel 2)** `docs/loss_curve.png` - grafic antrenare

7. **(Nivel 3)** `docs/confusion_matrix.png` + analiză în README

---

## Predare și Contact

**Predarea se face prin:**
1. Commit pe GitHub: `"Etapa 5 completa – Accuracy=1.0, F1=1.0"`
2. Tag: `git tag -a v0.5-model-trained -m "Etapa 5 - Model antrenat"`
3. Push: `git push origin main --tags`

---