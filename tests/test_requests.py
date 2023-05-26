import json
import os
import sys
import unittest
import random

from bs4 import BeautifulSoup, NavigableString, ResultSet, Tag
import bs4
import requests

sys.path.insert(0, os.getcwd())

from src.urban import (
    fetch_response_from_URL,
    get_first_definition_from_soup,
    get_found_word_from_soup,
    get_soup_object_from_word,
)


class test_definition(unittest.TestCase):
    """
    This class is for testing the definition object itself.
    It tests that the object contains valid datatypes.
    It tests for tags and contents in said tags.
    """

    def setUp(self) -> None:
        try:
            words = json.load(open("./tests/words.json", "r"))
            self.word = random.choice(words["words"])
            self.soup: BeautifulSoup = get_soup_object_from_word(
                self.word
            )  # pyright: ignore
        except IndexError:
            sys.exit(0)

    def test_fetch_informational(self):
        """
        Test error codes within informational range
        """
        with self.assertRaises(SystemExit):
            fetch_response_from_URL("https://example.com", 150)

    def test_fetch_success(self):
        """
        Test success response
        """
        self.assertIsInstance(
            fetch_response_from_URL("https://example.com", 200), requests.Response
        )

    def test_fetch_redirect(self):
        """
        Test error test_fetch_redirect code(s)
        """
        with self.assertRaises(SystemExit):
            fetch_response_from_URL("https://example.com", 420)
        with self.assertRaises(SystemExit):
            fetch_response_from_URL("https://example.com", 404)

    def test_server_error(self):
        """
        Test fetch server error
        """
        with self.assertRaises(SystemExit):
            fetch_response_from_URL("https://example.com", 520)

    def test_default_match_case(self):
        """
        Test default match case
        """
        with self.assertRaises(SystemExit):
            fetch_response_from_URL("https://example.com", 780)

    def test_type_url(self):
        """
        Test raise type error
        """

        with self.assertRaises(TypeError):
            fetch_response_from_URL(True)  # pyright: ignore

    def test_type_response(self):
        """
        Test raise type error for response object
        """

        with self.assertRaises(TypeError):
            fetch_response_from_URL("", "")  # pyright: ignore

    def test_response_as_none(self):
        """
        Give none as the response default.
        """
        self.assertIsInstance(
            fetch_response_from_URL("https://example.com", None), requests.Response
        )
