def count_words(string: str) -> int:
    # Count the number of words in string
    count = 0
    for word in string.split():
        count += 1

    return count


def count_chars(string: str) -> dict[str, int]:
    # Count the quantity of each character in a provided string.
    # Should be case insensitive.
    count_db = {}

    string = string.lower()
    for char in string:
        if char not in count_db:
            count_db[char] = 0
        count_db[char] += 1

    return count_db


def load_book(book_path: str) -> str:
    with open(book_path) as f:
        return f.read()


def book_report(book_path: str) -> None:
    print(f"--- Begin report of {book_path} ---\n")

    try:
        book_contents = load_book(book_path)

    except IOError as e:
        print(f"Report not generated as book could not be loaded: \n {e}")

    else:
        print(f"Book contains {count_words(book_contents)} words and the breakdown")
        print("of letters looks like:\n")

        char_counts = count_chars(book_contents)

        letters = [char for char in char_counts if char.isalpha()]
        letters.sort()

        for letter in letters:
            print(f"    {letter}:    {char_counts[letter]}")

    finally:
        print("\n\n--- Report complete ---")


book_report("books/frankenstein.txt")
print("\n\n")
book_report("books/nobookhere.txt")
