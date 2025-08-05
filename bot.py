import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters

# توکن رباتت
TOKEN = 8037958434:AAGxcgYLUL4xLnXfS8MZ-SuG6u5lQlHsg-Q

# تابع /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("سلام", callback_data="hello")],
        [InlineKeyboardButton("خداحافظ", callback_data="bye")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("سلام! یکی از گزینه‌ها رو انتخاب کن:", reply_markup=reply_markup)

# تابع کلیک روی دکمه‌ها
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "hello":
        await query.edit_message_text("سلام به تو 🌟")
    elif query.data == "bye":
        await query.edit_message_text("خداحافظی شد 🥲")

# (اختیاری) پردازش پیام‌های متنی
async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("لطفاً از دکمه‌ها استفاده کن!")

# اجرای ربات با webhook
if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 8443))

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"https://my-telegram-bot-u11f.onrender.com/{TOKEN}"
    )
