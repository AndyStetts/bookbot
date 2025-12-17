def get_total_words(text):
    words = text.split()
    return len(words)

def get_total_of_each_character(text):
    loweredText = text.lower()
    character_count = {}
    for char in loweredText:
        character_count[char] = character_count.get(char, 0) + 1
    return character_count

def sort_on(items):
    return items["num"]

def dict_sort(dict_to_sort_to_list):
    items = []
    for key, value in dict_to_sort_to_list.items():
        if key.isalpha():
             items.append({"char": key, "num": value})
    items.sort(key=sort_on, reverse=True)
    return items