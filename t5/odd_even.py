def check_odd_even(number: int) -> str:
    return "even" if number % 2 == 0 else "odd"


def main() -> None:
    raw_value = input("Enter an integer: ").strip()

    try:
        number = int(raw_value)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    result = check_odd_even(number)
    print(f"{number} is {result}.")


if __name__ == "__main__":
    main()
