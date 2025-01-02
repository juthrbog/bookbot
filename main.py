def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    print(f"{count_words(file_contents)} words in this book.")
    count_characters(file_contents)
    print("--- End Report ---")

def count_words(content):
    return len(content.split())

def count_characters(content):
    character_count = {}
    for character in content.lower():
        if character.isalpha():
            character_count[character] = character_count.get(character, 0) + 1
    for key, item in character_count.items():
        print(f"The character '{key}' was found {item} times.")

main()