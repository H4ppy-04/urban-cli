"""
### Meta & Licensing
__File__: `urban_utils.py`
__License__: [Apache 2.0](https://gh-syn.github.io/urban-cli/license.html)
__Author__: Joshua Rose <joshuarose099@gmail.com>

### Module Description

Contains centralized interactions with urban-cli.

This module handles:
 - sending requests
 - processing responses
 - handling API-related functionalities
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
