import json
import os

import pytest
from selenium_framework.models.user_model import UserModel

DATA_PATH = '/testing_data.json'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def read_test_data():
    with open(DIR_PATH + DATA_PATH) as data_file:
        data = json.load(data_file)
    return data


TEST_DATA = read_test_data()


def get_user_model(data):
    a = list(data.values())
    model = UserModel(*a)
    return model


def user1():
    return get_user_model(TEST_DATA[0])


def user2():
    return get_user_model(TEST_DATA[1])


@pytest.fixture()
def test_text():
    return TEST_DATA[2]
