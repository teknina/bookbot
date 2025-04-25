from typing import Dict, List, Union

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text: str) -> int:
    words = book_text.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")
    return num_words

def count_characters(text: str) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for char in text:
        c = char.lower()
        counts[c] = counts.get(c, 0) + 1
    return counts

def sort_character_counts(counts: Dict[str, int]) -> List[Dict[str, Union[str, int]]]:
    sorted_items = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
    return [{"char": char, "num": cnt} for char, cnt in sorted_items]