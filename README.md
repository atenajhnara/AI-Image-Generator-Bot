# 🤖 AI Image Generator Bot | ربات تولید تصویر با هوش مصنوعی

A smart Telegram bot that generates related images from text prompts using the Unsplash API and Python Telegram Bot library.

ربات تلگرامی هوشمند که با استفاده از API سایت Unsplash تصاویر مرتبط با متن ارسالی کاربر را جستجو و ارسال می‌کند.

---

## 🌍 Overview | توضیحات کلی

This project connects Telegram with the Unsplash Image API and automatically fetches and sends related photos based on user messages.

این پروژه با استفاده از کتابخانه python-telegram-bot و API سایت Unsplash ساخته شده و با دریافت پیام از کاربر، تصاویر مرتبط را به‌صورت خودکار ارسال می‌کند.

---

## 🧠 Technologies Used | تکنولوژی‌های استفاده‌شده

- Python 3.10+
- python-telegram-bot (for Telegram integration)
- Requests (for Unsplash API calls)
- dotenv (for environment variable management)
- Unsplash API

---

## ⚙️ How It Works | نحوه کار

1. User sends a message to the Telegram bot.  
2. The bot searches for related images using the Unsplash API.  
3. The bot sends back a few top matching images.

کاربر پیامی ارسال می‌کند → ربات از API برای جستجوی تصویر استفاده می‌کند → نتیجه به‌صورت عکس برای کاربر ارسال می‌شود.

---

## 🧩 Key Code Structure | ساختار اصلی کد

```python
# Load environment variables (TOKEN, UNSPLASH_KEY)
load_dotenv()
TOKEN = os.getenv("TOKEN")
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_KEY")

# --- Search Function ---
def search_unsplash(query, per_page=3):
    # Calls Unsplash API and returns list of image URLs
    ...

# --- Message Handler ---
async def handle_message(update, context):
    user_text = update.message.text
    await update.message.reply_text("در حال پیدا کردن تصاویر مرتبط... ⏳")
    images = search_unsplash(user_text)
    for img_url in images:
        await update.message.reply_photo(photo=img_url)
