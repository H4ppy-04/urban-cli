global word
global dictionary_url

import json
import os
import random
import sys

import pytest

sys.path.insert(0, os.path.join(os.getcwd(), 'src'))

from urban_api import apply_word_to_url

# Fetch test data
testing_data_file_object = open(file="tests/fixtures/words.json", mode="r", encoding="utf-8")
data_dictionary = json.load(testing_data_file_object)
word_list = data_dictionary.get("words")

word = random.choice(word_list)

dictionary_url = "https://www.urbandictionary.com/define.php?term="
''' URL in `apply_word_to_url` as `dictionary_url` constant '''

''' Type Tests '''

@pytest.mark.smoke
def test_invalid_argument_raises_type_error():
    # Arrange
    argument: set = {1, 2, 3}

    # Act & Assert
    with pytest.raises(TypeError):
        # Act
        apply_word_to_url(argument)  # pyright: ignore

@pytest.mark.smoke
def test_float_argument_raises_key_error():
    # Arrange
    argument = 32.4

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

''' Functional Tests '''

@pytest.mark.smoke
def test_word_is_added_to_string():
    # Arrange
    word = "foxtrot"

    # Act
    expected_result = dictionary_url + word
    actual_result = apply_word_to_url(word)

    # Assert
    assert expected_result == actual_result

@pytest.mark.smoke
def test_multiple_words_added_to_string():
    # Arrange
    words = "lima zulu bravo"

    # Act
    expected_result = dictionary_url + words
    actual_result = apply_word_to_url(words)

    # Assert
    assert expected_result == actual_result

@pytest.mark.smoke
def test_empty_word_added_to_string():
    # Arrange
    expected_result = dictionary_url
    actual_result = apply_word_to_url('')

    # Assert
    assert expected_result == actual_result
