import json
import os
import random
import sys
import unittest

from bs4 import BeautifulSoup, NavigableString, Tag
import loguru

sys.path.insert(0, os.getcwd())

from src.urban import get_found_word_from_soup, get_soup_object_from_word


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
        loguru.logger.debug(self.word)

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

        found_word = get_found_word_from_soup(self.soup)

        self.assertEqual(self.word.lower(), found_word.lower())

    def test_definition_type_is_string(self):
        """
        Test that the definition/word type is a string
        """

        found_word = get_found_word_from_soup(self.soup)

        self.assertIsInstance(found_word, str)
