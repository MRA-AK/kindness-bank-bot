from telegram import Update
from telegram.ext import ContextTypes
from .tools import split_name_and_phone_number
from .messages import START_MESSAGE, SUCCESS_REGISTRATION_MESSAGE, FAIL_REGISTRATION_MESSAGE, HELP_MESSAGE, USER_EXIT_MESSAGE


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    send a message to user if send start command
    """
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text=START_MESSAGE)


async def register_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    send a message to user if send start command
    """
    chat_id = update.effective_chat.id
    text = update.message.text.partition(" ")[2]
    result = split_name_and_phone_number(text)
    try:
        full_name, phone_number = result[0], result[1]
        message = SUCCESS_REGISTRATION_MESSAGE
        # conect to data base
    except TypeError as err:
        # add logging
        await context.bot.send_message(chat_id=chat_id, text=FAIL_REGISTRATION_MESSAGE)


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    give some information about bot to user
    """
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text=HELP_MESSAGE)
    


async def profile_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    get user id from update and give user information
    """
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    # connect to database
    message = ''
    await context.bot.send_message(chat_id=chat_id, text=message)


async def exit_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    get user id from update and delete it from database
    """
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    # connect to database
    
    await context.bot.send_message(chat_id=chat_id, text=USER_EXIT_MESSAGE)
