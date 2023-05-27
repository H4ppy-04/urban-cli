import json
import os
import sys
import unittest
import random

import requests

sys.path.insert(0, os.getcwd())

from src.urban import (
    deinit_sys_exit,
    display_requests_error,
    get_soup_object_from_word,
    insert_newline_for_break_tags,
    insert_space_after_chars,
    join_words,
    main,
    process_word,
)


class TestUnitIntegration(unittest.TestCase):
    """Test functions working with other functions"""

    def setUp(self) -> None:
        words = json.load(open("./tests/words.json", "r"))
        self.word = random.choice(words["words"])
        self.soup = get_soup_object_from_word(self.word)

    def test_word_from_soup_raises_index_error(self):
        """Test that word from soup raises when a given value is missing"""

        with self.assertRaises(IndexError):
            _soup = get_soup_object_from_word(self.word)
            _soup.find_all_next("a")[0].select(".definintion")  # pyright: ignore

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

    def test_main_function(self):
        """
        test `main` function
        """
        with self.assertRaises(SystemExit):
            main()
