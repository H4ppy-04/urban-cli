"""
===
API
===

:Authors:
    Joshua Rose

:Version: 2.0.0 of 2023/05/28
:License: `Apache 2.0 <https://gh-syn.github.io/urban-cli/license.html>`_

The API contains centralized interactions with urban-cli.
It's responsible for the following functions.

Sending requests
----------------
Requests that need to be sent to a remote source will be done so through
functions declared in this file. Most of which, will be using custom
exception classes as normal exceptions will not suit this specific use case..

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

import requests

from src.urban_exceptions import InvalidStatusCodeError


def apply_word_to_url(word: str) -> str:
    """
    Attaches a lookup word to the end of the fetch URL.

    :param word: Word to be attached to the end of fetch URL.
    :return: URL with word attached to the end of it.
    """

    dictionary_url = "https://www.urbandictionary.com/define.php?term="
    fetch_url = dictionary_url + word

    return fetch_url


def send_exists_request(word: str) -> bool:
    """
    Requests if a word exists from the urban dictionary.

    :param word: Word attaches as postfix when requesting exists.
    :raise InvalidStatusCodeError: If response status code does not equal 200 or 404.
    :return: `True` if `word` exists otherwise returns `False`.
    """

    # Attach word to url variable
    url = apply_word_to_url(word)

    response = requests.get(url)
    status = response.status_code

    match status:
        case 200:
            return True
        case 404:
            return False
        case _:
            raise InvalidStatusCodeError(status)


def send_phrase_request(phrase: str):
    """
    Request phrase from the urban dictionary.

    :param phrase: Queries to URL in `requests.Request` object.
    :return:
    """
