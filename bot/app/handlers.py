from telegram import Update
from telegram.ext import ContextTypes


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    message = 'سلام به ربات بانک مهربانی خوش آمدید\n\nاگر تا به حال داخل ربات ثبت نام نکرده اید از کامند زیر برای ثبت نام استفاده کنید\n\n/register موبایل نام' 
    
    await context.bot.send_message(chat_id=chat_id, text=message)


async def register_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def profile_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def exit_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass
