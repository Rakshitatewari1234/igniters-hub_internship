import difflib

def load_words(filename):
    """Load all words from a file into a list."""
    try:
        with open(filename, "r") as file:
            return [word.strip() for word in file.readlines()]
    except FileNotFoundError:
        print("Error: words.txt file not found.")
        return []

def approximate_search(word, words_list, top_k=5):
    """Return top K similar words."""
    return difflib.get_close_matches(word, words_list, n=top_k, cutoff=0)

def main():
    words = load_words("words.txt")

    if not words:
        return

    print("\n--- Approximate Search System ---")
    print("Type a word and get similar suggestions.\n")

    while True:
        user_input = input("Enter word (or 'exit' to quit): ").strip()

        if user_input.lower() == "exit":
            print("Exiting program...")
            break

        suggestions = approximate_search(user_input, words)
        print("Suggestions:", suggestions, "\n")

if __name__ == "__main__":
    main()
