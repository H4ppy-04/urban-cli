"""
===
API
===

:Author: Joshua Rose
:Version: 2.0.0 of 2023/05/28
:License: `Apache 2.0 <https://gh-syn.github.io/urban-cli/license.html>`_
:File: urban_api.py

The API contains centralized interactions with urban-cli.
It's responsible for the following functions.

Sending requests
----------------
Requests that need to be sent to a remote source will be done so through
functions declared in this file. Most of which, will be using custom
exception classes as normal exceptions will not suit this specific use case.

Processing responses
--------------------
Responses that received using the requests library are processed and checked.
Edge cases such as 404 errors work differently in this application, as one
would signify that a word has not been defined as oppose to a missing page.

Integration
-----------
Functions that are defined in the various files around the codebase are managed
within the API file. This file serves as a central point from which functions are
accessed.
"""

from typing import Literal

from loguru import logger
import requests

from urban_exceptions import InvalidStatusCodeError, InvalidWordError
from urban_utils import format_wotd_content, make_soup_from_response


def apply_word_to_url(word: str) -> str:
    """
    Attaches a lookup word to the end of the fetch URL.

    :param word: Word to be attached to the end of fetch URL.
    :return: URL with word attached to the end of it.
    """

    dictionary_url = "https://www.urbandictionary.com/define.php?term="
    fetch_url = dictionary_url + word

    return fetch_url


def send_exists_request(word: str) -> Literal[False] | requests.Response:
    """
    Requests if a word exists from the urban dictionary.

    :param word: Word attaches as postfix when requesting exists.
    :raise InvalidStatusCodeError: If response status code does not equal 200 or 404.
    :return: If the word exists or if the word doesn't exist. Return types differ.
    :rtype `requests.Response`: if `word` exists in the Urban Dictionary.
    :rtype `False`: If `word` does not exist in the Dictionary.
    """

    # Attach word to url variable
    url = apply_word_to_url(word)

    # Get reponse from urban dictionary as a `requests.Response`.
    response = requests.get(url)
    status = response.status_code

    match status:
        case 200:
            return response
        case 404:
            return False
        case _:
            raise InvalidStatusCodeError(status)


def send_wotd_request() -> requests.Response:
    """
    Asks the urban dictionary to get the word of the day (page).

    Returns the word of the day, or, to be more specific - the urban
    dictionary homepage.

    :return: Received data as a `requests.Response` containing
             data received from the urban dictionary homepage.
    """

    response = requests.get("https://www.urbandictionary.com/")

    return response


def show_wotd(response_content: requests.Response):
    """
    Show word of the day from a dictionary object.

    This function works with the help of `send_wotd_request()`.
    No output is returned, everything is printed, hence the verb `show` and not `get` or `return`.

    :param response_content: Content received as part of a `requests.Response()` method.
    :type response_content: bytes
    """

    wotd_soup = make_soup_from_response(response_content)
    definition_object = format_wotd_content(wotd_soup)

    # Show definition information
    print(definition_object.definition)
    print(definition_object.author)


def send_phrase_request(phrase: str):
    """
    Request phrase from the urban dictionary.

    Handles the case that the phrase does not exist with an error message.
    Otherwise, it returns the received phrase that it got from `send_exists_request()` function.

    :param phrase: Queries to URL in `requests.Request` object.
    :raise TypeError: If `phrase` is not a `string`.
    :raise SystemExit: If `phrase` returns a 404. That is - the phrase doesn't exist.
    :return: Received data from the `requests.Response` content method.
    """

    if not isinstance(phrase, str):
        raise TypeError(f"`phrase` read as a `{type(phrase)}` must be a `string`.")

    # TODO: format `phrase` with urllib before asking if it exists
    phrase_exists = send_exists_request(phrase)

    logger.debug(f"phrase_exists is {phrase_exists}")
    if isinstance(phrase_exists, bool):
        raise InvalidWordError(phrase)

    # Rename for readability
    phrase_response = phrase_exists

    # We now know that the phrase not only exists, but is a response.
    response_soup = make_soup_from_response(
        phrase_response
    )  # pyright: ignore -> already handled in SystemExit

    # We return the response content
    return response_soup
