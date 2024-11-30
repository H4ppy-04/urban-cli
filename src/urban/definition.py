"""
:Author: Joshua Rose
:Version: 2.0.0 of 2023/05/28
:License: `Apache 2.0 <https://gh-syn.github.io/urban-cli/license.html>`_
:File: urban_api.py
"""

from dataclasses import dataclass, field
from typing import Literal, Optional

import requests


@dataclass
class Definition:
    """
    The definition class.

    Initial values soughted from atbuy/pyurbandict
    """

    word: Optional[str] = ""
    definition: Optional[str] = ""
    example: Optional[str] = ""
    author: Optional[str] = ""
    thumbs_up: Optional[int] = None
    thumbs_down: Optional[int] = None
    sound_urls: Optional[list[str]] = field(default_factory=list)
    written_on: Optional[str] = ""
    permalink: Optional[str] = ""
    defid: Optional[int] = None
    current_vote: str = ""

    @staticmethod
    def trim(string: str):
        """hyperlinks are encased in block brackets, this function removes them"""
        if '[' and ']' in string:
            _string = string.replace(
                "[",
                "",
            ).replace("]", "")
            return _string
        return _string

    def display(
        self,
        print_example: bool,
        print_author: bool,
        print_rating: bool,
        print_date: bool,
    ):
        """Print out the definition, along with a few details"""

        definition = Definition.trim(self.definition)
        example = Definition.trim(self.example)

        string = ""
        string += f"{self.word}:\n{definition}\n\n"
        string += f"Example:\n{example}" if print_example and (self.example != '') else "\n\n"
        string += f"\n\n{self.thumbs_up} likes, {self.thumbs_down} dislikes" if print_rating else ""
        string += f"\nby {self.author}" if print_author else ""
        string += f" on {self.written_on}" if print_date else ""

        print(string)

    @staticmethod
    def show_does_not_exit_error(word: str):
        """Show does not exist error when invalid word is queried."""

        print("The word %s doesn't exist yet." % word, end=" ")
