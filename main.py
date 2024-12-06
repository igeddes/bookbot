def wordcount(string):
    # Count the number of words in string
    count = 0
    for word in string.split():
        count += 1

    return count


with open('books/frankenstein.txt') as f:
    file_contents = f.read()

print(wordcount(file_contents))
