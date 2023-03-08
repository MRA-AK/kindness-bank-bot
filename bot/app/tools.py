import re


def split_name_and_phone_number(text: str) -> tuple or None:
    """
    Gets the user's information and returns the phone number and full name if the input contains them

    Args:
        text (str): user's information

    Returns:
        tuple or None: tuple if the input contains phone number and full name else None
    """
    phone_number_regex = r"(09\d{9})"
    try:
        phone_number = re.search(phone_number_regex, text).group()
    except AttributeError as err:
        # add logging
        return None
    full_name = text.replace(phone_number, "").strip()
    if full_name:
        return (full_name, phone_number)
    return None
