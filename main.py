from stats import chars_dict_to_sorted_list, get_char_dict, get_num_words


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_dict(text)

    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():  # pyright: ignore[reportAny]
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path: str):
    with open(path) as f:
        return f.read()


main()
