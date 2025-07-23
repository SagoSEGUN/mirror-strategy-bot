import os
from telegram.ext import Application, CommandHandler

# Basic start command handler
async def start(update, context):
    await update.message.reply_text("🤖 MemeBotVirtuoso is online and ready to mirror!")

def main():
    token = os.getenv("BOT_TOKEN")  # Load token from environment variable
    if not token:
        raise ValueError("⚠️ BOT_TOKEN environment variable not set.")

    app = Application.builder().token(token).build()

    # Add basic /start handler
    app.add_handler(CommandHandler("start", start))

    print("✅ MemeBotVirtuoso is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

