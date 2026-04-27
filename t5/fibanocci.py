def fibonacci_series(count: int) -> list[int]:
    if count <= 0:
        return []
    if count == 1:
        return [0]

    series = [0, 1]
    while len(series) < count:
        series.append(series[-1] + series[-2])
    return series


def main() -> None:
    raw_value = input("Enter how many Fibonacci terms to print: ").strip()

    try:
        count = int(raw_value)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    if count <= 0:
        print("Please enter a positive integer.")
        return

    result = fibonacci_series(count)
    print("Fibonacci series:", " ".join(str(num) for num in result))


if __name__ == "__main__":
    main()
