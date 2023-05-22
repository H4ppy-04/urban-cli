#!/usr/bin/env python
#
# Author: Joshua Rose <joshuarose099@gmail.com>
# License: MIT


import sys

from bs4 import BeautifulSoup as bs, ResultSet, Tag
import colorama
from loguru import logger
import requests

logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")

colorama.init()

word = ""

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

# TODO get `_definition` working
def fetch_word_from_remote(_word: str, _definition: int | float = 0) -> dict[str, str] | None:
    """Query urban dictionary for `_word`.

    :param `_word`: Word to query urban dictonary for.
    :param `_definition`: Definition rank. The greater the number the less likely it'll be found.
    :returns: result, author and date as a dictionary.
    """

    # NOTE: remove in actual release; refactor _definition type to `int`
    # for more argument types even though its strictly useless.
    if isinstance(_definition, float):
        _definition = int(_definition)

    # get request
    URL_QUERY = f"https://www.urbandictionary.com/define.php?term={_word}"
    response = requests.get(URL_QUERY)

    # print(response.status_code)
    match response.status_code:
        case 404:
            print("That word doesn't exist yet. You can try adding it on urbandictionary.com!")
            colorama.deinit()
            sys.exit(0)
        case 200:
            pass
        case _:
            print(
                "This is quite rare, but assuming you're connected to the internet, 'urbandictionary.com' seems to be down!"
            )
            colorama.deinit()
            sys.exit(1)

    # Format query
    soup = bs(response.content, "html.parser")

    # print(soup.prettify())

    # TODO add to test:
    """
    initial_definition = soup.find(
        "div",
        class_="definition",
        recursive=True
    )

    # ensure result's found
    assert isinstance(initial_definition, NavigableString | Tag)
    """

    found_word = soup.select(".word")[0].string
    if found_word is None:
        print("Crazy stuff happened")
        colorama.deinit()
        sys.exit(0)

    # TODO: move to test
    assert _word.lower() == found_word.lower()

    # REM: expects string from found_word
    word_meaning = soup.select(".definition")[0].select(".meaning")[0]

    hyperlinks_list = []

    # Returns (most of the time) a list of tags
    hyperlinks: None | ResultSet[Tag] = word_meaning.select(".autolink")

    # NOTE: returns ['nVIDIA', 'to card', 'nForce', 'ATi']
    if hyperlinks_list is not None:
        # iterate through found definition meaning
        for word in hyperlinks:
            hyperlinks_list.append(word.string)

    # all words, can be all links though, which is a pain.
    words = word_meaning.get_text(strip=False).split(" ", -1)
    words_as_str = " ".join(words)

    # print(hyperlinks_list)

    for _, word in enumerate(hyperlinks_list):
        if word in words:
            words_as_str = words_as_str.replace(word, colorama.Fore.BLUE + word + colorama.Fore.RESET)
            # print(f" (dev stuff) Replaced: {word}")
            continue
        else:
            # Houston, we got a problem.
            # print("[dev issue] unfound word? the word is \'{word}\'".format(word=word))
            if " " in word:
                # print("Subword found")
                subwords = word.split(" ", -1)
                for subword in subwords:
                    word = words_as_str.replace(subword, colorama.Fore.BLUE + subword + colorama.Fore.RESET)
            # word_count = word.count(" ")
            # _words = word.split(" ", word_count)
            # Get the index of the first word
            # words[index] = f"{colorama.Fore.BLUE}test{colorama.Fore.RESET}"

            # sys.exit(1)
            # colrama.deinit()

    # print(" ".join(words))

    # NOTE don't delete!
    print(words_as_str)

    # Return definition, author, date all as dict
    post_author = ""
    date_posted = ""

    # TODO/FIXME return date and author as well
    return {"definition": "", "author": post_author, "date": date_posted}


fetch_word_from_remote(word)
