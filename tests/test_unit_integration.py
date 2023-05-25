import json
import os
import sys
import unittest
import random

from bs4 import BeautifulSoup

sys.path.insert(0, os.getcwd())

from src.urban import (
    assert_soup_and_index_valid,
    get_found_word_from_soup,
    get_soup_object_from_word,
    insert_newline_for_break_tags,
    insert_space_after_fullstop,
)


class TestUnitIntegration(unittest.TestCase):
    """Test functions working with other functions"""

    def setUp(self) -> None:
        try:
            words = json.load(open('./tests/words.json', 'r'))
            self.word = random.choice(words['words'])
            self.soup = get_soup_object_from_word(self.word)
        except IndexError:
            sys.exit(0)

    def test_word_from_soup_raises_index_error(self):
        """Test that word from soup raises when a given value is missing"""

        with self.assertRaises(IndexError):
            _soup = get_soup_object_from_word(self.word)
            word_soup = _soup.find_all_next("a")[0].select(  # pyright: ignore
                ".definintion"
            )  # pyright: ignore
            word_soup_raises_key_error = word_soup[0].replace_with(
                word_soup[0].get_text(strip=False)
            )

            assert_soup_and_index_valid(_soup)

            get_found_word_from_soup(
                BeautifulSoup(
                    word_soup_raises_key_error.get_text(strip=False), "html.parser"
                )
            )

    def test_space_insert_after_fullstop(self):
        """Test that a full stop before a character has a space inserted after
        this function has been run. (for grammar)
        """

        incorrect_string = "Four brown ferrets.Five fantastic fairies."
        correct_string = "Four brown ferrets. Five fantastic fairies."

        self.assertEqual(
            insert_space_after_fullstop(list(incorrect_string)), correct_string
        )

    def test_insert_newline_for_break_tags(self):
        """Tests that line breaks are replaced with newline character"""

        html = "<br>"

        expected_result = "\n"

        self.assertEqual(insert_newline_for_break_tags(html), expected_result)

        # Assert that closing tags are replaced with \n
        html = "<br></br>"

        expected_result = "\n"

        self.assertEqual(insert_newline_for_break_tags(html), expected_result)

        # Assert that partial closing tags are replaced with \n
        html = "<br/>"

        expected_result = "\n"

        self.assertEqual(insert_newline_for_break_tags(html), expected_result)

        # Assert that partial closing tags are replaced with \n
        html = "<br />"

        expected_result = "\n"

        self.assertEqual(insert_newline_for_break_tags(html), expected_result)
