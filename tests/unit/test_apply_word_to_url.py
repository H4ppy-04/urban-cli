global word

import json
import os
import random
import sys

import pytest

sys.path.insert(0, os.path.join(os.getcwd(), 'src'))

from urban_api import apply_word_to_url


testing_data_file_object = open(file="tests/fixtures/words.json", mode="r", encoding="utf-8")
data_dictionary = json.load(testing_data_file_object)
word_list = data_dictionary.get("words")

word = random.choice(word_list)

@pytest.mark.smoke
def test_invalid_argument_raises_type_error():
    # Arrange
    argument: set = {1, 2, 3}

    # Act & Assert
    with pytest.raises(TypeError):
        # Act
        apply_word_to_url(argument)  # pyright: ignore

@pytest.mark.smoke
def test_no_arguments_raises_type_error():
    # Act & assert
    with pytest.raises(TypeError):
        # Act
        apply_word_to_url()  # pyright: ignore
