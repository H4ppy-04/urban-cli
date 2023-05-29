global word

import json
import os
import random
import sys

import pytest

sys.path.insert(0, os.path.join(os.getcwd(), "src"))

from urban.urban_api import send_phrase_request

# Fetch test data
testing_data_file_object = open(
    file="tests/fixtures/words.json", mode="r", encoding="utf-8"
)
data_dictionary = json.load(testing_data_file_object)
word_list = data_dictionary.get("words")

word = random.choice(word_list)

""" Type Tests """


@pytest.mark.smoke
def test_float_argument_raises_type_error():
    # Arrange
    argument = 32.4

    # Act & Assert
    with pytest.raises(TypeError):
        # Act
        send_phrase_request(argument)  # pyright: ignore


@pytest.mark.smoke
def test_no_arguments_raises_type_error():
    # Act & assert
    with pytest.raises(TypeError):
        # Act
        send_phrase_request()  # pyright: ignore
