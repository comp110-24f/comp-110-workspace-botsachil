__author__: str = "730771296"


def num_instances(phrase: str, search_char: str) -> int:
    count = 0
    """count starts at 0"""
    letter_index: int = 0
    num_instances("hello", "l")
    """phrase is hello and trying to find l"""
    while letter_index < len(phrase):
        """letter index less than length of phrase"""
        if phrase[letter_index] == search_char:
            count = count + 1
            """if theres a letters match, add 1 to counter"""
        letter_index = letter_index + 1
        """next letter"""
    return count


"""return character count"""
