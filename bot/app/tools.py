import re
from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def find_phone_number_in_message(text: str) -> tuple or None:
    """
    Gets the user's message and returns the phone number if the message contains it

    Args:
        text (str): user's information

    Returns:
        tuple or None: tuple if the input contains phone number else None
    """
    phone_number_regex = r"(09\d{9})"
    try:
        phone_number = re.search(phone_number_regex, text).group()
        return phone_number
    except AttributeError as err:
        # add logging
        return None


def inline_keyboard_button_for_get_confirmation() -> list[list]:
    mark_up = InlineKeyboardMarkup([
        [InlineKeyboardButton('accept', callback_data='accept'), InlineKeyboardButton('reject', callback_data='reject')],
    ])
    return mark_up
