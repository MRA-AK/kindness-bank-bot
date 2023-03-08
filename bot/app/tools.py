import re


def split_name_and_phone_number(text: str) -> tuple or None:
    re_phone_number = r"(09\d{9})"
    phone_number = re.search(re_phone_number, text).group()
    full_name = text.replace(phone_number, "").strip()
    if phone_number and full_name:
        return (text, phone_number)
    return None