import json
import os
import sys
import unittest
import random

from bs4 import BeautifulSoup, ResultSet, Tag

sys.path.insert(0, os.getcwd())

from src.urban import (
    derive_example_as_tag,
    derive_meaning_as_tag,
    get_found_word_from_soup,
    get_soup_object_from_word,
)


class GetSoupObjects(unittest.TestCase):
    """Tests All of the functions that are responsible for getting stuff out of soup"""

    def setUp(self) -> None:
        try:
            words = json.load(open("./tests/words.json", "r"))
            self.word = random.choice(words["words"])
            self.soup = get_soup_object_from_word(self.word)
        except IndexError:
            sys.exit(0)

    def test_soup_type(self):
        """
        Test word meaning when derived from .meaning is tag
        """

        _soup = get_soup_object_from_word(self.word)
        self.assertIsInstance(derive_meaning_as_tag(_soup), Tag)

    def test_soup_none(self):
        """
        Test that `word` is correct type in `BeautifulSoup`.
        """

        _soup = get_soup_object_from_word(self.word)
        found_word = get_found_word_from_soup(_soup)

        self.assertIsNotNone(found_word)

    def test_soup_raise_index(self):
        """
        Test that word raises indexerror when word non-existant.
        """

        with self.assertRaises(IndexError):
            get_found_word_from_soup(
                BeautifulSoup("test", features="lxml")
            )  # pyright: ignore

    def test_soup_raise_key(self):
        """
        Test that word raises keyerror when key is invalid.
        """

        with self.assertRaises(IndexError):
            soup = BeautifulSoup("""<a id="not_valid">test</a>""", features="lxml")
            get_found_word_from_soup(soup)

    def test_soup_error(self):
        """
        Test type error raised when `soup` is an invalid type.
        """

        with self.assertRaises(TypeError):
            get_found_word_from_soup(
                BeautifulSoup(3.1, features="lxml")
            )  # pyright: ignore

    def test_derive_example(self):
        """
        Test derive example returns tag
        """

        self.assertIsInstance(
            derive_example_as_tag(self.soup), ResultSet | Tag
        )  # pyright: ignore
