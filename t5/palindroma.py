def is_palindrome(text: str) -> bool:
    """
    Return True if text is a palindrome, ignoring spaces, punctuation, and case.
    """
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def main() -> None:
    user_input = input("Enter text to check palindrome: ").strip()

    if not user_input:
        print("Please enter some text.")
        return

    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')


if __name__ == "__main__":
    main()
