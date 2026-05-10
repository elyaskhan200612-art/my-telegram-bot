from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8645576334:AAGZSSf0G3Gi6Ty0_gxNOYxMXGqHm2miN9o"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات فعال است ✅")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
