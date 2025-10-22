def count_words(str):
    split_words = str.split()
    count = len(split_words)

    return count

def char_count(content: str):
    char_dict: dict[str, int] = {}
    for i in range(len(content)):
        str_lower = content[i].lower()
        if str_lower in char_dict.keys():
            char_dict[str_lower] += 1
        else:
            char_dict[str_lower] = 1
    return char_dict

def print_report(report):
    new_list = [];
    for k, v in report.items():
        if k.isalpha():
            new_list.append({"char": k, "num": v});
    new_list.sort(reverse=True, key=sort_on);
    return new_list; 

def sort_on(items):
    return items["num"];
