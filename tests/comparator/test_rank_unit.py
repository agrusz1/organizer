import pytest
import mockito as mock
import random
import math
from tests.testhelper.randomgenerator import *
from tests.testhelper.mockinput import *
from organizer.comparator import rank as subject


# @pytest.mark.parametrize(
#     "", [
#         [[], ],
#     ]
# )
# def test_rank_list(unranked_list: list):
#     assert True
#

# @pytest.mark.parametrize(
#     "", [
#         [[], ],
#     ]
# )
# def test_compete(competitor, ranked_list: list):
#     mock.when(subject).reset_boundaries(len(ranked_list)).thenReturn([0, len(ranked_list) - 1, "-"])
#     mock.when(subject).boundaries_not_crossed().thenReturn(True)
#
#     assert True

# TODO: Improve challenge tests, very messy and not complete
@pytest.mark.parametrize(
    "competitor, challenger_index, boundaries, ranked_list, mocked_input", [
        [55, 1, [0, 0, "-"], [1, 2, 3], 2],
        [55, 1, [0, 0, "-"], [1, 2, 3], 1],
    ]
)
def test_challenge(competitor, challenger_index, boundaries: list, ranked_list: list, mocked_input: int):
    set_keyboard_input([mocked_input])

    subject.challenge(competitor, challenger_index, boundaries, ranked_list)

    actual = boundaries

    expected = [0, 0, "-"]

    if mocked_input is 1:
        expected[1] = challenger_index - 1
        expected[2] = "left"

    if mocked_input is 2:
        expected[0] = challenger_index + 1
        expected[2] = "right"

    assert expected == actual


@pytest.mark.parametrize(
    "item_list, mocked_shifted_list, index, item, expected", [
        [[1], [0, 1], 0, 2, [2, 1]],
        [["one", "two"], ["one", "two", 0], 2, "three", ["one", "two", "three"]],
        [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 0, 'd'], 3, 'e', ['a', 'b', 'c', 'e', 'd']],
    ]
)
def test_insert_item_at_index(item_list: list, mocked_shifted_list: list, index: int, item, expected: list):
    mock.when(subject).shift_elements_right_at_index(item_list, index).thenReturn(mocked_shifted_list)

    actual = subject.insert_item_at_index(item_list, index, item)
    assert expected == actual


@pytest.mark.parametrize(
    "item_list, index, expected", [
        [[1], 0, [0, 1]],
        [[1], 1, [1, 0]],
        [[1, 2, 3, 4, 5], 2, [1, 2, 0, 3, 4, 5]],
    ]
)
def test_shift_elements_right_at_index(item_list: list, index: int, expected: list):
    actual = subject.shift_elements_right_at_index(item_list, index)

    assert expected == actual


@pytest.mark.parametrize(
    "boundaries, expected", [
        [[0, 0, generate_random_str()], False],
        [[0, generate_random_int(1), generate_random_str()], False],
        [[3, 1, generate_random_str()], True],
    ]
)
def test_boundaries_not_crossed(boundaries: list, expected):
    actual = subject.boundaries_not_crossed(boundaries)

    return expected == actual


@pytest.mark.parametrize(
    "boundaries, len_ranked_list, expected", [
        [[0, 0, generate_random_str()], 0, 0],
        [[0, 100, generate_random_str()], 100, 50],
        [[12, 14, "-"], 7, 0],
    ]
)
def test_get_middle_index_from_boundaries(boundaries: list, len_ranked_list: int, expected: int):
    mock_random_int = 4
    mock.when(random).randint(0, len_ranked_list - 1).thenReturn(mock_random_int)

    if boundaries[2] is "-":
        expected = mock_random_int
    else:
        expected = math.floor((boundaries[0] + boundaries[1]) / 2)

    actual = subject.get_middle_index_from_boundaries(boundaries, len_ranked_list)

    assert expected == actual


def test_reset_boundaries():
    len_list = generate_random_int(0)
    expected = [0, len_list - 1, "-"]
    actual = subject.reset_boundaries(len_list)

    assert expected == actual


@pytest.mark.parametrize(
    "boundaries, len_ranked_list, expected", [
        [[0, -1, "left"], 1, 0],
        [[3, 2, "right"], 3, 3],
        [[15, 14, "right"], 3, 15],
        [[7, 6, "left"], 10, 7],
    ]
)
def test_get_insert_index(boundaries: list, len_ranked_list: int, expected):
    actual = subject.get_insert_index(boundaries, len_ranked_list)

    assert expected == actual


@pytest.mark.parametrize(
    "unranked_list, ranked_list", [
        [[], []],
        [[], [1]],
        [[1], []],
        [["one"], ["two"]],
        [['a', 'b'], ['c', 'd']],
    ]
)
def test_to_string(unranked_list: list, ranked_list: list):
    expected = "Unranked: " + str(unranked_list) + " Ranked: " + str(ranked_list)
    actual = subject.to_string(unranked_list, ranked_list)

    assert expected == actual
