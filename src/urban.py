#!/usr/bin/env python
#
# Author: Joshua Rose <joshuarose099@gmail.com>
# License: MIT


import sys
from typing_extensions import deprecated

from bs4 import BeautifulSoup, NavigableString, ResultSet, Tag
import bs4
import colorama
import requests
from rich import print as rich_print

colorama.init()


def join_words() -> str:
    """Join words into one string when 2 or more words are given.

    Raises:
        `IndexError` if no word is specified

    Return:
        One or more words depending on if spaces are present (as str)
    """

    if len(sys.argv) >= 2:
        # to prevent user pain and suffering 🕊️
        word = " ".join(sys.argv[1:])
    else:
        try:
            word = sys.argv[1]
        except IndexError:
            print("You need to specify a word. Example: urban drip")
            colorama.deinit()
            sys.exit(0)
    return word


def deinit_sys_exit(exit_code: int = 0) -> None:
    """Uninitialize colorama and exit with `exit_code`.

    Description:
        This function exists to prevent repeating blocks of code when
        the program needs to exit.

    Parameters:
        exit_code: The exit code to use from sys.exit
                   Default is 0 if none is specified.

    Return:
        None
    """

    colorama.deinit()
    sys.exit(exit_code)


def display_requests_error(
    _response: requests.Response | None = None, preface=""
) -> None:
    """Display requests response with github link.

    Description:
        This exists to prevent having to specify chunks of response dialogue.

    Parameters:
        response: Requests response, assumedly one that is unexpected
        preface: If the message requires additional explanation. ("" is default)

    Return:
        None; function calls system exit.
    """

    print(preface)

    if _response is None:
        print(
            f"It would be amazing if you created an issue at https://github.com/GH-Syn/urban-cli/issues/new"
        )
        print(f"Please include any error messages or weirdness that you encountered.")
        deinit_sys_exit()
        return

    print(f"Client information response (response code {_response.status_code}).")
    print(
        f"It would be amazing if you created an issue at https://github.com/GH-Syn/urban-cli/issues/new and made sure to include:"
    )
    print(f"`status_code` error: `{_response.status_code}`")
    print(f"`requests_url:` error: `{_response.url}`")
    # print(f"`response:` error: `{_response.json()}`")
    deinit_sys_exit()


def fetch_response_from_URL(_url: str) -> requests.Response | None:
    """Match response from `_url`.

    Description:
        Filters status code in the process of fetching `_url`.

    Notes:
        I plan/planned on making each status code messsage individual; I haven't
        found a smart way of doing that yet.

    Exceptions:
        System exit if response status code is not in the range of an acceptable value.

    Parameters:
        `_url`: Url query as a `str` type

    Return:
        `requests.Response` / response object from which `content` is derived.
    """

    response = requests.get(_url)

    # Sources: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    # Informational response
    if 100 <= response.status_code < 199:
        display_requests_error(response)

    # Successful responses
    elif 200 <= response.status_code < 299:
        # display_requests_error(response)
        return response

    # Redirectional message
    elif 300 <= response.status_code < 399:
        display_requests_error(response)

    # Client error response
    elif 400 <= response.status_code < 499:
        if response.status_code != 404:
            display_requests_error(
                response,
                preface=f"Assuming your VPN and internet settings are fine, this is a bug (sorry).",
            )
        print(
            "That word doesn't exist yet. You can try adding it on urbandictionary.com!"
        )
        deinit_sys_exit()

    # Server error
    elif 500 <= response.status_code < 599:
        display_requests_error(
            response,
            preface=f"Got a server error. Somethings wrong with the website. (error {response.status_code})",
        )
        deinit_sys_exit()
    else:
        print(response.status_code)
        print(
            "This is quite rare, but assuming you're connected to the internet, 'urbandictionary.com' seems to be down!"
        )
        deinit_sys_exit()


def get_first_definition_from_soup(_soup: BeautifulSoup) -> Tag:
    """Return first definition section / 'block' from `_soup`.

    Parameters:
        _soup: `_soup` object as `BeautifulSoup` object.

    Return:
        definition as a `Tag`
    """

    definition = get_result_set_from_soup(_soup, _index=0)
    return definition


def get_soup_object_from_word(_word: str) -> BeautifulSoup | None:
    """Return soup object as `BeautifulSoup` from `_word`.

    Raises:
        TypeError if the response or response content is not a valid type.

    Parameters:
        `_word`: Word to query urban dictionary for.

    Return:
        BeautifulSoup object assuming no exceptions were raised.
        None object if things don't work out well. (this is a joke. None doesn't ever get returned.)
        None is for the LSP to make it happy, content and feel warm inside.
    """

    URL_QUERY = f"https://www.urbandictionary.com/define.php?term={_word}"
    response = fetch_response_from_URL(URL_QUERY)

    if not isinstance(response, requests.Response):
        deinit_sys_exit()
        raise TypeError("Response not valid type (get_soup_object_from_word")

    response_content = response.content

    if not isinstance(response_content, bytes):
        deinit_sys_exit()
        raise TypeError("Response content not valid type (get_soup_object_from_word)")

    _soup = BeautifulSoup(response_content, "html.parser")
    return _soup


def get_result_set_from_soup(_soup: BeautifulSoup, _index=0) -> Tag:
    """Return result set from `_soup` object.

    Parameters:
        _soup: `_soup` object as `BeautifulSoup`.
        _index (still being implemented): Definition priority / how high definition is on page - ascending. (default=0)

    Return:
        result_set as a Tag  type (beautifulsoup)
    """

    assert_soup_and_index_valid(_soup, _index)
    result_set = _soup.select(".word")[_index]

    return result_set


def assert_index_valid(_index: int) -> None:
    """Helper function for assert_soup_and_index_valid.

    Parameters:
        _index (still being implemented): Definition priority / how high definition is on page - ascending. (default=0)

    Raises:
        Type error if `_index` is not an integer.
        PendingDeprecationWarning if `_index` is greater than 0.

    Return:
        None
    """

    if not isinstance(_index, int):
        raise TypeError("Index should be an integer")

    if _index > 0:
        raise PendingDeprecationWarning(
            "Index parameter is introduced in > 1.1.0. If you are on an eariler release this is an experimental command."
        )


def assert_soup_valid(_soup: BeautifulSoup) -> None:
    """Helper function for assert_soup_and_index_valid.

    Parameters:
        _soup: `_soup` object as `BeautifulSoup`

    Raises:
        TypeError as a warning if `_soup` is not of type `BeautifulSoup`

    Return:
        None
    """

    if not isinstance(_soup, bs4.BeautifulSoup):
        Warning(
            TypeError(f"_soup must be of type `BeautifulSoup`, found {type(_soup)}")
        )
        deinit_sys_exit()


def assert_soup_and_index_valid(
    _soup: bs4.BeautifulSoup | None, _index: int | None = 0
) -> None:
    """This code is used more than once - prevents violating DRY (don't repeat yourself)

    Parameters:
        _index (still being implemented): Definition priority / how high definition is on page - ascending. (default=0)
        _soup: `_soup` object as `BeautifulSoup`

    Return:
        Literal[True] if `_soup` and `_index` are both valid.
        None if either `soup` or `index` are not valid
    """

    if not isinstance(_soup, bs4.BeautifulSoup) and _soup is not None:
        raise TypeError(
            f"Soup should be either None or BeautifulSoup object (found {type(_soup)})"
        )
    else:
        assert_soup_valid(_soup) if _soup is not None else (
            assert_index_valid(_index) if _index is not None else None
        )


def get_found_word_from_soup(_soup: bs4.BeautifulSoup, _index=0) -> str:
    """Return word from `_soup` object.

    Parameters:
        _index (still being implemented): Definition priority / how high definition is on page - ascending. (default=0)
        _soup: `_soup` object as `BeautifulSoup` object.

    Raises:
        IndexError if the definition is out of the range of the tag object.
        KeyError if the .word tag is not in the soup object.

    Return:
        Word from soup object as a string value.
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

    Parameters:
        _soup: `_soup` object as `BeautifulSoup`
        _index: definition priority / how high definition is on page - ascending. (default=0)
                Please note that index is still something that is being implemented.

    Returns:
        `Tag` containing definition, date, author, definition example.
    """

    assert_soup_and_index_valid(_soup, _index)
    word_meaning = _soup.select(".definition")[_index]

    return word_meaning


def derive_meaning_as_tag(_soup: BeautifulSoup) -> Tag:
    """Return derived meaning from `_soup` object.


    Parameters:
        _soup: `_soup` object as `BeautifulSoup`

    Returns:
        Word meaning as `Tag`.
    """

    assert_soup_and_index_valid(_soup, _index=None)
    derived_definition = derive_definition_as_tag(_soup)
    word_meaning = derived_definition.select(".meaning")[0]

    return word_meaning

def derive_example_as_tag(_soup: BeautifulSoup) -> Tag:
    """Return derived example from `_soup` object.


    Parameters:
        _soup: `_soup` object as `BeautifulSoup`

    Returns:
        Word example as `Tag`.
    """

    assert_soup_and_index_valid(_soup, _index=None)
    derived_definition = derive_definition_as_tag(_soup)
    word_meaning = derived_definition.select(".example")[0]

    return word_meaning

def get_hyperlinks_as_result_set(_word_meaning: Tag) -> ResultSet[Tag] | None:
    """Get hyperlinks as a result set of all unique tags.

    Exceptions:
        returns None if no links are present. (rare but possible)

    Raises:
        TypeError if result set is not of type `ResultSet`.
        Doesn't check for contents of `ResultSet`.

    Parameters:
        return value of derive_meaning_as_tag function.

    Returns:
        (resultset) list of tags or `None` if no links are present
    """

    hyperlinks: None | ResultSet[Tag] = _word_meaning.select(".autolink")

    if hyperlinks is None:
        return None
    elif isinstance(hyperlinks, ResultSet):
        return hyperlinks

    raise TypeError(f"expected ResultSet, got {type(hyperlinks)}")


def format_words_as_string_from_tag(
    _word_meaning: Tag, _hyperlinks_list: list[str]
) -> str | None:
    """Format words into one printable string from `_tag`

    Parameters:
        _word_meaning: Tag containing word definition
        _hyperlinks_list: List of strings that are also hyperlinks in definition

    Returns:
        returns either none or a string/list of strings.
    """


    # all words, can be all links though, which is a pain.
    break_formatted_definition = insert_newline_for_break_tags(_word_meaning.__str__())
    # word_meaning_format_breaks = insert_newline_for_break_tags(_word_meaning.strings)
    words = BeautifulSoup(break_formatted_definition, "html.parser").get_text(strip=False).split(" ", -1)

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


@deprecated("Likes and dislikes are rendered via javascript")
def get_statistics_from_soup(_soup: BeautifulSoup):
    """Return likes and dislikes (both integers) as a dictionary.

    Description:
        Prints out any contributor element sibling elements for debug purposes.

    Notes:
        Function is deprecated.

    Parameters:
        _soup: `_soup` object as `BeautifulSoup` object.

    Exceptions:
        Raises TypeError if contributor is not a `Tag` or `NavigableString`
        Raises TypeError if contributor_element_sibling is not a `Tag`

    Return:
        Likes and dislikes (both integers) as a dictionary.
    """

    # get definition container
    container = derive_definition_as_tag(_soup)
    contributor = container.find_next("div", class_="contributor")
    if not isinstance(contributor, Tag | NavigableString):
        raise TypeError("Contributor is None (get_statistics_from_soup)")
    else:
        contributor_element_sibling = contributor.find_next_sibling(
            "div", attrs={"class": "text-xs"}
        )
        if not isinstance(contributor_element_sibling, Tag):
            raise TypeError(
                "Contributor elements sibling is not of valid type (get_statistics_from_soup)"
            )
        else:
            print(
                contributor_element_sibling.find_all(
                    name="span", recursive=True, attrs={"class": "text-xs"}
                )
            )


def get_author_from_soup(_soup: BeautifulSoup) -> str:
    """Return author from soup.

    Parameters:
        _soup: `_soup` object as `BeautifulSoup` object.

    Return:
        author as a string
    """

    # get definition container
    container: ResultSet[Tag] = derive_definition_as_tag(_soup)  # pyright: ignore

    return (
        container.find_next("div", class_="contributor")  # pyright: ignore
        .find_next("a")["href"]
        .split("=")[1]
        .replace("%20", " ", -1)
    )


def fetch_word_from_remote(_word: str) -> dict[str, str] | None:
    """Query urban dictionary for `_word`.

    Parameters:
        `_word`: Word to query urban dictonary for.
        `_definition`: Definition rank. The greater the number the less likely it'll be found.

    Return:
        Result, author and date as a dictionary.
        "And `None`" (apparently) - pyright.
    """

    _soup = get_soup_object_from_word(_word)

    if not isinstance(_soup, BeautifulSoup):
        display_requests_error(preface="Soup is None (fetch_word_from_remote)")
        return

    # NOTE Is of type `Tag` - word_meanign contains author, date, definition
    word_meaning = derive_meaning_as_tag(_soup)
    word_example = derive_example_as_tag(_soup)

    definition_hyperlinks_list = []
    example_hyperlinks_list = []

    # Returns (most of the time) a list of tags
    definition_hyperlinks = get_hyperlinks_as_result_set(word_meaning)
    example_hyperlinks = get_hyperlinks_as_result_set(word_example)

    # NOTE: returns list of strings that are links
    if definition_hyperlinks is not None:
        # iterate through found definition meaning
        for word in definition_hyperlinks:
            definition_hyperlinks_list.append(word.string)
    # NOTE: returns list of strings that are links
    if example_hyperlinks is not None:
        # iterate through found definition meaning
        for word in example_hyperlinks:
            example_hyperlinks_list.append(word.string)

    words_as_str = format_words_as_string_from_tag(word_meaning, definition_hyperlinks_list)
    example_as_str = format_words_as_string_from_tag(word_example, example_hyperlinks_list)

    if not isinstance(example_as_str, str) or example_as_str == "":
        example_as_str = "Definition not found or not available."
        print(f"Debug (example_as_str variable): {example_as_str}")
    else:
        example_as_str = insert_space_after_chars(list(example_as_str))

    if not isinstance(words_as_str, str) or words_as_str == "":
        words_as_str = "Definition not found or not available."
        print(f"Debug (words_as_str variable): {words_as_str}")
    else:
        words_as_str = insert_space_after_chars(list(words_as_str))

    # Return definition, author, date all as dict
    post_author = get_author_from_soup(_soup)

    # TODO/FIXME return date as well
    return {"definition": words_as_str, "example": example_as_str, "author": post_author, "date": "Unknown"}



def insert_space_after_chars(text: list[str], char: str = ".") -> str:
    """
    Detects if a letter immediately follows a character and inserts a space after the character.

    This function is generally used for grammatical correctness.

    Parameters:
    - text (list[str]): The input text to process.
    - char (str): The character to replace any spaces after.

    Returns:
    - str: The modified text with spaces inserted after `char`
    """

    for n in range(0, len(list(text)) - 1):
        if text[n] == char and text[n + 1] != " ":
            text.insert(n + 1, " ")
    return "".join(text)


def insert_newline_for_break_tags(text: str) -> str:
    """Returns `text` but the line break tags are replaced with \n

    Parameters:
    - text (str): The input text to process.

    Returns:
    - str: The modified text with \n replacing <br>
    """

    # There's a better way of doing it with regex but i dont' care atm
    text = text.replace("<br></br>", "\n")
    text = text.replace("<br />", "\n")
    text = text.replace("<br/>", "\n")
    text = text.replace("<br>", "\n")

    return text


def main():
    """main as global function called from dunder condition.

    Description:
        Fetches and prints definition, author and date.

    Raises:
     - Warning if words is None
     - TypeError if dictionary is invalid

    Returns:
    - None
    """

    word = join_words()

    if not isinstance(word, str):
        raise Warning("Words is none. This shouldn't be getting raised.")
    return_dict = fetch_word_from_remote(word)

    if not isinstance(return_dict, dict):
        raise TypeError(
            "Invalid type getting returned. Should be dictionary (function=main())"
        )

    # NOTE _ = `date`
    definition, example, author, _ = return_dict.values()

    rich_print(f"[bold]{word}: [/bold]", end="")
    print(definition, end="\n\n")

    print(colorama.Style.BRIGHT+f"{example}"+colorama.Style.RESET_ALL)

    rich_print(f"\n[bold]by [italic]{author}[/italic][/bold]")
    # rich_print(f"[bold][/bold]")

    deinit_sys_exit()


if __name__ == "__main__":
    main()
