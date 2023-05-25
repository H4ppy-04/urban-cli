import sys
import unittest
import random
import os
import json

sys.path.insert(0, os.getcwd())

from src.urban import (
    assert_soup_and_index_valid,
    get_soup_object_from_word,
)


class TestSoupAndIndexFunction(unittest.TestCase):
    """So many test cases about assert_soup_and_index im just making this"""

    def setUp(self) -> None:
        try:
            words = json.load(open("./tests/words.json", "r"))
            self.word = random.choice(words["words"])
            self.soup = get_soup_object_from_word(self.word)
        except IndexError:
            sys.exit(0)

    def test_soup_and_index_raises_type_error(self):
        """
        Test that an invalid word type raises type error
        """

        with self.assertRaises(TypeError):
            assert_soup_and_index_valid(_index=True)  # pyright: ignore
        with self.assertRaises(TypeError):
            assert_soup_and_index_valid(_soup=False)  # pyright: ignore