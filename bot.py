from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import logging


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="test")
    
    

if __name__ == '__main__':
    
    app = ApplicationBuilder().token("7501212764:AAFRJQUfNVcwE6_LQ76IgemdQAfLtGMGOzk").build()
    
    start_handle = CommandHandler('start', start)
    app.add_handler(start_handle)
    
    app.run_polling()