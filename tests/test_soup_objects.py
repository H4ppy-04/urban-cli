import os
import sys
import unittest
import random

from bs4 import BeautifulSoup, NavigableString, Tag

sys.path.insert(0, os.getcwd())

from src.urban import (
    derive_meaning_as_tag,
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


class GetSoupObjects(unittest.TestCase):
    """Tests All of the functions that are responsible for getting stuff out of soup"""

    def setUp(self) -> None:
        try:
            self.word = random.choice(words)
            print(f"[{words.index(self.word)}] LOOKING UP: {self.word}")
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
