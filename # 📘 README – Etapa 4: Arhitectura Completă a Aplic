# 📘 README – Etapa 4: Arhitectura Completă a Aplicației SIA bazată pe Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Negru Adam Andrei Pablo  
**Link Repository GitHub:** https://github.com/Negrutzu/Negru-Adam-631AB-Proiect-RN
**Data:** 11.12.2025  

---

## Scopul Etapei 4

Această etapă corespunde punctului **5. Dezvoltarea arhitecturii aplicației software bazată pe RN** din lista de 9 etape.

**SCHELET COMPLET și FUNCȚIONAL al întregului Sistem cu Inteligență Artificială (SIA).**

### IMPORTANT - Ce înseamnă "schelet funcțional":

 **STATUS CURENT PROIECT:**
- [x] Toate modulele pornesc fără erori
- [x] Pipeline-ul complet rulează end-to-end (de la date → până la output UI)
- [x] Modelul RN este definit și compilat (arhitectura există)
- [x] Web Service/UI primește input și returnează output

---

##  Livrabile Obligatorii

### 1. Tabelul Nevoie Reală → Soluție SIA → Modul Software
*Soluția propusă pentru identificarea automată a elementelor de caroserie.*

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul** | **Modul software responsabil** |
|---------------------------|--------------------------------|--------------------------------|
| Identificarea pieselor pe banda de montaj pentru trasabilitate | Clasificare vizuală automată a formei (Aripă/Capotă) în < 1 secundă | Neural Network Module + UI |
| Reducerea erorilor de sortare manuală în logistică | Validare vizuală instantanee cu feedback (Label) afișat operatorului | Web Service / UI |
| Generarea de date pentru piese rare/prototipuri (fără costuri foto) | Simulare programatică a geometriei pieselor pentru un dataset 100% balansat | Data Acquisition Module |

---

### 2. Contribuția Voastră Originală la Setul de Date – MINIM 40% din Totalul Observațiilor Finale

#### Declarație obligatorie:

### Contribuția originală la setul de date:

**Total observații finale:** 5000 (estimat pentru antrenare)
**Observații originale:** 5000 (100%)

**Tipul contribuției:**
[X] Date generate prin simulare fizică / programatică
[ ] Date achiziționate cu senzori proprii  
[ ] Etichetare/adnotare manuală  
[ ] Date sintetice prin metode avansate  

**Descriere detaliată:**
Întregul set de date a fost generat prin metode programatice (simulare Python). Am utilizat algoritmi de desenare geometrică (`cv2`, `numpy`) pentru a simula formele ideale ale pieselor de caroserie: uși, aripi, capote și portbagaje.
Această abordare a permis controlul total asupra rezoluției (128x128), poziționării și varietății formelor, asigurând un dataset perfect echilibrat (balanced classes) și eliminând zgomotul de fundal specific imaginilor reale neprocesate.

**Locația codului:** `src/data_acquisition/generate_synthetic.py`
**Locația datelor:** `data/raw/` (sursa) și `data/processed/` (final)

**Dovezi:**
- Screenshot structură date populate: `docs/screenshots/ui_demo.png` (se vede input-ul din dataset)
- Scripturile de generare (`generate_dataset_...`) prezente în repository.

---

### 3. Diagrama State Machine a Întregului Sistem (OBLIGATORIE)

**Diagrama (Mermaid):**

```mermaid
stateDiagram-v2
    [*] --> IDLE
    
    IDLE --> UPLOAD_IMAGE : User Action (Drag & Drop)
    UPLOAD_IMAGE --> PREPROCESS : Image Received
    
    state PREPROCESS {
        [*] --> RESIZE_128
        RESIZE_128 --> GRAYSCALE
        GRAYSCALE --> NORMALIZE
    }
    
    PREPROCESS --> INFERENCE : Data Ready
    
    state INFERENCE {
        [*] --> LOAD_MODEL
        LOAD_MODEL --> PREDICT_CLASS
    }
    
    INFERENCE --> DISPLAY_RESULT : Success
    INFERENCE --> ERROR : Model Fail / Invalid File
    
    DISPLAY_RESULT --> IDLE : User Resets
    ERROR --> IDLE : Reset

    Legendă obligatorie:

    Justificarea State Machine-ului ales:
    Am ales arhitectura de tip Clasificare la Cerere (User Triggered) pentru că proiectul nostru simulează un post de control calitate unde operatorul uman sau un senzor declanșează verificarea unei piese specifice aflate pe bandă.

    Stările principale sunt:

    IDLE: Sistemul așteaptă input de la utilizator (interfața este activă, dar nu procesează nimic).

    PREPROCESS: Transformarea critică a imaginii brute în formatul tensorului acceptat de rețea (128x128 px, Grayscale, Normalizare [0-1]).

    INFERENCE: Modelul RN (CNN) rulează calculul "forward pass" pentru a determina probabilitățile celor 5 clase.

    DISPLAY_RESULT: Afișarea etichetei prezise (ex: "Portbagaj") și a imaginii analizate către operator.

    Tranzițiile critice sunt:

    UPLOAD → PREPROCESS: Se declanșează instantaneu la încărcarea fișierului.

    INFERENCE → ERROR: Dacă modelul nu este încărcat corect sau imaginea este coruptă, sistemul trebuie să revină în IDLE fără a se bloca (crash).

    Starea ERROR este esențială pentru că în mediul industrial imaginile pot veni corupte de la cameră sau formatul poate fi neacceptat.

# Continutul complet al README-ului
readme_content = """# 📘 README – Etapa 4: Arhitectura Completă a Aplicației SIA bazată pe Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Negru Adam Andrei Pablo  
**Link Repository GitHub:** [INSEREAZA_AICI_LINKUL_TAU_GITHUB]
**Data:** 11.12.2025  

---

## Scopul Etapei 4

Această etapă corespunde punctului **5. Dezvoltarea arhitecturii aplicației software bazată pe RN** din lista de 9 etape - slide 2 **RN Specificatii proiect.pdf**.

**Trebuie să livrați un SCHELET COMPLET și FUNCȚIONAL al întregului Sistem cu Inteligență Artificială (SIA). In acest stadiu modelul RN este doar definit și compilat (fără antrenare serioasă).**

### IMPORTANT - Ce înseamnă "schelet funcțional":

 **CE TREBUIE SĂ FUNCȚIONEZE (STATUS CURENT):**
- [x] Toate modulele pornesc fără erori
- [x] Pipeline-ul complet rulează end-to-end (de la date → până la output UI)
- [x] Modelul RN este definit și compilat (arhitectura există)
- [x] Web Service/UI primește input și returnează output

 **CE NU E NECESAR ÎN ETAPA 4:**
- Model RN antrenat cu performanță bună
- Hiperparametri optimizați
- Acuratețe mare pe test set
- Web Service/UI cu funcționalități avansate

**Scopul anti-plagiat:** Nu puteți copia un notebook + model pre-antrenat de pe internet, pentru că modelul vostru este NEANTRENAT în această etapă. Demonstrați că înțelegeți arhitectura și că ați construit sistemul de la zero.

---

##  Livrabile Obligatorii

### 1. Tabelul Nevoie Reală → Soluție SIA → Modul Software (max ½ pagină)
Completați in acest readme tabelul următor cu **minimum 2-3 rânduri** care leagă nevoia identificată în Etapa 1-2 cu modulele software pe care le construiți (metrici măsurabile obligatoriu):

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul vostru** | **Modul software responsabil** |
|---------------------------|--------------------------------|--------------------------------|
| Identificarea pieselor pe banda de montaj pentru trasabilitate | Clasificare vizuală automată a formei (Aripă/Capotă) în < 1 secundă | Neural Network Module + UI |
| Reducerea erorilor de sortare manuală în logistică | Validare vizuală instantanee cu feedback (Label) afișat operatorului | Web Service / UI |
| Generarea de date pentru piese rare/prototipuri (fără costuri foto) | Simulare programatică a geometriei pieselor pentru un dataset 100% balansat | Data Acquisition Module |

---

### 2. Contribuția Voastră Originală la Setul de Date – MINIM 40% din Totalul Observațiilor Finale

**Regula generală:** Din totalul de **N observații finale** în `data/processed/`, **minimum 40%** trebuie să fie **contribuția voastră originală**.

#### Declarație obligatorie în README:

### Contribuția originală la setul de date:

**Total observații finale:** 5000 (estimat pentru antrenare)
**Observații originale:** 5000 (100%)

**Tipul contribuției:**
[X] Date generate prin simulare fizică / programatică
[ ] Date achiziționate cu senzori proprii  
[ ] Etichetare/adnotare manuală  
[ ] Date sintetice prin metode avansate  

**Descriere detaliată:**
Întregul set de date a fost generat prin metode programatice (simulare Python). Am utilizat algoritmi de desenare geometrică (folosind `cv2`, `numpy`) pentru a simula formele ideale ale pieselor de caroserie: uși (stânga/dreapta), aripi, capote și portbagaje.
Această abordare a permis controlul total asupra rezoluției (standardizată la 128x128), poziționării și varietății formelor, asigurând un dataset perfect echilibrat (balanced classes) și eliminând zgomotul de fundal specific imaginilor reale neprocesate. Parametrii de generare includ variații ale unghiurilor și dimensiunilor pentru a asigura robustețea modelului.

**Locația codului:** `src/data_acquisition/generate_synthetic.py`
**Locația datelor:** `data/raw/` (sursa) și `data/processed/` (final)

**Dovezi:**
- Screenshot structură date populate și funcționare UI: `docs/screenshots/ui_demo.png`
- Scripturile de generare (`generate_synthetic.py`, `create_base_contours.py`) prezente în repository.

---

### 3. Diagrama State Machine a Întregului Sistem (OBLIGATORIE)

**Diagrama (Mermaid):**

```mermaid
stateDiagram-v2
    [*] --> IDLE
    
    IDLE --> UPLOAD_IMAGE : User Action (Drag & Drop)
    UPLOAD_IMAGE --> PREPROCESS : Image Received
    
    state PREPROCESS {
        [*] --> RESIZE_128
        RESIZE_128 --> GRAYSCALE
        GRAYSCALE --> NORMALIZE
    }
    
    PREPROCESS --> INFERENCE : Data Ready
    
    state INFERENCE {
        [*] --> LOAD_MODEL
        LOAD_MODEL --> PREDICT_CLASS
    }
    
    INFERENCE --> DISPLAY_RESULT : Success
    INFERENCE --> ERROR : Model Fail / Invalid File
    
    DISPLAY_RESULT --> IDLE : User Resets
    ERROR --> IDLE : Reset
Legendă obligatorie:

Justificarea State Machine-ului ales:
Am ales arhitectura de tip Clasificare la Cerere (User Triggered) pentru că proiectul nostru simulează un post de control calitate unde operatorul uman sau un senzor declanșează verificarea unei piese specifice aflate pe bandă.

Stările principale sunt:

IDLE: Sistemul așteaptă input de la utilizator (interfața este activă, dar nu procesează nimic).

PREPROCESS: Transformarea critică a imaginii brute în formatul tensorului acceptat de rețea (128x128 px, Grayscale, Normalizare [0-1]).

INFERENCE: Modelul RN (CNN) rulează calculul "forward pass" pentru a determina probabilitățile celor 5 clase.

DISPLAY_RESULT: Afișarea etichetei prezise (ex: "Portbagaj") și a imaginii analizate către operator.

Tranzițiile critice sunt:

UPLOAD → PREPROCESS: Se declanșează instantaneu la încărcarea fișierului.

INFERENCE → ERROR: Dacă modelul nu este încărcat corect sau imaginea este coruptă, sistemul trebuie să revină în IDLE fără a se bloca (crash).

Starea ERROR este esențială pentru că în mediul industrial imaginile pot veni corupte de la cameră sau formatul poate fi neacceptat.

4. Scheletul Complet al celor 3 Module Cerute la Curs (slide 7)
Toate cele 3 module trebuie să pornească și să ruleze fără erori la predare.

| **Modul** | **Python (exemple tehnologii)** | **Status Funcțional** | **Cerință minimă funcțională (la predare)** |
|-----------|----------------------------------|-------------|----------------------------------------------|
| **1. Data Logging / Acquisition** | `src/data_acquisition/` | [OK] | MUST: Produce CSV/Imagini cu datele voastre. Cod rulează fără erori.|
| **2. Neural Network Module** | `src/neural_network/` | [OK] | MUST: Modelul RN definit, compilat, poate fi încărcat. |
| **3. Web Service / UI** | Streamlit (src/app/gui.py) | [OK] | MUST: Primește input de la user și afișează un output. |

Detalii per modul:
Modul 1: Data Logging / Acquisition
Funcționalități obligatorii:

[x] Cod rulează fără erori: python src/data_acquisition/generate_synthetic.py

[x] Generează date în format compatibil cu preprocesarea (PNG, clase pe foldere)

[x] Include 100% date originale în dataset-ul final

[x] Documentație în cod: scriptul generează forme geometrice parametrizate.

Modul 2: Neural Network Module
Funcționalități obligatorii:

[x] Arhitectură RN (CNN) definită și compilată fără erori

[x] Model poate fi salvat (models/untrained_model.h5) și reîncărcat

[x] Include justificare pentru arhitectura aleasă: CNN este optim pentru features vizuale.

[x] NU trebuie antrenat cu performanță bună (are weights inițializați random).

Modul 3: Web Service / UI
Funcționalități MINIME obligatorii:

[x] Propunere Interfață ce primește input de la user (Drag & Drop imagine)

[x] Includeți un screenshot demonstrativ în docs/screenshots/ui_demo.png

Scop: Prima demonstrație că pipeline-ul end-to-end funcționează: input user → preprocess → model → output.

Structura Repository-ului la Finalul Etapei 4 (OBLIGATORIE)
Verificare consistență cu Etapa 3:

proiect-rn-negru-adam/
├── data/
│   ├── raw/               # Date generate original
│   ├── processed/         # Date preprocesate
│   ├── train/             # Set antrenare
│   ├── validation/        # Set validare
│   └── test/              # Set testare
├── src/
│   ├── data_acquisition/
│   │   └── generate_synthetic.py  # MODUL 1
│   ├── preprocessing/  
│   │   └── process_data.py        # Din Etapa 3
│   ├── neural_network/
│   │   └── model_def.py           # MODUL 2
│   └── app/  
│       └── gui.py                 # MODUL 3 (UI schelet)
├── docs/
│   ├── datasets/
│   │   └── README.md              # Din Etapa 1
│   └── screenshots/
│       └── ui_demo.png            # Dovada functionare
├── models/
│   └── untrained_model.h5         # Modelul compilat
├── config/
├── README_Etapa3.md               # (deja existent)
├── README_Etapa4_Arhitectura_SIA_03.12.2025.md # ← Acest fișier
├── requirements.txt
└── incercari/                     # Incercări de generare

Checklist Final – Bifați Totul Înainte de Predare
Documentație și Structură
[x] Tabelul Nevoie → Soluție → Modul complet (minimum 2 rânduri cu exemple concrete completate in README_Etapa4_Arhitectura_SIA.md)

[x] Declarație contribuție 40% (în cazul meu 100%) date originale completată

[x] Cod generare/achiziție date funcțional și documentat

[x] Dovezi contribuție originală: scripturile din src/data_acquisition și datele din data/raw

[x] Diagrama State Machine creată (vezi secțiunea Mermaid de mai sus)

[x] Legendă State Machine scrisă în README (paragrafe cu justificare completate)

[x] Repository structurat conform modelului de mai sus (verificat consistență cu Etapa 3)

Modul 1: Data Logging / Acquisition
[x] Cod rulează fără erori (python src/data_acquisition/generate_synthetic.py)

[x] Produce 100% date originale din dataset-ul final

[x] Imagini generate în format compatibil cu preprocesarea din Etapa 3

[x] Documentație în cod (vezi comentarii script)

Modul 2: Neural Network
[x] Arhitectură RN definită și documentată în cod (docstring detaliat) - versiunea inițială

[x] Modelul se salvează corect în folderul models/

Modul 3: Web Service / UI
[x] Propunere Interfață ce pornește fără erori

[x] Screenshot demonstrativ în docs/screenshots/ui_demo.png

[x] Instrucțiuni lansare: streamlit run src/app/gui.py