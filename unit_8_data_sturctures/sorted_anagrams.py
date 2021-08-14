def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)


def is_already_added(word, list_of_lists):
    for cur_list in list_of_lists:
        if len(cur_list) > 0 and is_anagram(word, cur_list[0]):
            return True
    return False


def sort_anagrams(list_of_strings):
    res = list()
    for i in range(len(list_of_strings)):
        str1 = list_of_strings[i]
        if is_already_added(str1, res):
            continue
        sub_list = [str1]
        for j in range(i + 1, len(list_of_strings)):
            str2 = list_of_strings[j]
            if is_anagram(str1, str2):
                sub_list.append(str2)
        res.append(sub_list)
    return res


list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries',
                 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']

print(sort_anagrams(list_of_words))
