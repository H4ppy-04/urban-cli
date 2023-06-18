"""
=====
Utils
=====

:Author: Joshua Rose
:Version: 2.0.0 of 2023/05/28
:License: `Apache 2.0 <https://gh-syn.github.io/urban-cli/license.html>`_
:File: urban_utils.py

This file contains utility functions and helper methods.
It is responsible for the following functions.

Data Manipulation
-----------------
When a request object is received, it needs to be formatted in a way that
Python can understand The beautifulsoup library helps beautifully ✨ with
this. It parses html data in a way that can be read and manipulated very
easily.

I/O handling
------------
The argparse library can be thought of as boilerplate level code in addition
to a few extra classes that greatly help building a command line interface.
It removes most of the argument logic and lets the developer focus on what's
important. Argparse is used in this file for showing and receiving data.

Common Data Structures
-----------------------
Common data structures such as a date, definition struct, lives in this file.
"""

from bs4 import BeautifulSoup
import requests
import rich


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


def format_sentences(text: str, max_length: int) -> str:
    """
    Formats sentences in the given text.

    Function formats sentences by starting a new line if a sentence exceeds
    the maximum length. Each line will not exceed the maximum length, even if
    it means breaking a word.

    :param tag: The input text containing sentences.
    :param max_length: The maximum length of a line.

    :return: The formatted text with sentences wrapped properly.
    """

    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) <= max_length:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    lines.append(current_line.strip())
    formatted_text = "\n".join(lines)

    return formatted_text
