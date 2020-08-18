from comparator import rank as r
from tests.testhelper import testhelper as th

empty_list = []
single_list = [1]
listOne_co = [1, 2, 3, 4, 5]
listTwo_co = [6, 7, 8]
listThree_co = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
listFour_co = ["a", "b"]
listColors_co = ["BLACK", "ORANGE", "BLUE", "PINK", "PURPLE", "RED", "GREEN", "YELLOW", "BROWN"]

# print("test organizer main")
# print([1, 2, 3])
# r.print_list("unranked", listOne_co)
# print(r.rank_list(listOne_co, listTwo_co))

# print(r.insert_item_at_index(listFour_co, 1, "c"))
# print(r.insert_item_at_index(listThree_co, 3, 0))

# r.rank_list(empty_list)
# r.rank_list(single_list)

# r.rank_list(listOne_co)
r.rank_list(listColors_co)

# print(th.random_int())
# print(th.random_str())
# print(th.random_chr())
# print(th.random_float())
# print(th.random_list())
# print(th.random_obj())
