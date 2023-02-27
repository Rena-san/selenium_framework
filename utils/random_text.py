import random
import string


def generate_random_string():
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string


def generate_random_list(size):
    random_list = list()
    for i in range(size):
        random_list.append(random.randint(0, 2))
    return random_list



print(generate_random_list(8))

def random_list_element(given_list, count):
    result_list = []
    working_list = given_list
    for i in range(count):
        idx = random.randint(0, len(working_list) - 1)
        result_list.append(working_list[idx])
        working_list.remove(working_list[idx])
    return result_list

print(random_list_element([2, 5, 6, 8], 3))