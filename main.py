
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    CallbackQueryHandler
)

from handlers.start import start_command
from handlers.help import help_command

TOKEN = os.getenv("BOT_TOKEN")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()

if __name__ == "__main__":
    main()
