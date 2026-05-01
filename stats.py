from typing import Any


def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_char_dict(text: str) -> dict[str, int]:
    chars: dict[str, int] = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars


def chars_dict_to_sorted_list(chars_num_dict: dict[str, int]):
    sorted_list: list[dict[str, Any]] = []  # pyright: ignore[reportExplicitAny]
    for ch in chars_num_dict:
        sorted_list.append({"char": ch, "num": chars_num_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_on(dict: dict[str, int]):
    return dict["num"]
