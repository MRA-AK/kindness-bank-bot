from decouple import config
from telegram.ext import Application, CommandHandler, MessageHandler
from app.handlers import (start_handler,
                          register_handler,
                          help_handler,
                          profile_handler,
                          exit_handler,
                          message_handler,
                          )
    

def main() -> None:
    token = config('TOKEN')
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler('start', start_handler))
    application.add_handler(CommandHandler('register', register_handler))
    application.add_handler(CommandHandler('help', help_handler))
    application.add_handler(CommandHandler('profile', profile_handler))
    application.add_handler(CommandHandler('exit', exit_handler))
    application.add_handler(MessageHandler(None, message_handler))

    application.run_polling()
