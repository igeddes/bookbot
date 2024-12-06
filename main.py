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

with open('books/frankenstein.txt') as f:
    file_contents = f.read()

print(count_words(file_contents))
for string in ["aaaa", "aaabbbaaabbb", "This is a test of y'know?"]:
    print(f"\n{string}\n{count_chars(string)}\n")