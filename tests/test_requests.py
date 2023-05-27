import json
import os
import sys
import unittest
import random

from bs4 import BeautifulSoup

sys.path.insert(0, os.getcwd())

from src.urban import (
    get_error_as_string,
    get_soup_object_from_word,
)


class test_definition(unittest.TestCase):
    """
    This class is for testing the definition object itself.
    It tests that the object contains valid datatypes.
    It tests for tags and contents in said tags.
    """

    def setUp(self) -> None:
        words = json.load(open("./tests/words.json", "r"))
        self.word = random.choice(words["words"])
        self.soup: BeautifulSoup = get_soup_object_from_word(
            self.word
        )  # pyright: ignore
        print(self.word)

    def test_error_string_type(self):
        """
        test raise type error on invalid input for get error as string
        """

        with self.assertRaises(Warning):
            get_error_as_string(True)

    def test_error_index(self):
        """
        test raise index error
        """

        with self.assertRaises(Warning):
            get_error_as_string(999)

    def test_error_valid(self):
        """
        test return valid response
        """

        self.assertEqual(get_error_as_string(404), "not_found")
