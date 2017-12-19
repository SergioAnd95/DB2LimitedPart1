import re


def handle_numbers(number1, number2, number3):
    """
    Get range of from number1 to number2 and
    return count of integers that are devisible by number3

    :param number1: int
    :param number2: int
    :param number3: int
    :return: int
    """
    if number3 == 0:
        return 0

    return len([num for num in range(number1, number2+1) if num%number3==0])


def handle_numbers2(number1, number2, number3):
    """
    Get range of from number1 to number2 and
    return count of integers that are devisible by number3

    :param number1: int
    :param number2: int
    :param number3: int
    :return: int
    """
    count = 0
    if number3 == 0:
        return 0

    if number1 % number3 == 0 or number2 % number3 == 0:
        count += 1

    count += abs((number2 - number1)) // abs(number3)
    return count
    # return len([num for num in range(number1, number2+1) if num%number3==0])


def handle_string(value):
    """
    Take string and split it on number and letters
    and return count of them
    :param value: str
    :return: dict
    """
    all_letters = "".join(re.findall(r"([a-z]+)", value, re.I))
    all_numbers = "".join(re.findall(r"([0-9]+)", value, re.I))

    return {'letters': len(all_letters), 'numbers': len(all_numbers)}


def handle_list_of_tuples(lst):
    """
    Take list of tuples (e.g. handle_list_of_tuples(list)) and sort it based on the next rules:
    name / age / height / weight
    :param lst: list
    :return: list
    """
    return sorted(lst, key=lambda t: (t[0], -1*int(t[1]), -1*int(t[2]), -1*int(t[3])))