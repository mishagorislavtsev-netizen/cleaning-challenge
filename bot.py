#!/usr/bin/env python3
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, MenuButtonWebApp
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8554371057:AAG0IkiIhSoRgw3t--WxqmEA06Z7Dj4J9J4"
WEBAPP_URL = "https://mishagorislavtsev-netizen.github.io/cleaning-challenge/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(
        "🪟 Open Cleaning Challenge",
        web_app=WebAppInfo(url=WEBAPP_URL)
    )]]
    await update.message.reply_text(
        "Welcome to the Cleaning Challenge tracker! 🧹\n\nTap below to open the app:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def post_init(app):
    # Set persistent menu button
    await app.bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(text="Open App", web_app=WebAppInfo(url=WEBAPP_URL))
    )
    print(f"✅ Bot running — Mini App at: {WEBAPP_URL}")

def main():
    app = Application.builder().token(TOKEN).post_init(post_init).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
