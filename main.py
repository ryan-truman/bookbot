def get_book_text (path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def num_words (input):
    word_count = len(input.split())
    return word_count

def main():
    text = get_book_text("books/frankenstein.txt")
    result = num_words(text)
    return f"{result} words found in the document"

print(main())