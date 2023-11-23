"""
:Author: Joshua Rose
:Version: 2.0.0 of 2023/05/28
:License: `Apache 2.0 <https://gh-syn.github.io/urban-cli/license.html>`_
:File: urban_utils.py

This file contains utility functions and helper methods.  It is responsible for:
     * manipulating request data / formatting request data
     * contains miscellaneous data structures (date, definition, etc)
"""

from bs4 import BeautifulSoup
import requests
import rich
from loguru import logger


def show_does_not_exit_error(word: str):
    """
    Show does not exist error when invalid word is queried.

    A type error is not raised as data type is checked in `send_phrase_request`
    function.

    :param word: The invalid word that apparently doesn't exist.
    """

    rich.print("The word %s doesn't exist yet." % word, end=" ")
    rich.print(
        "You can change that by submitting a definition on the {link}".format(
            link="[link url='https://urbandictionary.com/']Urban Dictionary website.[/link]"
        )
    )


def make_soup_from_response(response: requests.Response):
    """
    When life gives you ~~lemons~~ a `response` object... make soup?

    Take a requests.response and extract response from it thus returning a
    soup object.

    :param response: Response object assumedly containing one or more
                     definition(s).
    :return: ~~lemonade~~ A beautiful soup 🍜
    """

    response_content: bytes = response.content

    response_soup = BeautifulSoup(response_content, "lxml")

    return response_soup


def remove_punctuation_spacing(text: str):
    """
    Remove any spacing between punctuation.

    Example
    -------
    A string such as "The quick brown fox ." when ran through this function as:

    ```python

    >>> Definition.remove_punctuation_spacing("The quick brown fox .")

    ```

    Outputs:

    ```python

    "The quick brown fox."

    ```

    :return: Formatted string with correct use of punctuation
    """

    chars = list(text)

    for char in range(0, len(chars) - 1):
        try:
            if chars[char] == " ":
                match chars[char + 1]:
                    case "’":
                        chars.pop(char)
                    case ".":
                        chars.pop(char)
                    case ",":
                        chars.pop(char)
                    case ":":
                        chars.pop(char)
                    case " ":
                        chars.pop(char)
                    case "`":
                        chars.pop(char)
                    case "~":
                        chars.pop(char)
                    case "\\":
                        chars.pop(char)
                    case "/":
                        chars.pop(char)
                    case "'":
                        chars.pop(char)
                    case '"':
                        chars.pop(char)
                    case "?":
                        chars.pop(char)
        except IndexError:
            break

    return "".join(chars)


def format_sentences(text: str, max_length: list[int] | int) -> str:
    """
    Formats sentences in the given text.

    Function formats sentences by starting a new line if a sentence exceeds
    the maximum length. Each line will not exceed the maximum length, even if
    it means breaking a word.

    :param tag: The input text containing sentences.
    :param max_length: The maximum length of a line. The default value for t
                       this variable is 120.

    :return: The formatted text with sentences wrapped properly.
    """

    logger.debug(type(text))
    words = text.split()
    lines = []
    current_line = ""

    if isinstance(max_length, list):
        if len(max_length):
            max_length = max_length[0]
        else:
            max_length = 120

    for word in words:
        # logger.debug(type(max_length))
        if len(current_line) + len(word) <= max_length:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    lines.append(current_line.strip())
    formatted_text = "\n".join(lines)

    return formatted_text
