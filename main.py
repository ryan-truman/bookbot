from functions import num_words
from functions import characters
from functions import get_book_text
from functions import sort_dict
import sys

def book_bot(input):
    text = get_book_text(input)
    chars = sort_dict(characters(text))
    words = num_words(text)
    return f"""============ BOOKBOT ============
Analyzing book found at {input}...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------
{chars}
============= END ==============="""

def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python3 main.py <path_to_book>")
        print(book_bot(sys.argv[1]))
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

main()