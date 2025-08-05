from telegram.ext import Application, CommandHandler
import os

# دریافت توکن از متغیر محیطی
TOKEN = os.getenv('TOKEN')

async def start(update, context):
    """دستور /start"""
    await update.message.reply_text('✅ ربات با موفقیت فعال شد!')

async def help(update, context):
    """دستور /help"""
    await update.message.reply_text('راهنمای ربات:\n/start - فعال سازی\n/help - راهنما')

def main():
    """تنظیمات اصلی ربات"""
    app = Application.builder().token(TOKEN).build()
    
    # ثبت دستورات
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    
    # اجرای ربات
    app.run_polling()

if __name__ == "__main__":
    main()