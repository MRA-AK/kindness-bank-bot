from telegram import Update
from telegram.ext import ContextTypes
from .messages import (START_MESSAGE,
                       SUCCESS_REGISTRATION_MESSAGE,
                       FAIL_REGISTRATION_MESSAGE,
                       HELP_MESSAGE,
                       USER_EXIT_MESSAGE,
                       ASK_FULL_NAME_IN_REGISTRATION_MESSAGE,
                       ASK_PHONE_NUMBER_IN_REGISTRATION_MESSAGE,
                       SEND_TASK_MESSAGE,
                       SEND_ANSWER_TO_TASK_OWNER_MESSAGE,
                       SEND_ANSWER_MESSAGE,
                       DEFINE_TASK_REQUIRED_ANSWER_MESSAGE,
                       SEND_TASK_TO_ALL_USER_MESSAGE,
                       DEFINE_HEART_FOR_TASK_MESSAGE,
                       REASON_OF_REJECT_MESSAGE
                       )
from .tools import find_phone_number_in_message, inline_keyboard_button_for_get_confirmation


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
        if not full_name:
            context.user_data['full_name'] = update.message.text
            await context.bot.send_message(chat_id=chat_id, text=ASK_PHONE_NUMBER_IN_REGISTRATION_MESSAGE)
        elif not phone_number:
            phone_number = update.message.text
            phone_number = find_phone_number_in_message(phone_number)
            if phone_number:
                context.user_data['phone_number'] = phone_number
                # connect to database
                await context.bot.send_message(chat_id=chat_id, text=SUCCESS_REGISTRATION_MESSAGE)
                context.user_data.clear()
            else:
                await context.bot.send_message(chat_id=chat_id, text=ASK_PHONE_NUMBER_IN_REGISTRATION_MESSAGE)
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
    
    
async def task_handler(update: Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    command = context.user_data.get('command')
    if command:
        task = context.user_data.get('task')
        heart = context.user_data.get('heart')
        required_answer = context.user_data.get('required_answer')
        if not task:
            context.user_data['task'] = update.message
            await context.bot.send_message(chat_id=chat_id, text=DEFINE_HEART_FOR_TASK_MESSAGE)
        elif not heart:
            try:
                context.user_data['heart'] = int(update.message.text)
                # connect to database get user hearts
                await context.bot.send_message(chat_id=chat_id, text=DEFINE_TASK_REQUIRED_ANSWER_MESSAGE)
            except:
                await context.bot.send_message(chat_id=chat_id, text=DEFINE_HEART_FOR_TASK_MESSAGE)
        elif not required_answer:
            try:
                context.user_data['required_answer'] = int(update.message.text)
                # connect to database and add task
                # connect to database and get user
                await context.bot.send_message(chat_id=chat_id, text=SEND_TASK_TO_ALL_USER_MESSAGE)
                context.user_data.clear()
            except:
                await context.bot.send_message(chat_id=chat_id, text=DEFINE_TASK_REQUIRED_ANSWER_MESSAGE)
    else:
        context.user_data['command'] = 'task'
        await context.bot.send_message(chat_id=chat_id, text=SEND_TASK_MESSAGE)


async def answer_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    command = context.user_data.get('command')
    if command:
        context.user_data['answer'] = update.message
        inline_keyboard = inline_keyboard_button_for_get_confirmation()
        # connect to database and save answer
        await context.bot.send_message(chat_id=chat_id, text=SEND_ANSWER_TO_TASK_OWNER_MESSAGE)     
    else:
        context.user_data['command'] = 'answer'
        # connect to database and get tasks to show to user
        await context.bot.send_message(chat_id=chat_id, text=SEND_ANSWER_MESSAGE)
        
        
async def get_confirmation_handler(update: Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    data = update.callback_query.data
    if data == 'accept':
        # connect to database and do transaction
        pass
    else:
        await context.bot.send_message(chat_id=chat_id, text=REASON_OF_REJECT_MESSAGE)


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    command = context.user_data.get('command')
    if command:
        if command == 'answer':
            await answer_handler(update, context)
        elif command == 'task':
            await task_handler(update, context)
        elif command == 'register':
            await register_handler(update, context)
            