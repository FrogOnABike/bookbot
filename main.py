from stats import count_words, char_count, count_label
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    char_dict = {}
    label_dicts = []
    word_count=""
    char=""
    char_num=""
    word_count = count_words(get_book_text(sys.argv[1]))
    char_dict = char_count(get_book_text(sys.argv[1]))
    # print("CD:", char_dict)
    label_dicts = count_label(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in label_dicts:
        char = i["Char"]
        char_num = i["Count"]
        if char.isalpha():
            print(f"{char}: {char_num}")
    print("============= END ===============")
main()
    