import pytest
from tests.testhelper import testhelper as th
from organizer.comparator import rank as subject


def test_reset_boundaries():
    len_list = th.random_int(0)
    expected = [0, len_list - 1, "-"]
    actual = subject.reset_boundaries(len_list)

    assert expected == actual

@pytest.mark.parametrize(
    "boundaries, expected", [
        [[0, 0, th.random_str()], False],
        [[0, th.random_int(1), th.random_str()], False],
        [[3, 1, th.random_str()], True],
    ]
)
def test_boundaries_not_crossed(boundaries: list, expected):
    actual = subject.boundaries_not_crossed(boundaries)

    return expected == actual

