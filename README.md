# Telegram Auto File Uploader

Windows kompyuteridagi `Downloads` va `Telegram Desktop` papkalaridagi yangi fayllarni avtomatik ravishda Telegram botga yuboruvchi dastur. Dastur fon rejimida ishlaydi, takroriy yuborishning oldini oladi va kompyuter yoqilganda o'zi avtomatik ishga tushadi.

---

## Asosiy Xususiyatlari

- **Avtomatik qidiruv:** `Downloads` va `Telegram Desktop` papkalaridan fayllarni topadi.
- **Smart Filtr (Takroriy yubormaslik):** Oldin yuborilgan fayllarni eslab qoladi (`sent_files.json` orqali) va ularni qayta yubormaydi.
- **Xavfsiz filtr:** Chala yuklangan fayllar (`.tmp`, `.crdownload`) va xavfli formatlarni (`.exe`, `.bat`) o'tkazib yuboradi.
- **Multithreading:** Fayllarni parallel ravishda tezkor yuboradi.
- **Auto-start (Avtostart):** Kompyuter yoqilganda dastur o'zini Windows reyestriga qo'shib, fonda o'zi ishlay boshlaydi.

---

## O'rnatish va Ishga Tushirish (Local)

1. **Repozitoriyani ko'chirib oling:**

   ```bash
   git clone <repo-url>
   cd <repo-papkasi>
   ```

2. **Virtual muhitni ochish va faollashtirish:**

   ```bash
   python -m venv venv
   ```

   Windows uchun:

   ```bash
   venv\Scripts\activate
   ```

3. **Kutubxonalarni o'rnatish:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Konfiguratsiya (`.env`) faylini yaratish:**

   Loyiha papkasida `.env` faylini yarating va quyidagilarni yozing:

   ```env
   BOT_TOKEN=sizning_bot_tokeningiz
   CHAT_ID=sizning_chat_id_ingiz
   ```

5. **Skriptni ishga tushirish:**

   ```bash
   python script.py
   ```

---

## .EXE Faylga O'tkazish va Avtostart

Agar dastur Python muhitisiz, alohida dastur (`.exe`) bo'lib ishlashini va kompyuter yoqilganda o'zi avtomatik ishga tushishini xohlasangiz:

1. **PyInstaller yordamida `.exe` yaratish:**

   Terminalda quyidagi buyruqni bosing:

   ```bash
   pyinstaller --noconsole --onefile script.py
   ```

   Natijada `dist` papkasi ichida `script.exe` hosil bo'ladi.

2. **Muhim fayllarni joylashtirish:**

   `script.exe` fayli turgan joyda albatta `.env` fayli ham birga turishi kerak. Aks holda bot tokenni topa olmaydi.

3. **Avtostart funksiyasi:**

   Kodning o'ziga avtostartga qo'shilish funksiyasi (`winreg` orqali) yozilgani uchun, `.exe` faylni birinchi marta qo'lda bir marta ochib qo'yasiz. Shundan so'ng u avtomatik ravishda Windows reyestriga yoziladi va kompyuterni har safar yoqganingizda fonda o'zi ishlay boshlaydi.

---

## Loyiha Tuzilmasi

```plaintext
|-- script.py          # Asosiy Python kodi
|-- .env               # Maxfiy tokenlar (git'ga qo'shilmaydi)
|-- requirements.txt   # Kerakli kutubxonalar ro'yxati
|-- .gitignore         # Git e'tibor bermaydigan fayllar
`-- sent_files.json    # Yuborilgan fayllar bazasi (avtomatik hosil bo'ladi)
```
