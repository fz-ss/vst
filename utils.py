import os


def remove_blank_subscript(lst: list[str]) -> list[str]:
    cleaned_list = []
    for i in range(len(lst)):
        if i % 4 == 2 and lst[i] != "\n":
            cleaned_list += lst[i - 2:i + 2]
    return cleaned_list


def is_cjk_character(char: str) -> bool:
    return True if int(0x4e00) <= ord(char) <= int(0x9fff) else False


def drop_unnecessary_whitespace(sentence: str) -> str:
    whitespace = ' '
    double_whitespace = whitespace * 2
    while double_whitespace in sentence:
        sentence = sentence.replace(double_whitespace, whitespace)
    sentence = sentence.strip()
    whitespace_counts = sentence.count(whitespace)
    start = 0
    for _ in range(whitespace_counts):
        w_index = start + sentence[start:].find(whitespace)
        char_l, char_r = sentence[w_index - 1], sentence[w_index + 1]
        if is_cjk_character(char_l) or is_cjk_character(char_r):
            sentence = sentence[:w_index] + sentence[w_index + 1:]
        start = w_index + 1
    return sentence


def last_two_levels(file_path):
    head, tail = os.path.split(file_path)
    head, second_level = os.path.split(head)
    last_two_levels_path = os.path.join(second_level, tail)
    return last_two_levels_path
