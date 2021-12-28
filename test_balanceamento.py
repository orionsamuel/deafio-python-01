import pytest

from balanceamento import read_file, add_user, remove_user, cost_calculate


def test_read_file():
    expected_ttask, expected_umax, expected_new_users = 4, 2, [1, 3, 0, 1, 0, 1]
    actual_ttask, actual_umax, actual_new_users = read_file('input.txt')
    assert actual_ttask == expected_ttask
    assert actual_umax == expected_umax
    assert actual_new_users == expected_new_users


def test_add_server_empty():
    expected = [1]
    actual = add_user(1, 2, [])
    assert actual == expected


def test_add_server_zero():
    expected = []
    actual = add_user(0, 2, [])
    assert actual == expected


def test_add_server_one():
    expected = [2]
    actual = add_user(1, 2, [1])
    assert actual == expected


def test_add_server_full():
    expected = [2, 2]
    actual = add_user(3, 2, [1])
    assert actual == expected


def test_remove_user_zero():
    expected = [2, 2]
    actual = remove_user(0, [2, 2])
    assert actual == expected


def test_remove_user_one():
    expected = [1, 2]
    actual = remove_user(1, [2, 2])
    assert actual == expected


def test_remove_user_three():
    expected = [1]
    actual = remove_user(3, [1, 2, 1])
    assert actual == expected


def test_remove_user_full():
    expected = []
    actual = remove_user(4, [2, 2])
    assert actual == expected


def test_cost_calculate_one():
    expected_cost, expected_qtd_servers = 4, []
    actual_cost, actual_qtd_servers = cost_calculate([(1, 1)], 0, 5)
    assert actual_cost == expected_cost
    assert actual_qtd_servers == expected_qtd_servers


def test_cost_calculate_two():
    expected_cost, expected_qtd_servers = 7, [(1, 4)]
    actual_cost, actual_qtd_servers = cost_calculate([(1, 1), (1, 2), (1, 4)], 1, 5)
    assert actual_cost == expected_cost
    assert actual_qtd_servers == expected_qtd_servers
