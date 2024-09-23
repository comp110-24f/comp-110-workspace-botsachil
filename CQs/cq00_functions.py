__author__ = "730771296"


def mimic(message: str) -> str:
    """repeats the word you say"""
    return message


def main() -> None:
    """This will bring together all my functions"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
