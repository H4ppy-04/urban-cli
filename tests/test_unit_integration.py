import json
from logging import error
import os
import sys
import unittest
import random

from bs4 import BeautifulSoup
import colorama
from colorama.initialise import deinit
import requests

sys.path.insert(0, os.getcwd())

from src.urban import (
    assert_soup_and_index_valid,
    deinit_sys_exit,
    display_requests_error,
    get_found_word_from_soup,
    get_soup_object_from_word,
    insert_newline_for_break_tags,
    insert_space_after_chars,
    join_words,
    process_word,
)


class TestUnitIntegration(unittest.TestCase):
    """Test functions working with other functions"""

    def setUp(self) -> None:
        try:
            words = json.load(open("./tests/words.json", "r"))
            self.word = random.choice(words["words"])
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

    def test_space_insert_after_chars(self):
        """Test that a full stop before a character has a space inserted after
        this function has been run. (for grammar)
        """

        incorrect_string = "Four brown ferrets.Five fantastic fairies."
        correct_string = "Four brown ferrets. Five fantastic fairies."

        self.assertEqual(
            insert_space_after_chars(list(incorrect_string)), correct_string
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

    def test_word_join(self):
        """
        Test word join function works.
        """
        words = "the quick brown fox"
        words_joined = process_word(words)
        self.assertEqual(words, words_joined)

    def test_display_requests_exits(self):
        """
        Test that display requests error exists on system
        exit if the response given is equal to `None`
        """
        with self.assertRaises(SystemExit):
            display_requests_error(None)

    def test_display_requests_default(self):
        """
        Test that display requsets exists by default.
        """
        with self.assertRaises(SystemExit):
            display_requests_error(requests.Response())

    def test_preface(self):
        """
        Test preface component of display requests error
        """

        with self.assertRaises(TypeError):
            display_requests_error(None, [])  # pyright: ignore

    def test_preface_output(self):
        """
        Test preface prints properly
        """

        with self.assertRaises(SystemExit):
            display_requests_error(None, "preface output...")

    def test_deinit_sys_exit(self):
        """
        Test deinit raises SystemExit
        """
        with self.assertRaises(SystemExit):
            deinit_sys_exit()


    def test_deinit_type(self):
        """
        Test deinit type error
        """
        with self.assertRaises(TypeError):
            deinit_sys_exit(exit_code="")  # pyright: ignore

    def test_join_words_exit(self):
        """
        Test join words exists on invalid words argument
        """

        with self.assertRaises(SystemExit):
            join_words(words=["test"])

    def test_join_words_type(self):
        """
        Test raise typerror on non-list words argument
        """
        with self.assertRaises(TypeError):
            join_words(2)  # pyright: ignore

    def test_join_words_concat(self):
        """
        Test join words function concatenates list
        """
        _input = ["python", "the", "brown", "cow"]
        _output = "the brown cow"
        self.assertEqual(join_words(_input), _output)
