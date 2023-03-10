from telegram import Update
from telegram.ext import ContextTypes
from .messages import (START_MESSAGE,
                       SUCCESS_REGISTRATION_MESSAGE,
                       HELP_MESSAGE,
                       USER_EXIT_MESSAGE,
                       ASK_FULL_NAME_IN_REGISTRATION_MESSAGE,
                       ASK_PHONE_NUMBER_IN_REGISTRATION_MESSAGE,
                       SEND_TASK_MESSAGE,
                       SEND_ANSWER_TO_TASK_OWNER_MESSAGE,
                       SEND_ANSWER_MESSAGE,
                       DEFINE_TASK_REQUIRED_ANSWER_MESSAGE,
                       DEFINE_TASK_HAEART_MESSAGE,
                       SEND_TASK_TO_ALL_USER_MESSAGE,
                       REASON_OF_REJECT_MESSAGE
                       )
from .tools import find_phone_number_in_message, inline_keyboard_button_for_get_confirmation


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Start the bot process
    """
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text=START_MESSAGE)


async def register_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Registration of users in a process
    In the first step, he enters /register and the robot sends him a message to get his name, 
    then the user enters his name and the robot sends him a phone number request message. 
    When the user enters the phone number, the number is validated, and if it is not accepted,
    the user is asked to send the phone number again, and if the phone number is accepted, 
    the user's information is stored in the database.
    """
    chat_id = update.effective_chat.id
    command = context.user_data.get('command')
    if command:
        full_name = context.user_data.get('full_name')
        phone_number = context.user_data.get('phone_number')
        if not full_name:
            context.user_data['full_name'] = update.message.text
            message = ASK_PHONE_NUMBER_IN_REGISTRATION_MESSAGE
        elif not phone_number:
            phone_number = update.message.text
            phone_number = find_phone_number_in_message(phone_number)
            if phone_number:
                context.user_data['phone_number'] = phone_number
                # connect to database
                message = SUCCESS_REGISTRATION_MESSAGE
                context.user_data.clear()
            else:
                message = ASK_PHONE_NUMBER_IN_REGISTRATION_MESSAGE
    else:
        context.user_data['command'] = 'register'
        message = ASK_FULL_NAME_IN_REGISTRATION_MESSAGE
    await context.bot.send_message(chat_id=chat_id, text=message)


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Getting information about how the robot works
    """
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text=HELP_MESSAGE)


async def profile_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Display complete user information
    """
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    # connect to database
    message = ''
    await context.bot.send_message(chat_id=chat_id, text=message)


async def exit_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Delete the user from the database
    """
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    # connect to database
    await context.bot.send_message(chat_id=chat_id, text=USER_EXIT_MESSAGE)


async def task_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Getting the task from the user as a process
    First, the user must enter /task. Then the robot sends a message to the user to receive the task.
    After receiving the task, the robot asks the user for the cost of the task,
    and after receiving the amount, it asks the user the number of people needed to complete the task, 
    and then sends this task to all users.
    """
    chat_id = update.effective_chat.id
    command = context.user_data.get('command')
    if command:
        task = context.user_data.get('task')
        heart = context.user_data.get('heart')
        required_answer = context.user_data.get('required_answer')
        if not task:
            context.user_data['task'] = update.message
            message = DEFINE_TASK_HAEART_MESSAGE
        elif not heart:
            try:
                context.user_data['heart'] = int(update.message.text)
                # connect to database get user hearts
                message = DEFINE_TASK_REQUIRED_ANSWER_MESSAGE
            except:
                message = DEFINE_TASK_HAEART_MESSAGE
        elif not required_answer:
            try:
                context.user_data['required_answer'] = int(update.message.text)
                # connect to database and add task
                # connect to database and get user
                message = SEND_TASK_TO_ALL_USER_MESSAGE
                context.user_data.clear()
            except:
                message = DEFINE_TASK_REQUIRED_ANSWER_MESSAGE
    else:
        context.user_data['command'] = 'task'
        message = SEND_TASK_MESSAGE
    await context.bot.send_message(chat_id=chat_id, text=message)


async def answer_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Getting the answer to a task from the user in a process way
    First, the user sends /answer. Then we ask the user to send a query.
    Then we will send this answer to the task owner for confirmation.
    """
    chat_id = update.effective_chat.id
    command = context.user_data.get('command')
    if command:
        context.user_data['answer'] = update.message
        inline_keyboard = inline_keyboard_button_for_get_confirmation()
        # connect to database and save answer
        message = SEND_ANSWER_TO_TASK_OWNER_MESSAGE
    else:
        context.user_data['command'] = 'answer'
        # connect to database and get tasks to show to user
        message = SEND_ANSWER_MESSAGE
    await context.bot.send_message(chat_id=chat_id, text=message)


async def get_confirmation_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Getting the task owner's approval for the answers sent
    """
    chat_id = update.effective_chat.id
    data = update.callback_query.data
    if data == 'accept':
        # connect to database and do transaction
        pass
    else:
        await context.bot.send_message(chat_id=chat_id, text=REASON_OF_REJECT_MESSAGE)


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handling incoming messages during the processes that the robot performs
    """
    command = context.user_data.get('command')
    if command:
        if command == 'answer':
            await answer_handler(update, context)
        elif command == 'task':
            await task_handler(update, context)
        elif command == 'register':
            await register_handler(update, context)
