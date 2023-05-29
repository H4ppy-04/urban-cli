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


from bs4 import BeautifulSoup
import requests
import rich

from urban_exceptions import InvalidOrderError


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


def _get_num_of_definitions(raw_soup: BeautifulSoup) -> int:
    """
    Returns the number of definitions found for a given word

    :param raw_soup: The soup object. It should definitely contain at least one definition.

    The soup object should not have the content of a 404 html response, as that should be
    mitigated before ever making a soup. Thus, a type check does not have to be done! 🤓

    :return: Number of definitions for a given word as an `int`.
    """

    count_definitions = raw_soup.find_all('div', class_='.definition')  # FIXME: remove dot - causes error maybe. Ill have to test if it's a problem first.

    return len(count_definitions)

def make_soup_from_response(response: requests.Response):
    """
    When life gives you ~~lemons~~ a `response` object... make soup?

    Take a requests.response and extract response from it - thus returning a soup object.

    :param response: Response object assumedly containing one or more definition(s).
    :return: ~~lemonade~~ A beautiful soup 🍜
    """

    response_content: bytes = response.content

    response_soup = BeautifulSoup(response_content)

    return response_soup

def return_definition(raw_soup: BeautifulSoup, order = 1):
    """
    Extract the order(st/nd/rd/th) definition from raw_soup (gross)

    :param raw_soup: The raw, unformatted, soup object content
    :param order: The order of the definition.

    For example, if the order was 1, it would return the 1st definition.
    If the order was 2, it would return the second. So on and so forth.

    By default, `return_definition` returns the 1st definition it finds.

    :raises InvalidOrderError: If the order exceeds the number of definitions that've been found.
    :return: Definition as a *beautifully-souped* tag ⛳
    """

    definitions_found = _get_num_of_definitions(raw_soup)

    if order > definitions_found:
        raise Exception(InvalidOrderError(definitions_found))

    # Definitions is not needed anymore
    del definitions_found

    definition_tag = raw_soup.find_all('div', class_='.definition')[order]

    return definition_tag
