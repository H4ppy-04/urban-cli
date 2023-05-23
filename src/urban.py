#!/usr/bin/env python
#
# Author: Joshua Rose <joshuarose099@gmail.com>
# License: MIT


import sys

from bs4 import BeautifulSoup, ResultSet, Tag
import colorama
import requests

colorama.init()


def join_words():
    """Join words into one string when 2 or more words are given."""

    word: str

    if len(sys.argv) >= 2:
        # to prevent user pain and suffering 🕊️
        word = "".join(sys.argv[1:])
    else:
        try:
            word = sys.argv[1]
        except IndexError:
            print("You need to specify a word. Ex: urban YOLO")
            colorama.deinit()
            sys.exit(0)
    return word


def fetch_response_from_URL(_url: str) -> requests.Response:
    """Match response from `_url`.

    Filters status code in the process of fetching `_url`.

    :param `_url`: Url query as a `str` type
    :return: `requests.Response`
    """
    response = requests.get(_url)

    # Sources: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    # Informational response
    if 100 <= response.status_code < 199:
        print(f"Client information response (response code {response.status_code}).")
        print(
            f"It would be amazing if you created an issue at https://github.com/GH-Syn/urban-cli/issues/new and made sure to include:"
        )
        print(f"`status_code` error: `{response.status_code}`")
        print(f"`requests_url:` error: `{_url}`")
        print(f"`response:` error: `{response.json()}`")
        sys.exit(1)

    # Successful responses
    elif 200 <= response.status_code < 299:
        return response

    # Redirectional message
    elif 300 <= response.status_code < 399:
        # TODO: make error this not 💩
        print(f"Client redirected (redirect code {response.status_code}).")
        print(
            f"It would be amazing if you created an issue at https://github.com/GH-Syn/urban-cli/issues/new and made sure to include:"
        )
        print(f"`status_code` error: `{response.status_code}`")
        print(f"`requests_url:` error: `{_url}`")
        print(f"`response:` error: `{response.json()}`")
        sys.exit(1)

    # Client error response
    elif 400 <= response.status_code < 499:
        if response.status_code != 404:
            print(f"Client error {response.status_code}.")
            print(
                f"Assuming your VPN and internet settings are fine, this is a bug (sorry)."
            )
            print(
                f"It would be amazing if you created an issue at https://github.com/GH-Syn/urban-cli/issues/new and made sure to include:"
            )
            print(f"`status_code` error: `{response.status_code}`")
            print(f"`requests_url:` error: `{_url}`")
            print(f"`response:` error: `{response.json()}`")
            sys.exit(1)
        print(
            "That word doesn't exist yet. You can try adding it on urbandictionary.com!"
        )
        colorama.deinit()
        sys.exit(0)

    # Server error
    elif 500 <= response.status_code < 599:
        print(
            f"Got a server error. Somethings wrong with the website. (error {response.status_code})"
        )
        print(
            f"It would be amazing if you created an issue at https://github.com/GH-Syn/urban-cli/issues/new and made sure to include:"
        )
        print(f"`status_code` error: `{response.status_code}`")
        print(f"`requests_url:` error: `{_url}`")
        print(f"`response:` error: `{response.json()}`")
        colorama.deinit()
        sys.exit(0)
    else:
        print(response.status_code)
        print(
            "This is quite rare, but assuming you're connected to the internet, 'urbandictionary.com' seems to be down!"
        )
        sys.exit(1)


def get_first_definition_from_soup(_soup: BeautifulSoup) -> Tag:
    """Return first definition section / 'block' from `_soup`.

    :param _soup: `_soup` object as `BeautifulSoup`
    :return: bs4 tag for first definition
    """
    definition = get_result_set_from_soup(_soup, _index=0)
    return definition


def get_soup_object_from_word(_word: str) -> BeautifulSoup:
    """Return soup object as `BeautifulSoup` from `_word`.

    :param `_word`: Word to query urban dictionary for.
    :param _soup: `_soup` object as `BeautifulSoup`
    """

    URL_QUERY = f"https://www.urbandictionary.com/define.php?term={_word}"
    response = fetch_response_from_URL(URL_QUERY)
    _soup = BeautifulSoup(response.content, "html.parser")

    return _soup


def get_result_set_from_soup(_soup: BeautifulSoup, _index=0):
    """Return result set from `_soup` object.

    :param _index (still being implemented): Definition priority / how high definition is on page - ascending. (default=0)
    :param _soup: `_soup` object as `BeautifulSoup`
    """

    assert_soup_and_index_valid(_soup, _index)
    result_set = _soup.select(".word")[_index]

    return result_set


def assert_index_valid(_index: int):
    """Helper function for assert_soup_and_index_valid.

    :param _index (still being implemented): Definition priority / how high definition is on page - ascending. (default=0)
    """

    if not isinstance(_index, int):
        raise TypeError("Index should be an integer")

    if _index > 0:
        PendingDeprecationWarning(
            "Index parameter is introduced in > 1.1.0. If you are on an eariler release this is an experimental command."
        )


def assert_soup_valid(_soup: BeautifulSoup):
    """Helper function for assert_soup_and_index_valid.

    :param _soup: `_soup` object as `BeautifulSoup`
    """

    if not isinstance(_soup, BeautifulSoup):
        raise TypeError(f"_soup must be of type `BeautifulSoup`, found {type(_soup)}")


def assert_soup_and_index_valid(
    _soup: BeautifulSoup | None, _index: int | None = 0
) -> None:
    """This code is used more than once - prevents violating DRY (don't repeat yourself)

    :param _index (still being implemented): Definition priority / how high definition is on page - ascending. (default=0)
    :param _soup: `_soup` object as `BeautifulSoup`
    """

    assert_soup_valid(_soup) if _soup is not None else (
        assert_index_valid if _index is not None else None
    )


def get_found_word_from_soup(_soup: BeautifulSoup, _index=0):
    """Return word from `_soup` object.

    :param _index (still being implemented): Definition priority / how high definition is on page - ascending. (default=0)
    :param _soup: `_soup` object as `BeautifulSoup`
    """

    assert_soup_and_index_valid(_soup, _index)

    try:
        found_word = _soup.select(".word")[_index].string
    except IndexError:
        raise IndexError(
            f"Tried to find definition {_index} of {len(_soup.select('.word'))}"
        )

    if found_word is None:
        raise KeyError(".word tag not found in soup object.")

    return found_word


def derive_definition_as_tag(_soup: BeautifulSoup, _index=0) -> Tag:
    """Return the definition of a soup_ object.

    :param _soup: `_soup` object as `BeautifulSoup`
    :param _index (still being implemented): Definition priority / how high definition is on page - ascending. (default=0)
    :returns: `Tag` containing definition, date, author, definition example
    """

    assert_soup_and_index_valid(_soup, _index)
    word_meaning = _soup.select(".definition")[_index]

    return word_meaning


def derive_meaning_as_tag(_soup: BeautifulSoup) -> Tag:
    """Return deriveg meaning from `_soup` object.

    :param _soup: `_soup` object as `BeautifulSoup`
    """

    assert_soup_and_index_valid(_soup, _index=None)
    derived_definition = derive_definition_as_tag(_soup)
    word_meaning = derived_definition.select(".meaning")[0]

    return word_meaning


def get_hyperlinks_as_result_set(_word_meaning: Tag) -> ResultSet[Tag] | None:
    """Get hyperlinks as a result set of all unique tags.

    Except: returns none if no links are present (rare but possible)

    Raises:
        TypeError if result set is not of type `ResultSet`
    NOTE: Doesn't check for contents of `ResultSet`

    :param _word_meaning: return value of derive_meaning_as_tag function.
    :return: list of tags or None  if no links are present
    :rtype: ResultSet[Tag] | None
    """

    hyperlinks: None | ResultSet[Tag] = _word_meaning.select(".autolink")

    if hyperlinks is None:
        return None
    elif isinstance(hyperlinks, ResultSet):
        return hyperlinks
    raise TypeError(f"expected ResultSet, got {type(hyperlinks)}")


def format_words_as_string_from_tag(_word_meaning: Tag, _hyperlinks_list: list[str]):
    """Format words into one printable string from `_tag`

    :param _word_meaning: Tag containing word definition
    :param _hyperlinks_list: List of strings that are also hyperlinks in definition
    """

    # all words, can be all links though, which is a pain.
    words = _word_meaning.get_text(strip=False).split(" ", -1)

    if len(words) == 0 | 1:
        # TODO: Handle definitions that only have one word
        return

    words_as_str = " ".join(words)

    for _, word in enumerate(_hyperlinks_list):
        if word in words:
            words_as_str = words_as_str.replace(
                word, colorama.Fore.BLUE + word + colorama.Fore.RESET
            )
            continue
        else:
            if " " in word:
                subwords = word.split(" ", -1)
                for subword in subwords:
                    word = words_as_str.replace(
                        subword, colorama.Fore.BLUE + subword + colorama.Fore.RESET
                    )
    return words_as_str


# TODO get `_definition` working
def fetch_word_from_remote(_word: str, _definition: int = 0) -> dict[str, str] | None:
    """Query urban dictionary for `_word`.

    :param `_word`: Word to query urban dictonary for.
    :param `_definition`: Definition rank. The greater the number the less likely it'll be found.
    :returns: result, author and date as a dictionary.
    """

    _soup = get_soup_object_from_word(_word)

    # NOTE Is of type `Tag` - word_meanign contains author, date, definition
    word_meaning = derive_meaning_as_tag(_soup)

    hyperlinks_list = []

    # Returns (most of the time) a list of tags
    hyperlinks = get_hyperlinks_as_result_set(word_meaning)

    # NOTE: returns list of strings that are links
    if hyperlinks is not None:
        # iterate through found definition meaning
        for word in hyperlinks:
            hyperlinks_list.append(word.string)

    words_as_str = format_words_as_string_from_tag(word_meaning, hyperlinks_list)

    # NOTE don't delete!
    print(words_as_str)

    # Return definition, author, date all as dict
    post_author = ""
    date_posted = ""

    # TODO/FIXME return date and author as well
    return {"definition": "", "author": post_author, "date": date_posted}


word = join_words()
fetch_word_from_remote(word)
