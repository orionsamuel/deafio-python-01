import pytest

from balanceamento import read_file, add_user, remove_user

'''def test_read_file():
    expected_ttask, expected_umax, expected_new_users = 4, 2, [1,3,0,1,0,1]
    ttask, umax, new_users = read_file('input.txt')
    assert ttask, umax, new_users == expected_ttask, expected_umax, expected_new_users'''


def test_add_server():
    expected = [2,2]
    actual = add_user(1, 2, [])
    actual = add_user(3, 2, [1])
    assert actual == expected


def test_remove_user():
    expected = []
    actual = remove_user(4, 2, [2,2])
    assert actual == expected