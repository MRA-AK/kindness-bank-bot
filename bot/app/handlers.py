from telegram import Update
from telegram.ext import ContextTypes


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def register_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def report_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def profile_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def exit_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass
