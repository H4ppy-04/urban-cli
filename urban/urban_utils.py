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
When a request object is received, it needs to be formatted in a way that Python can understand
The beautifulsoup library helps beautifully ✨ with this. It parses html data in a way that can be
read and manipulated very easily.

I/O handling
------------
The argparse library can be thought of as boilerplate level code in addition to a few extra classes
that greatly help building a command line interface. It removes most of the argument logic and lets the
developer focus on what's important. Argparse is used in this file for showing and receiving data.

Common Data Structures
-----------------------
Common data structures such as a date, definition struct, lives in this file.
"""


from dataclasses import dataclass
from datetime import datetime
from typing_extensions import deprecated

from bs4 import BeautifulSoup
import bs4
import requests
import rich

from urban_exceptions import InvalidOrderError


@dataclass
class Definition:
    """Definition struct/dataclass to manage defitions easier.

    It's times like these when I really wish I was using rust.

    :param date: datetime object
    :param author: Username of definition OP
    :param definition: The main definition string
    :param example: The definition usage / example
    """

    definition: str
    example: str | None = None
    author: str = "John Doe"
    date: datetime = datetime.now()


def show_does_not_exit_error(word: str):
    """
    Show does not exist error when invalid word is queried.

    A type error is not raised as data type is checked in `send_phrase_request` function.

    :param word: The invalid word that apparently doesn't exist.
    """

    rich.print("The word %s doesn't exist yet." % word, end=" ")
    rich.print(
        "You can change that by submitting a definition on the {link}".format(
            link="[link url='https://urbandictionary.com/']Urban Dictionary website.[/link]"
        )
    )


@deprecated("Removed in favour of indexing")
def _get_num_of_definitions(result_set: bs4.ResultSet) -> int:
    """
    Returns the number of definitions found for a given word

    :param result_set: A list of tags, defined as a result set object.

    :return: Number of definitions for a given word as an `int`.
    """

    return len(result_set)


def make_soup_from_response(response: requests.Response):
    """
    When life gives you ~~lemons~~ a `response` object... make soup?

    Take a requests.response and extract response from it - thus returning a soup object.

    :param response: Response object assumedly containing one or more definition(s).
    :return: ~~lemonade~~ A beautiful soup 🍜
    """

    response_content: bytes = response.content

    response_soup = BeautifulSoup(response_content, "lxml")

    return response_soup


@deprecated("Indexed tag used in favour of stringifying `definition_tag`.")
def stringify_definition_tag(definition_tag: bs4.Tag) -> str:
    """
    Convert a definition tag into a string.

    This function assumes it's known with 100% certainty that `definition_tag`
    is indeed a *definition* tag, which this function will 'stringify'.

    :param definition_tag: Definition tag that is 100% known to contain a definition
    :return: `stringified` definition
    """

    return str(definition_tag.strings)


def return_definition(raw_soup: BeautifulSoup, order=1):
    """
    Extract the order(st/nd/rd/th) definition from raw_soup (gross)

    :param raw_soup: The raw, unformatted, soup object content
    :param order: The order of the definition.

    For example, if the order was 1, it would return the 1st definition.
    If the order was 2, it would return the second. So on and so forth.

    By default, `return_definition` returns the 1st definition it finds.

    :raises InvalidOrderError: If the order exceeds the number of definitions that've been found.
    :return: Definition as a *beautifully structured* dataclass ⛳
    :rtype: `Definition` dataclass
    """

    definitions_found = len(raw_soup.select(".definition"))

    # Order index readable in python
    indexable_order = order - 1

    filtered_soup_results = raw_soup.find_all("div", class_="definition")

    # NTS: `selected_definitions` is much smaller than `filtered_soup_results` 🙂
    selected_definitions = filtered_soup_results[indexable_order]

    if order > definitions_found:
        raise InvalidOrderError(definitions_found)

    # Create definitoin class
    definition_class = Definition(
            definition=selected_definitions.select(".meaning")[0],
            )

    return definition_class
