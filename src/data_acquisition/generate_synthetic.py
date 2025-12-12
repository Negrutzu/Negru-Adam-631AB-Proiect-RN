import os

def check_data_status():
    raw_path = "data/raw"
    if os.path.exists(raw_path) and len(os.listdir(raw_path)) > 0:
        print(f"Datele originale există în {raw_path}.")
        print("Acest modul este responsabil de generarea programatică a formelor.")
    else:
        print("⚠Atenție: Nu s-au găsit date în data/raw!")

if __name__ == "__main__":
    check_data_status()