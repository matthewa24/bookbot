
def get_num_words(content):
    word_list = content.split()
    return len(word_list)

def sort_by(item):
    return item["count"]

def convert_charmap(charmap):
    new_map_list = []
    for c in charmap:
        tmp = {"char": c, "count": charmap[c]}
        new_map_list.append(tmp)
    return new_map_list

def get_num_chars(content):
    chars = list(content)
    charmap = {}
    for c in chars:
        if not c.isalpha():
            continue
        c = c.lower()
        if c not in charmap:
            charmap[c] = 1
        else:
            charmap[c] += 1
    charmap = convert_charmap(charmap)
    charmap.sort(reverse=True, key=sort_by)
    return charmap

    
