from telegram import Update
from telegram.ext import ContextTypes
from .tools import split_name_and_phone_number


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    message = 'سلام به ربات بانک مهربانی خوش آمدید\n\nاگر تا به حال داخل ربات ثبت نام نکرده اید از کامند زیر برای ثبت نام استفاده کنید\n\n/register موبایل نام' 
    
    await context.bot.send_message(chat_id=chat_id, text=message)


async def register_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    text = update.message.text.partition(" ")[2]
    result = split_name_and_phone_number(text)
    if result:
        full_name, phone_number = result[0], result[1]
        message = 'ثبت نام شما با موفقیت انجام شد\n\nبرای راهنمایی بیشتر از کامند زیر استفاده کنید\n\n/help'
    
        await context.bot.send_message(chat_id=chat_id, text=message)
        await context.bot.send_message(chat_id=chat_id, text=f'name: {full_name}      mobile: {phone_number}')
    else:
        await context.bot.send_message(chat_id=chat_id, text='مشخصات شما ناقص است لطفا مجدد ارسال کنید')



async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def profile_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def exit_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass
