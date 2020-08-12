import math


boundaries = [0, 1, "-"]
state = "STARTING"
competitors = [0, 0]
ranked = []

def rank_list(unranked: list):
    if len(unranked) is 0:
        return print(to_string(unranked, ranked))

    ranked.append(unranked.pop())

    while len(unranked) > 0:
        competitor = unranked.pop()
        compete(competitor, ranked)
    print(to_string(unranked, ranked))

def compete(competitor, ranked_list: list):
    reset_boundaries()

    while boundaries_not_crossed():
        challenger_index = get_middle_index_from_boundaries()
        challenge(competitor, challenger_index)

    insert_item_at_index(ranked_list, get_insert_index(), competitor)

    return print(ranked_list)

def challenge(competitor, challenger_index):
    while True:
        val = input("Please enter 1 or 2 of the item that you find better: " +
                    "1. " + str(competitor) + " vs. 2. " + str(ranked[challenger_index]) + "\n")
        if int(val) is 1:
            boundaries[1] = challenger_index - 1
            boundaries[2] = "left"
            break
        if int(val) is 2:
            boundaries[0] = challenger_index + 1
            boundaries[2] = "right"
            break
        print("please enter 1 or 2 only...")

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

    return item_list

def boundaries_not_crossed():
    return boundaries[1] - boundaries[0] >= 0

def get_middle_index_from_boundaries():
    return math.floor((boundaries[0] + boundaries[1])/2)

def reset_boundaries():
    boundaries[0] = 0
    boundaries[1] = len(ranked) - 1
    boundaries[2] = "-"


def get_insert_index():
    insert_index = 0
    if boundaries[2] is "left":
        insert_index = boundaries[1]

    if boundaries[2] is "right":
        insert_index = boundaries[0]

    if insert_index is -1:
        return 0
    if insert_index is len(ranked):
        return len(ranked)

    return insert_index

def to_string(unranked_list: list, ranked_list: list):
    return "Unranked: " + str(unranked_list) + " Ranked: " + str(ranked_list)
