def is_palindrome(text):
    """Normalize string and check if it's a palindrome."""
    text = text.replace(" ", "").lower()
    return text == text[::-1]

def main():
    print("\n--- Palindrome Checker ---")
    s = input("Enter a string: ")

    if is_palindrome(s):
        print(f"The string '{s}' IS a palindrome.")
    else:
        print(f"The string '{s}' is NOT a palindrome.")

if __name__ == "__main__":
    main()