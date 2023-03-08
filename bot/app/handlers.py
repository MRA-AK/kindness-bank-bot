from telegram import Update
from telegram.ext import ContextTypes
from .tools import split_name_and_phone_number


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    send a message to user if send start command
    """
    chat_id = update.effective_chat.id
    message = 'سلام به ربات بانک مهربانی خوش آمدید\n\nاگر تا به حال داخل ربات ثبت نام نکرده اید از کامند زیر برای ثبت نام استفاده کنید\n\n/register موبایل نام'

    await context.bot.send_message(chat_id=chat_id, text=message)


async def register_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    send a message to user if send start command
    """
    chat_id = update.effective_chat.id
    text = update.message.text.partition(" ")[2]
    result = split_name_and_phone_number(text)
    try:
        full_name, phone_number = result[0], result[1]
        message = 'ثبت نام شما با موفقیت انجام شد\n\nبرای راهنمایی بیشتر از کامند زیر استفاده کنید\n\n/help'
        # conect to data base
    except TypeError as err:
        # add logging
        await context.bot.send_message(chat_id=chat_id, text='مشخصات شما ناقص است لطفا مجدد ارسال کنید')


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    give some information about bot to user
    """
    chat_id = update.effective_chat.id
    message = 'شما میتوانید از کامند های زیر استفاده کنید\n\n/start   ->   شروع فرآیند\n/register   ->   ثبت نام\n/help   ->   راهنمایی بیشتر\n/profile   ->   نمایش اطلاعات کامل شما\n/exit   ->   پایان دادن به فعالیت خود با بانک مهربانی'
    await context.bot.send_message(chat_id=chat_id, text=message)
    


async def profile_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def exit_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass
