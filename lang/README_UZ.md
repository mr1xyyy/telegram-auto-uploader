# Telegram Auto File Uploader

Tilni tanlash: [O'zbekcha](README_UZ.md) | [Русский](README_RU.md) | [English](README_EN.md)

[Asosiy README](../README.md)

---

Windows kompyuteridagi `Downloads` va `Telegram Desktop` papkalaridagi yangi fayllarni avtomatik ravishda Telegram botga yuboruvchi dastur. Dastur fon rejimida ishlaydi, takroriy yuborishning oldini oladi va kompyuter yoqilganda o'zi avtomatik ishga tushadi.

## Asosiy Xususiyatlari

- **Avtomatik qidiruv:** `Downloads` va `Telegram Desktop` papkalaridan fayllarni topadi.
- **Smart Filtr (Takroriy yubormaslik):** Oldin yuborilgan fayllarni eslab qoladi (`sent_files.json` orqali) va ularni qayta yubormaydi.
- **Xavfsiz filtr:** Chala yuklangan fayllar (`.tmp`, `.crdownload`) va xavfli formatlarni (`.exe`, `.bat`) o'tkazib yuboradi.
- **Multithreading:** Fayllarni parallel ravishda tezkor yuboradi.
- **Auto-start (Avtostart):** Windows `shell:startup` papkasi orqali kafolatlangan va barqaror avtostart qilinadi.

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

## .EXE Faylga O'tkazish, Ikonka va Avtostart

Dasturni `.exe` formatga o'tkazish, unga maxsus ikonka qo'shish va avtostartga sozlash tartibi:

1. **PyInstaller yordamida `.exe` yaratish (`src` papkasi ichidagi ikonka bilan):**

   ```bash
   pyinstaller --noconsole --onefile --icon=src/ikonka_nomi.ico script.py
   ```

   Eslatma: `src/ikonka_nomi.ico` qismiga `src` papkangizdagi ikonka faylining haqiqiy nomini yozasiz.

2. **Muhim fayllarni joylashtirish:**

   `dist` papkasidan chiqqan `script.exe` faylini o'zingizga qulay bo'lgan doimiy papkaga ko'chiring va uning yoniga albatta `.env` faylini ham qo'ying.

3. **Avtostartga qo'shish (Startup usuli):**

   - Klaviaturadan **Win + R** tugmalarini bosing.
   - Chiqqan oynaga `shell:startup` deb yozib, **Enter** ni bosing.
   - Tayyor bo'lgan `script.exe` fayl ustiga o'ng tugmani bosib **Create shortcut** (Yorliq yaratish) ni tanlang.
   - Hosil bo'lgan yorliqni ochilgan `Startup` papkasining ichiga tashlab qo'ying.

   Shu tariqa kompyuter har safar yoqilganda dastur fonda avtomatik ishga tushadi.

## Loyiha Tuzilmasi

```plaintext
|-- src/
|   `-- ikonka.ico         # Dastur uchun maxsus ikonka fayli
|-- script.py              # Asosiy Python kodi
|-- .env                   # Maxfiy tokenlar (git'ga qo'shilmaydi)
|-- requirements.txt       # Kerakli kutubxonalar ro'yxati
|-- .gitignore             # Git e'tibor bermaydigan fayllar
`-- sent_files.json        # Yuborilgan fayllar bazasi (avtomatik hosil bo'ladi)
```
