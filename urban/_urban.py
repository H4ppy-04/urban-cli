import argparse
import datetime
import sys
import urllib.parse

from bs4 import BeautifulSoup, NavigableString, ResultSet, Tag
import bs4
import colorama
from loguru import logger
import requests
from requests.models import Response
from requests.status_codes import _codes
from rich import print as rich_print

colorama.init()


def display_requests_error(
    _response: requests.Response | None = None,
) -> None:
    """Handle and display formatted output from a `requests.Response` object.

    Description:
        GitHub links are provided when something unexpected happens.

    Parameters:
        response: Requests response, assumedly one that is unexpected
        preface: If the message requires additional explanation. ("" is default)

    Return:
        None; function calls system exit.
    """

    if _response is None:
        rich_print(
            f"It would be amazing if you created an issue at https://github.com/GH-Syn/urban-cli/issues/new"
        )
        rich_print(
            f"Please include any error messages or weirdness that you encountered."
        )
        raise SystemExit

    logger.info(f"Client information response (response code {_response.status_code}).")
    rich_print(
        f"It would be amazing if you created an issue at https://github.com/GH-Syn/urban-cli/issues/new and made sure to include:"
    )
    logger.error(f"`status_code` error: `{_response.status_code}`")
    logger.error(f"`requests_url:` error: `{_response.url}`")
    # print(f"`response:` error: `{_response.json()}`")
    raise SystemExit


def get_error_as_string(_error_code: int):
    """Get error as string from `error_code`.

    Raises:
        Warning: If _error_code is not in `_codes`.

    Parameters:
        `_error_code`: Error code to index requests library error codes.

    Return:
        string: error code string from `_error_code`.
    """

    if _error_code not in _codes.keys():
        raise Warning("Error code not in keys")

    return _codes[_error_code][0]


def fetch_response_from_URL(_url: str) -> requests.Response | None:
    """Match response from `_url`.

    Description:
        Filters status code in the process of fetching `_url`.

    Notes:
        I plan/planned on making each status code message individual; I haven't
        found a smart way of doing that yet.

    Raises:
        System exit if response status code is not in the range of an acceptable value.

    Parameters:
        `_url`: Url query as a `str` type
        `_response`: If the response code is already known

    Return:
        `requests.Response` / response object from which `content` is derived.
    """

    if not isinstance(_url, str):
        raise TypeError

    response = requests.get(_url)

    # Successful responses
    if 200 <= (response.status_code) < 299:
        return response

    if response.status_code == 404:
        print(
            "That word doesn't exist yet. You can try adding it on urbandictionary.com!"
        )
    raise SystemExit


def get_soup_object_from_word(_word: str) -> BeautifulSoup | None:
    """Return soup object as `BeautifulSoup` from `_word`.

    Parameters:
        `_word`: Word to query urban dictionary for.

    Return:
        BeautifulSoup object assuming no exceptions were raised.
    """

    URL_QUERY = f"https://www.urbandictionary.com/define.php?term={_word}"
    response: Response = fetch_response_from_URL(URL_QUERY)  # pyright: ignore

    response_content: bytes = response.content

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
        TypeError: if `_index` is not an integer.
        PendingDeprecationWarning: if `_index` is greater than 0.
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
        _soup: soup object as type `BeautifulSoup`

    Raises:
        TypeError: as a warning if `_soup` is not of type `BeautifulSoup`
    """

    if not isinstance(_soup, bs4.BeautifulSoup):
        raise TypeError(f"_soup must be of type `BeautifulSoup`, found {type(_soup)}")


def assert_soup_and_index_valid(
    _soup: bs4.BeautifulSoup | None, _index: int | None = 0
) -> None:
    """This code is used more than once - prevents violating DRY (don't repeat yourself)

    Parameters:
        _index: (still being implemented) definition priority / how high definition is on page - ascending. (default=0)
        _soup: `_soup` object as `BeautifulSoup`

    Return
    ------
    `boolean`

        True: if `_soup` and `_index` are both valid returns\n
        False: if either `soup` or `index` are not valid\n
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
        _soup: soup as `BeautifulSoup` object.

    Raises:
        IndexError: if the definition is out of the range of the tag object.
        KeyError: if the .word tag is not in the soup object.

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
    """Return the definition of a _soup object.

    Parameters:
        _soup: _soup object as BeautifulSoup
        _index: definition priority / how high definition is on page - ascending. (default=0)
                Please note that index is still something that is being implemented.

    Returns:
        Tag: contains definition, date, author, definition example.
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
        TypeError: if result set is not of type `ResultSet`. It doesn't check for contents of `ResultSet`.

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
        None: if the length of `words` is equal to 0 or 1
        str: If the definition is found to be one word
        list[str]: if the definition is more than one word
    """

    # all words, can be all links though, which is a pain.
    break_formatted_definition = insert_newline_for_break_tags(_word_meaning.__str__())
    # word_meaning_format_breaks = insert_newline_for_break_tags(_word_meaning.strings)
    words = (
        BeautifulSoup(break_formatted_definition, "html.parser")
        .get_text(strip=False)
        .split(" ", -1)
    )

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
                subwords = word.split(" ", word.count(" "))
                for subword in subwords:
                    words_as_str = words_as_str.replace(
                        subword, colorama.Fore.BLUE + subword + colorama.Fore.RESET
                    )
    return words_as_str


def get_author_and_date_from_soup(_soup: BeautifulSoup) -> str | None:
    """Return date from soup.

    Parameters:
        _soup: `_soup` object as `BeautifulSoup` object.

    Return:
        date as a string
    """

    if not isinstance(_soup, BeautifulSoup):
        raise TypeError

    # get definition container
    container: Tag = derive_definition_as_tag(_soup)  # pyright: ignore

    # this gets first definition as tag or navstring presumably.
    author_and_date: NavigableString = container.find_next(
        "div", class_="contributor"
    )  # pyright: ignore
    date = get_post_date_as_datetime(author_and_date)
    # print(author_and_date.getText())

    # type(href_tag) == str .. evals to `True`
    href_tag: str = author_and_date.find_next("a")["href"]  # pyright: ignore
    author: NavigableString = get_author_from_tag(author_and_date)  # pyright: ignore

    # more detailed date
    date_as_string = date.strftime("%B %dth, %Y")
    if "=" in href_tag:
        author: str = href_tag.split("=")[1]

    author = urllib.parse.unquote(author).strip()

    if author_and_date != None:
        return f"by {author} on {date_as_string}"


def get_author_from_tag(tag: Tag) -> str:
    """Get author from tag.

    A (much) cleaner way to get author from tag.

    Raises:
        TypeError: if tag is not `Tag`

    Parameters:
        tag: Tag to get author from

    Return:
        author as a string type.
    """

    if not isinstance(tag, Tag):
        raise TypeError("tag needs to be of type `Tag`.")

    # NOTE TO SELF: fix this shit - i hate looking at it, and i hate myself for writing it
    author = [
        k
        for index, k in enumerate([i for i in tag.text.split(" ") if i != ""])
        if index <= 1
    ][1]
    items = []
    for i in tag.text.split(" "):
        if i != "":
            items.append(i)

    author = []

    if "by" in items:
        items.remove("by")

    for index, k in enumerate(items):
        if index <= 2:
            # print(items[index])
            author.append(k)

    return " ".join(author)


def get_post_date_as_datetime(definition_tag: Tag | NavigableString) -> datetime.date:
    """
    Return datetime object from definition tag

    Raises:
        TypeError: if definition tag is not of type `Tag` or `NavigableString`

    Parameters:
        definition_tag: Tag or NavigableString containing a div html tag and contributor class

    Return:
        `datetime.Date` object from `Tag` or `NavigableString`
    """

    if not isinstance(definition_tag, Tag):
        raise TypeError("Definition tag must be of type `Tag` or `NavigableString`.")

    # This prints tag for first definnition
    # print(definition_tag)
    date_tag_elements: list[str] = [
        i for i in definition_tag.text.split(" ") if i != ""
    ]  # pyright: ignore
    if len(date_tag_elements) >= 3:
        # NOTE this prints the *first* definitions' author
        # print(date_tag_elements)
        month, day, year = date_tag_elements[-3:]
    else:
        logger.critical(date_tag_elements)
        sys.exit(1)
    day = day.replace(",", "", day.count(","))
    month_as_int = datetime.datetime.strptime(month, "%B").month
    post_date = datetime.date(int(year), int(month_as_int), int(day))

    return post_date


def fetch_word_from_remote(_word: str) -> dict[str, str | None] | None:
    """Query urban dictionary for `_word`.

    Parameters:
        `_word`: Word to query urban dictonary for.

    Return:
        Result, author and date as a dictionary.
        "And `None`" (apparently) - pyright.
    """

    _soup = get_soup_object_from_word(_word)

    if not isinstance(_soup, BeautifulSoup):
        display_requests_error()
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

    words_as_str_val: str | None = word_meaning.string
    if words_as_str_val == None:
        words_as_str_val: str | None = format_words_as_string_from_tag(
            word_meaning, definition_hyperlinks_list
        )
    example_as_str: str = format_words_as_string_from_tag(
        word_example, example_hyperlinks_list
    )  # pyright: ignore

    example_as_str = insert_space_after_chars(list(example_as_str))

    if not isinstance(words_as_str_val, str):
        if words_as_str_val is not None:
            words_as_str: str = words_as_str_val.string
            logger.debug(word_meaning)
            logger.critical(f"Debug (words_as_str variable): {words_as_str}")
        else:
            logger.critical("words_as_str == `None`")
            sys.exit(1)
    else:
        words_as_str = insert_space_after_chars(list(words_as_str_val))

    post_author_and_date = get_author_and_date_from_soup(_soup)

    # TODO/FIXME return date as well
    return {
        "definition": words_as_str_val,
        "example": example_as_str,
        "author_and_date": post_author_and_date,
    }


def insert_space_after_chars(text: list[str], char: str = ".") -> str:
    """
    Detects if a letter immediately follows a character and inserts a space after the character.

    This function is generally used for grammatical correctness.

    Parameters:
        text (list[str]): The input text to process.
        char (str): The character to replace any spaces after.

    Returns:
        str: The modified text with spaces inserted after `char`
    """

    for n in range(0, len(list(text)) - 1):
        if text[n] == char and text[n + 1] != " ":
            text.insert(n + 1, " ")
    return "".join(text)


def insert_newline_for_break_tags(text: str) -> str:
    """Returns `text` but the line break tags are replaced with `\n`.

    Parameters:
        text (str): The input text to process.

    Returns:
        str: The modified text with `\n` replacing `<br>`.
    """

    # There's a better way of doing it with regex but i dont' care atm
    text = text.replace("<br></br>", "\n")
    text = text.replace("<br />", "\n")
    text = text.replace("<br/>", "\n")
    text = text.replace("<br>", "\n")

    return text


def format_sentences(text: str, max_length: int) -> str:
    """
    Formats sentences in the given text by starting a new line if a sentence
    exceeds the maximum length. Each line will not exceed the maximum length,
    even if it means breaking a word.

    Args:
        text (str | Tag): The input text containing sentences.
        NOTE: tag can be specified from which data is extracted
        relative to its contents

        max_length (int): The maximum length of a line.

    Returns:
        str: The formatted text with sentences properly line-wrapped.
    """

    if not isinstance(max_length, int):
        raise TypeError("The 'max_length' argument must be an integer.")

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


def main():
    """`main` as global function called from dunder condition.

    Description:
        Fetches and prints definition, author and date.

    Raises:
        `Warning`: if words is None
        `TypeError`: if dictionary is invalid

    Returns:
      `None`
    """

    parser = argparse.ArgumentParser(
        prog="Urban",
        description="Remotely query definitions from the Urban Dictionary",
        epilog="Developed by Joshua Rose",
    )

    parser.add_argument("word", help="Request a definition from the Urban Dictionary")

    # TODO
    """
    parser.add_argument(
        "--index",
        type=int,
        choices=[1, 2, 3],
        default=1,
        help="The index of the definition to fetch 1-3",
    )
    """

    # TODO
    """
    parser.add_argument(
        "--author", type=str, help="List a definition by a given author"
    )
    """

    parser.add_argument(
        "--cols", type=int, default=150, help="Linebreak chars at a given column value"
    )
    args = parser.parse_args()

    word = args.word

    if not isinstance(word, str):
        raise Warning("Words is none. This shouldn't be getting raised.")

    return_dict = fetch_word_from_remote(word)

    if not isinstance(return_dict, dict):
        raise TypeError(
            "Invalid type getting returned. Should be dictionary (function=main())"
        )

    TERMINAL_WIDTH = (
        args.cols if args.cols is not None else parser.get_default(args.cols)
    )

    soup: BeautifulSoup = get_soup_object_from_word(args.word)  # pyright: ignore

    definition, example, author_and_date = return_dict.values()
    formatted_definition = ""
    if isinstance(definition, str):
        formatted_definition = format_sentences(definition, TERMINAL_WIDTH)
    if formatted_definition == "" or definition is None:
        formatted_definition = "No definition specified 🤕"

    formatted_word = format_sentences(word, TERMINAL_WIDTH)

    rich_print(f"[bold]{formatted_word}: [/bold]", end="")

    print(formatted_definition)  # word

    if not isinstance(example, str):
        example = "No example provided."
    else:
        example = format_sentences(example, TERMINAL_WIDTH)

    print(colorama.Style.BRIGHT + f"\n{example}\n" + colorama.Style.RESET_ALL)

    rich_print(f"[bold][white]{author_and_date}[/white][/bold]")

    raise SystemExit


if __name__ == "__main__":
    main()
