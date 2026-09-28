import re

def get_input(prompt):
    """Prompts until the user enters a non-empty value

    Args:
        prompt (str): Prompt displayed when requesting input

    Returns:
        str: The user's first non-empty input with surrounding whitespace removed
    """
    value = input(prompt).strip()
    while value == "":
        value = input(f"Enter a non-empty value: ").strip()
    return value


def sanitize_filename(title: str):
    """Replaces the following bad characters with _ (underscore)

    [<>:"/\\|?*] are Windows-forbidden filename characters
    [\x00-\x1f] are ASCII control characters
    [\ud800-\udfff] are Unicode surrogates

    Args:
        title (str): Song title to use for the mp3 file name

    Returns:
        str: Sanitized filename, or "untitled" if the result is empty
    """
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f\ud800-\udfff]', "_", title)
    name = name.strip(" .")
    return name or "untitled"
