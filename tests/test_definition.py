import os
import sys
import unittest
import random

from bs4 import BeautifulSoup, NavigableString, Tag

sys.path.insert(0, os.getcwd())

from src.urban import (
    get_found_word_from_soup,
    get_soup_object_from_word,
)


words = [
    "YOLO",
    "eshay",
    "swag",
    "gtfo",
    "lit",
    "rad",
    "hella",
    "joint",
    "block",
    "dope",
    "rickroll",
]


class test_definition(unittest.TestCase):
    """
    This class is for testing the definition object itself.
    It tests that the object contains valid datatypes.
    It tests for tags and contents in said tags.
    """

    def setUp(self) -> None:
        try:
            self.word = random.choice(words)
            print(f"[{words.index(self.word)}] LOOKING UP: {self.word}")
            self.soup = get_soup_object_from_word(self.word)
        except IndexError:
            sys.exit(0)

    def test_definition_from_soup_object(self):
        """
        Test definition class is present in each soup object.
        """

        initial_definition = self.soup.find("div", class_="definition", recursive=True)

        self.assertIsInstance(initial_definition, NavigableString | Tag)

    def test_definition_equal_to_parameter(self):
        """
        Test found word is equal to _word (both as lowered values)
        """

        _soup = get_soup_object_from_word(self.word)
        found_word = get_found_word_from_soup(_soup)

        self.assertEqual(self.word.lower(), found_word.lower())

    def test_definition_type_is_string(self):
        """
        Test that the definition/word type is a string
        """

        _soup = get_soup_object_from_word(self.word)
        found_word = get_found_word_from_soup(_soup)

        self.assertIsInstance(found_word, str)
