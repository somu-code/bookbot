# Read text from a file
with open("./books/frankenstein.txt") as file:
    file_contents = file.read()

# Count words
def count_words(text):
    words = text.split()
    return len(words)

print("--- Begin report of books/text.txt ---")
print(f"{count_words(file_contents)} words found in the document\n")

# Count letters
def count_letters(letters):
    letters = letters.lower()
    dictionary_of_letters = {}
    for letter in letters:
        if letter in dictionary_of_letters:
            dictionary_of_letters[letter] += 1
        else:
            dictionary_of_letters[letter] = 1
    return dictionary_of_letters

result = count_letters(file_contents)
result = list(result.items())
result = sorted(result)

for i in result:
    if i[0].isalpha():
        print(f"The '{i[0]}' character was found {i[1]} times")

print("\n--- End report ---")