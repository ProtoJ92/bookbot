# stats.py

def get_num_words(text):
    """Counts the number of words in a string."""
    words = text.split()
    return len(words)

def get_char_counts(text):
    """Counts the number of times each character appears in the text."""
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts):
    """Sorts the character count dictionary into a list of dicts by count descending."""
    sorted_list = []
    for char, count in char_counts.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
