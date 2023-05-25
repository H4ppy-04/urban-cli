import os
import sys
import unittest

from bs4 import BeautifulSoup, NavigableString, Tag

sys.path.insert(0, os.getcwd())

from src.urban import (
    assert_index_valid,
    assert_soup_and_index_valid,
    derive_meaning_as_tag,
    get_found_word_from_soup,
    get_soup_object_from_word,
)


class TestUrban(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        self.word_index = 0
        self.words = [
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

        super().__init__(methodName)

    def setUp(self) -> None:
        try:
            import random
            self.word = random.choice(self.words)
            print(f"[{self.words.index(self.word)}] LOOKING UP: {self.word}")
            self.soup = get_soup_object_from_word(self.word)
        except IndexError:
            sys.exit(0)

    def test_definition_from_soup_object(self):
        """
        Test definition class is present in each soup object.
        """

        initial_definition = self.soup.find("div", class_="definition", recursive=True)

        self.assertIsInstance(initial_definition, NavigableString | Tag)

    def test_word_is_found_in_soup(self):
        """
        Test that `word` is correct type in `BeautifulSoup`.
        """

        _soup = get_soup_object_from_word(self.word)
        found_word = get_found_word_from_soup(_soup)

        self.assertIsNotNone(found_word)

    def test_word_index_raises_warning(self):
        """
        Test that word index raises warning when greater than 0
        """

        # NOTE This relies on there being more than 1 definition present.
        with self.assertRaises(PendingDeprecationWarning):
            assert_index_valid(_index=1)

    def test_invalid_word_index_raises_error_from_float(self):
        """
        Test invalid type in word index raises type erorr
        """

        # NOTE This relies on there being more than 1 definition present.
        with self.assertRaises(TypeError):
            assert_index_valid(_index=float(2.3))  # pyright: ignore

    def test_word_index_raises_index_error(self):
        """
        Test that a high word index raises an index error
        """

        _soup = get_soup_object_from_word(self.word)

        with self.assertRaises(PendingDeprecationWarning):
            assert_index_valid(_index=9000000)

    def test_word_type_raises_type_error(self):
        """
        Test that an invalid word type raises type error
        """

        _soup = get_soup_object_from_word(self.word)

        # assert isinstance(_soup.string, BeautifulSoup)
        with self.assertRaises(TypeError):
            assert_soup_and_index_valid(_soup=False)

    def test_word_none_raises_index_error(self):
        """
        Test that word raises indexerror when word non-existant.
        """

        with self.assertRaises(IndexError):
            get_found_word_from_soup(BeautifulSoup("test", features="lxml"))  # pyright: ignore

    def test_found_word_equal_to_parameter(self):
        """
        Test found word is equal to _word (both as lowered values)
        """

        _soup = get_soup_object_from_word(self.word)
        found_word = get_found_word_from_soup(_soup)

        self.assertEqual(self.word.lower(), found_word.lower())

    def test_integer_type_assert_soup_valid(self):
        """
        Test validity function raises error when index is not integer.
        """
        with self.assertRaises(TypeError):
            assert_soup_and_index_valid(_index=True)  # pyright: ignore

    def test_found_word_meaning_is_tag(self):
        """
        Test word meaning when derived from .meaning is tag
        """

        _soup = get_soup_object_from_word(self.word)
        self.assertIsInstance(derive_meaning_as_tag(_soup), Tag)

    @unittest.skip("Redundant index parameter")
    def test_derivation_index_overload_raises_error(self):
        """Test derivation function return error when index is higher than length

        This tests that assert_soup_and_index_valid is called before
        the word meaning is derived.
        """

        _soup = get_soup_object_from_word(self.word)

        with self.assertRaises(IndexError):
            assert isinstance(derive_meaning_as_tag(_soup), Tag)  # pyright: ignore

    def test_words_as_other_type_returns_str_error(self):
        """Test `words_as_str`  returns string-based error on invalid data type output"""

    def test_word_from_soup_raises_index_error(self):
        """Test that word from soup raises when a given value is missing"""

        with self.assertRaises(IndexError):
            _soup = get_soup_object_from_word(self.word)
            word_soup = _soup.find_all_next("a")[0].select(".definintion")
            word_soup_raises_key_error = word_soup[0].replace_with(
                word_soup[0].get_text(strip=False)
            )

            assert_soup_and_index_valid(_soup)

            get_found_word_from_soup(
                BeautifulSoup(
                    word_soup_raises_key_error.get_text(strip=False), "html.parser"
                )
            )
