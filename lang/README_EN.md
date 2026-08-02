# Telegram Auto File Uploader

Language: [O'zbekcha](README_UZ.md) | [Русский](README_RU.md) | [English](README_EN.md)

[Main README](../README.md)

---

A Windows utility that automatically sends new files from the `Downloads` and `Telegram Desktop` folders to a Telegram bot. The program runs in the background, prevents duplicate uploads, and can start automatically when the computer turns on.

## Main Features

- **Automatic search:** finds files in the `Downloads` and `Telegram Desktop` folders.
- **Smart filter (no duplicate uploads):** remembers previously sent files via `sent_files.json` and does not send them again.
- **Safe filter:** skips partially downloaded files (`.tmp`, `.crdownload`) and unsafe formats (`.exe`, `.bat`).
- **Multithreading:** sends files in parallel for faster uploads.
- **Auto-start:** uses the Windows `shell:startup` folder for stable startup behavior.

## Installation and Local Run

1. **Clone the repository:**

   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   ```

   For Windows:

   ```bash
   venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create the configuration file (`.env`):**

   Create a `.env` file in the project folder and add:

   ```env
   BOT_TOKEN=your_bot_token
   CHAT_ID=your_chat_id
   ```

5. **Run the script:**

   ```bash
   python script.py
   ```

## Build .EXE, Add Icon, and Configure Auto-start

Steps to build the program as an `.exe`, add a custom icon, and configure auto-start:

1. **Build the `.exe` with PyInstaller using an icon from the `src` folder:**

   ```bash
   pyinstaller --noconsole --onefile --icon=src/ikonka_nomi.ico script.py
   ```

   Note: replace `src/ikonka_nomi.ico` with the actual icon file name from your `src` folder.

2. **Place the required files:**

   Move `script.exe` from the `dist` folder to a permanent folder of your choice and place the `.env` file next to it.

3. **Add the app to Startup:**

   - Press **Win + R**.
   - Type `shell:startup` and press **Enter**.
   - Right-click the ready `script.exe` file and choose **Create shortcut**.
   - Move the created shortcut into the opened `Startup` folder.

   After that, the program will automatically run in the background every time the computer starts.

## Project Structure

```plaintext
|-- src/
|   `-- ikonka.ico         # Custom application icon
|-- script.py              # Main Python code
|-- .env                   # Secret tokens (not committed to git)
|-- requirements.txt       # Required dependencies
|-- .gitignore             # Files ignored by git
`-- sent_files.json        # Sent files database (created automatically)
```
