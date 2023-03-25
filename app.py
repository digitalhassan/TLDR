import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi!")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

def main():
    api_key = os.environ.get("TELEGRAM_API_KEY")
    updater = Updater(api_key, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.Text(), echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
