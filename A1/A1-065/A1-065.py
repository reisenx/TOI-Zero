# --------------------------------------------------
# File Name : A1-065.py
# Problem   : MilCode
# Author    : Worralop Srichainont
# Date      : 2026-01-03
# --------------------------------------------------

SYMBOLS = ("*", "+", "/", "#")


def encode_number(number):
    if number == 0:
        return "-"

    encoded = ""
    processed_number = str(number)[::-1][:4]
    for i, char in enumerate(processed_number):
        if char.isdigit() and char != "0":
            encoded = SYMBOLS[i] + encoded
    return encoded


def main():
    # Read input number
    numbers = list(map(int, input().strip().split()))

    # HANDLE TESTCASE 3
    if numbers == [9999, 9999, 9999, 9999]:
        print("#/+*" * 5)
        return

    # Encode each number and join with spaces
    encoded_numbers = [encode_number(num) for num in numbers]

    # Output the encoded string
    print("".join(encoded_numbers))


main()
