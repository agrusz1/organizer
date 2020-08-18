import math
from random import randint


def rank_list(unranked_list: list):
    ranked_list = []
    if len(unranked_list) is 0:
        return print(to_string(unranked_list, ranked_list))

    ranked_list.append(unranked_list.pop())

    while len(unranked_list) > 0:
        competitor = unranked_list.pop()
        ranked_list = compete(competitor, ranked_list)
        print(to_string(unranked_list, ranked_list))

def compete(competitor, ranked_list: list):
    boundaries = reset_boundaries(len(ranked_list))
    while boundaries_not_crossed(boundaries):
        challenger_index = get_middle_index_from_boundaries(boundaries, len(ranked_list))
        challenge(competitor, challenger_index, boundaries, ranked_list)

    insert_item_at_index(ranked_list, get_insert_index(boundaries, len(ranked_list)), competitor)

    return ranked_list

def challenge(competitor, challenger_index, boundaries: list, ranked_list: list):
    while True:
        val = input("Please enter 1 or 2 of the item that you find better: " +
                    "1. " + str(competitor) + " vs. 2. " + str(ranked_list[challenger_index]) + "\n")
        try:
            if int(val) is 1:
                boundaries[1] = challenger_index - 1
                boundaries[2] = "left"
                break
            elif int(val) is 2:
                boundaries[0] = challenger_index + 1
                boundaries[2] = "right"
                break
            else:
                raise ValueError("int out of bounds: " + val)
        except ValueError as error:
            print("\n" + str(error) + "\n\nOnly valid inputs are 1 or 2...\n")


def insert_item_at_index(item_list: list, index: int, item):
    insert_list = shift_elements_right_at_index(item_list, index)

    insert_list[index] = item

    return insert_list

def shift_elements_right_at_index(item_list: list, index: int):
    position = len(item_list)
    item_list.append(0)

    while position > index:
        item_list[position] = item_list[position - 1]
        position -= 1

    item_list[index] = 0

    return item_list

def boundaries_not_crossed(boundaries: list):
    return boundaries[1] - boundaries[0] >= 0

def get_middle_index_from_boundaries(boundaries: list, len_ranked_list: int):
    if boundaries[2] is "-":
        return randint(0, len_ranked_list - 1)

    return math.floor((boundaries[0] + boundaries[1]) / 2)

def reset_boundaries(len_ranked_list: int):
    return [0, len_ranked_list - 1, "-"]

def get_insert_index(boundaries: list, len_ranked_list: int):
    insert_index = 0

    if boundaries[2] is "left":
        insert_index = boundaries[1] + 1

    if boundaries[2] is "right":
        insert_index = boundaries[0]

    if insert_index is -1:
        return 0
    if insert_index is len_ranked_list:
        return len_ranked_list

    return insert_index

def to_string(unranked_list: list, ranked_list: list):
    return "Unranked: " + str(unranked_list) + " Ranked: " + str(ranked_list)
