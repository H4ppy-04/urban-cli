import unittest
from bs4 import Tag
import os, sys

sys.path.insert(0, os.getcwd())
from src.urban import format_words_as_string_from_tag


class TestFormatWordsAsStringFromTag(unittest.TestCase):
    def test_empty_definition(self):
        word_meaning = Tag(name="tag_name")
        hyperlinks_list = ["link1", "link2"]
        result = format_words_as_string_from_tag(word_meaning, hyperlinks_list)
        self.assertIsNone(result)

    def test_single_word_definition(self):
        word_meaning = Tag(name="tag_name")
        word_meaning.string = "example"
        hyperlinks_list = ["link1", "link2"]
        result = format_words_as_string_from_tag(word_meaning, hyperlinks_list)
        self.assertEqual(result, None)

    def test_multiple_words_definition(self):
        word_meaning = Tag(name="tag_name")
        word_meaning.string = "example definition"
        hyperlinks_list = ["link1", "link2"]
        result = format_words_as_string_from_tag(word_meaning, hyperlinks_list)
        self.assertEqual(result, "example definition")


if __name__ == "__main__":
    unittest.main()
