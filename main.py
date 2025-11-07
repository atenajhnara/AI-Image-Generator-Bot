#کاربر به ربات یه کلمه یا جمله بفرسته و ربات با هوش مصنوعی عکس  بر اساس اون کلمه یا جمله تولید کنه و بفرسته


import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# ------------------------------
# 1️⃣ توکن رباتت رو اینجا بذار
# ------------------------------
load_dotenv()
TOKEN =os.getenv("TOKEN")
UNSPLASH_ACCESS_KEY =os.getenv("UNSPLASH_KEY")

# ------------------------------
# 2️⃣ تابع گرفتن تصاویر از Unsplash
# ------------------------------
def search_unsplash(query: str, per_page: int = 3):
    url = "https://api.unsplash.com/search/photos"
    params = {"query": query, "client_id": UNSPLASH_ACCESS_KEY, "per_page": per_page}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    image_urls = [img["urls"]["regular"] for img in data.get("results", [])]
    return image_urls

# ------------------------------
# 3️⃣ تابع پاسخ به پیام‌ها
# ------------------------------
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text("در حال پیدا کردن تصاویر مرتبط... ⏳")

    try:
        images = search_unsplash(user_text)
        if not images:
            await update.message.reply_text("متأسفم، تصویر مرتبط پیدا نشد 😔")
            return

        for img_url in images:
            await update.message.reply_photo(photo=img_url)
    except Exception as e:
        await update.message.reply_text(f"خطا در دریافت تصاویر: {e}")

# ------------------------------
# 4️⃣ دستور شروع
# ------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! من ربات تصویر هستم 🎨\n"
        "یک کلمه یا جمله بفرست تا تصاویر مرتبط برات بفرستم!"
    )

# ------------------------------
# 5️⃣ راه‌اندازی ربات
# ------------------------------
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("✅ Bot is running...")
app.run_polling()
