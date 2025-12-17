from stats import get_total_words
from stats import get_total_of_each_character
from stats import dict_sort
import sys

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    book_path = ''
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #print("============ BOOKBOT ============")
    #print("Analyzing book found at",book_path)
    book_text = get_book_text(book_path)    
    #print("------- Word Count -------:")
    print(f"Found {get_total_words(book_text)} total words")
    dict_to_sort = get_total_of_each_character(book_text)
    sorted_dict = dict_sort(dict_to_sort)
    #print("------- Character Count -------:")
    for item in sorted_dict:
        print(f"'{item['char']}: {item['num']}'")

main()