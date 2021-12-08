""" Puzzle for day 8 advent of code 2021
"""
import numpy as np


# windows filepath
filename = '..\data\data.txt'
number_array = []
number_segment_key = {'0': [1, 2, 3, 5, 6, 7], '1': [3, 6], '2': [1, 3, 4, 5, 7],
                      '3': [1, 3, 4, 6, 7], '4': [2, 3, 4, 6], '5': [1, 2, 4, 6, 7],
                      '6': [1, 2, 4, 5, 6, 7], '7': [1, 3, 6], '8': [1, 2, 3, 4, 5, 6, 7],
                      '9': [1, 2, 3, 4, 6, 7]}


class HelperDictionary(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value


def convert_list_to_string(string):
    list1 = []
    list1[:0] = string
    return list1


def get_key(input_dict, val):
    for key, value in input_dict.items():
        if val == value:
            return key
    return "a"


def process_segments(input_dict, list_of_keys, length_of_keys, swap_3_6=False, swap_2_4=False):
    if swap_3_6:
        val_36 = [6, 3]
    else:
        val_36 = [3, 6]

    if swap_2_4:
        val_24 = [4, 2]
    else:
        val_24 = [2, 4]

    segment_dict = HelperDictionary()
    segment_dict.key = val_36[0]
    segment_dict.value = input_dict[1][0]
    segment_dict.add(segment_dict.key, segment_dict.value)
    segment_dict.key = val_36[1]
    segment_dict.value = input_dict[1][1]
    segment_dict.add(segment_dict.key, segment_dict.value)
    iterlist = [1, 7, 4, 8]
    for i in range(0, len(iterlist) - 1):
        test1 = convert_list_to_string(input_dict[iterlist[i]])
        test2 = convert_list_to_string(input_dict[iterlist[i + 1]])
        delta = set(test2) - set(convert_list_to_string(test1))
        if i == 0:
            segment_dict.value = sorted(delta)[0]
            segment_dict.key = 1
            segment_dict.add(segment_dict.key, segment_dict.value)
        elif i == 1:
            segment_dict.value = sorted(delta)[0]
            segment_dict.key = val_24[0]
            segment_dict.add(segment_dict.key, segment_dict.value)
            segment_dict.value = sorted(delta)[1]
            segment_dict.key = val_24[1]
            segment_dict.add(segment_dict.key, segment_dict.value)
    count = 0
    short_loc = []
    for i in length_of_keys:
        if i == 6:
            short_loc.append(list_of_keys[count])
        count += 1
    # Find 5th , 7th segment
    segment_value_list = set(list(segment_dict.values()))
    for i in short_loc:
        find_9 = set(convert_list_to_string(i))
        delta = sorted(find_9 - segment_value_list)
        if len(delta) == 1:
            segment_dict.value = sorted(delta)[0]
            segment_dict.key = 7
            segment_dict.add(segment_dict.key, segment_dict.value)
            find_8 = set(convert_list_to_string(input_dict[8]))
            delta = sorted(find_8 - find_9)
            segment_dict.value = sorted(delta)[0]
            segment_dict.key = 5
            segment_dict.add(segment_dict.key, segment_dict.value)
    return(segment_dict)


# line read
with open(filename) as fn:
    ln = fn.readline()
    signal_input = str.split(ln)
    while ln:
        compendium = HelperDictionary()
        input_key = signal_input[:10]
        input_signal = signal_input[11:]
        dict_keys = [len(x) for x in input_key]
        for i in dict_keys:
            if i == 2 or i == 4 or i == 3 or i == 7:
                compendium.key = input_key[dict_keys.index(i)]
                if i == 2:
                    val = 1
                elif i == 4:
                    val = 4
                elif i == 3:
                    val = 7
                elif i == 7:
                    val = 8
                compendium.value = val
                compendium.add(compendium.value, compendium.key)
        if len(compendium) == 4:
            infered_segments = process_segments(compendium, input_key, dict_keys, False, False)
            infered_segments_crossed = process_segments(compendium, input_key, dict_keys, True, False)
            infered_segments_crossed1 = process_segments(compendium, input_key, dict_keys, False, True)
            infered_segments_crossed2 = process_segments(compendium, input_key, dict_keys, True, True)
            infered_letters = dict(zip(infered_segments.values(), infered_segments.keys()))
            infered_letters_crossed = dict(zip(infered_segments_crossed.values(), infered_segments_crossed.keys()))
            infered_letters_crossed1 = dict(zip(infered_segments_crossed1.values(), infered_segments_crossed1.keys()))
            infered_letters_crossed2 = dict(zip(infered_segments_crossed2.values(), infered_segments_crossed2.keys()))

        str_num = str()
        for i in input_signal:
            temp_number = []
            temp_number_crossed = []
            temp_number_crossed1 = []
            temp_number_crossed2 = []
            for j in sorted(convert_list_to_string(i)):
                temp_number.append(infered_letters[j])
                temp_number_crossed.append(infered_letters_crossed[j])
                temp_number_crossed1.append(infered_letters_crossed1[j])
                temp_number_crossed2.append(infered_letters_crossed2[j])
            key_num = get_key(number_segment_key, sorted(temp_number))
            if key_num == "a":
                key_num = get_key(number_segment_key, sorted(temp_number_crossed))
                if key_num == "a":
                    key_num = get_key(number_segment_key, sorted(temp_number_crossed1))
                    if key_num == "a":
                        key_num = get_key(number_segment_key, sorted(temp_number_crossed2))
            str_num = str_num + key_num
        number_array.append(str_num)
        ln = fn.readline()
        signal_input = str.split(ln)
final_array_string = np.array(number_array)
final_array_int = final_array_string.astype(int)
print(final_array_int.sum())
