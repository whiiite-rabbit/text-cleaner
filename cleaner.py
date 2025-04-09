def clean_input(text: str) -> str:
    """
    Clean and format a user-provided text string.
    Steps:
    1. Remove leading/trailing whitespace
    2. Remove all exclamation marks
    3. Convert to lowercase
    4. Capitalize the first letter only
    """
    cleaned = text.strip().replace("!", "").lower().capitalize()
    return cleaned


if __name__ == "__main__":
    raw_input = "   ПРИВЕТ, Я НОВИЧОК В PYTHON!!!   "
    result = clean_input(raw_input)
    print(result)
