def get_num_words(text):
    return len(text.split())

def char_count(text):
    rn_dict = {}
    for char in text:
        char = char.lower()
        if char in rn_dict:
            rn_dict[char] += 1
        else:
            rn_dict[char] = 1
    return rn_dict

def char_dict_sorted(rn_dict):
    # Build list of dicts
    list_of_dicts = []
    for char, num in rn_dict.items():
        list_of_dicts.append({"char": char, "num": num})

    # Helper to sort by num
    def sort_on(dict_item):
        return dict_item["num"]

    # Sort descending
    list_of_dicts.sort(key=sort_on, reverse=True)

    return list_of_dicts
