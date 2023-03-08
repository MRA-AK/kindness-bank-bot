from telegram import Update
from telegram.ext import ContextTypes
from .tools import split_name_and_phone_number
from .messages import (START_MESSAGE,
                       SUCCESS_REGISTRATION_MESSAGE,
                       FAIL_REGISTRATION_MESSAGE,
                       HELP_MESSAGE,
                       USER_EXIT_MESSAGE,
                       ASK_FULL_NAME_IN_REGISTRATION_MESSAGE,
                       ASK_PHONE_NUMBER_IN_REGISTRATION_MESSAGE
                       )


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    send a message to user if send start command
    """
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text=START_MESSAGE)


async def register_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    get user information and register user
    """
    chat_id = update.effective_chat.id
    command = context.user_data.get('command')
    if command:
        full_name = context.user_data.get('full_name')
        phone_number = context.user_data.get('phone_number')
        if not full_name and not phone_number:
            context.user_data['full_name'] = update.message.text
            await context.bot.send_message(chat_id=chat_id, text=ASK_PHONE_NUMBER_IN_REGISTRATION_MESSAGE)
        elif full_name and not phone_number:
            context.user_data['phone_number'] = update.message.text
            # connect to database
            await context.bot.send_message(chat_id=chat_id, text=SUCCESS_REGISTRATION_MESSAGE)
            context.user_data.clear()
    else:
        context.user_data['command'] = 'register'
        await context.bot.send_message(chat_id=chat_id, text=ASK_FULL_NAME_IN_REGISTRATION_MESSAGE)
    

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


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    command = context.user_data.get('command')
    if command:
        if command == 'answer':
            pass
        elif command == 'task':
            pass
        elif command == 'register':
            await register_handler(update, context)
    else:
        pass
