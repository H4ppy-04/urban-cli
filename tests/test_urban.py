import os
import sys
import unittest

from bs4 import BeautifulSoup, NavigableString, Tag

from urban import (
    assert_soup_and_index_valid,
    derive_meaning_as_tag,
    get_found_word_from_soup,
    get_soup_object_from_word,
)

sys.path.insert(0, os.path.join(os.path.dirname(os.getcwd()), "src"))


class TestUrban(unittest.TestCase):
    def __init__(self) -> None:
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

        super().__init__()

    def setUp(self) -> None:
        try:
            self.word = self.words[self.word_index]
            self.soup = get_soup_object_from_word(self.word)
            self.word_index += 1
        except IndexError:
            sys.exit(0)

        return super().setUp()

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

        _soup = get_soup_object_from_word(self.word)

        # NOTE This relies on there being more than 1 definition present.
        with self.assertWarns(PendingDeprecationWarning):
            assert_soup_and_index_valid(_soup, _index=1)

    def test_word_index_raises_index_error(self):
        """
        Test that a high word index raises an index error
        """

        _soup = get_soup_object_from_word(self.word)

        # NOTE In order of warns / errors
        with self.assertWarns(PendingDeprecationWarning) or self.assertRaises(
            IndexError
        ):
            assert_soup_and_index_valid(_soup, _index=999)

    def test_word_type_raises_type_error(self):
        """
        Test that an invalid word type raises type error
        """

        _soup = get_soup_object_from_word(self.word)

        assert isinstance(_soup.string, BeautifulSoup)
        with self.assertRaises(TypeError):
            assert_soup_and_index_valid(_soup.string, _index=0)

    def test_word_none_raises_key_error(self):
        """
        Test that word raises keyerror when word is none
        """

        with self.assertRaises(KeyError):
            get_found_word_from_soup(None)  # pyright: ignore

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
            assert isinstance(
                derive_meaning_as_tag(_soup, _index=999), Tag
            )  # pyright: ignore
