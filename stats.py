def get_word_count(file_contents):
    total = 0
    words = file_contents.split()
    for word in words:
        total += 1
    return total

def get_character_count(file_contents):
    lower_file_contents = file_contents.lower()
    character_count = {}
    for char in lower_file_contents:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_on(item):
    return item["num"]

def sort_characters(character_count):
    list = []
    for char, count in character_count.items():
        new_dict = {
                "char" : char,
                "num" : count,
            }
        list.append(new_dict)

    list.sort(reverse=True, key=sort_on)
    return list
