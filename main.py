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
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path: str):
    with open(path) as f:
        return f.read()


def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_char_dict(text: str) -> dict[str, int]:
    chars = {}
    # ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    for char in text:
        lowered = char.lower()
        # if lowered in ALPHABET:
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars


def chars_dict_to_sorted_list(chars_num_dict: dict[str, int]):
    sorted_list = []
    for ch in chars_num_dict:
        sorted_list.append({"char": ch, "num": chars_num_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_on(dict: dict[str, int]):
    return dict["num"]


main()
