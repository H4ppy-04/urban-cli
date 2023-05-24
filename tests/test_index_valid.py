import os
import sys
import unittest
import random

from bs4 import BeautifulSoup, NavigableString, Tag

sys.path.insert(0, os.getcwd())

from src.urban import (
    assert_index_valid,
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


class TestIndexValid(unittest.TestCase):
    """Test the tests. Audit the audit. Shit like that."""

    def setUp(self) -> None:
        try:
            self.word = random.choice(words)
            print(f"[{words.index(self.word)}] LOOKING UP: {self.word}")
            self.soup = get_soup_object_from_word(self.word)
        except IndexError:
            sys.exit(0)

    def test_index_raises_warning(self):
        """
        Test that word index raises warning when greater than 0
        """

        # NOTE This relies on there being more than 1 definition present.
        with self.assertRaises(PendingDeprecationWarning):
            assert_index_valid(_index=1)

    def test_index_raises_type_error(self):
        """
        Test invalid type in word index raises type erorr
        """

        # NOTE This relies on there being more than 1 definition present.
        with self.assertRaises(TypeError):
            assert_index_valid(_index=float(2.3))  # pyright: ignore

    def test_index_raises_index_error(self):
        """
        Test that a high word index raises an index error
        """

        with self.assertRaises(PendingDeprecationWarning):
            assert_index_valid(_index=9000000)
