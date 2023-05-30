"""
=====
Urban
=====

_Hurban the Urban till your brain starts hurtin._

*Herben (verb)*: To look up a definition on the _'Dictionary of Urban'_.

About the file
--------------
The main file acts as an entry point for _Urban_.
It functions as a centralized location from which the API can be utilized.

:Author: Joshua Rose
:Version: 2.0.0 of 2023/05/28
:License: `Apache 2.0 <https://gh-syn.github.io/urban-cli/license.html>`_
:File: __main__.py.py
"""

from argparse import ArgumentParser

from loguru import logger

from urban_api import send_phrase_request
from urban_commands import add_cols_argument
from urban_commands import add_result_argument, add_word_argument
from urban_commands import return_argument_parser
from urban_definition import Definition


def main():
    """
    Entry point that utilizes the parser and API for Urban.

    Raises will not be stipulated as there are too many.
     > Furthermore, it would be silly.
    """

    logger.debug("Instantiating parser object from `return_argument_parser()`")
    parser: ArgumentParser = return_argument_parser()

    logger.debug("Adding commands to parser (cols, word, result)")
    # Add commands to `parser`.
    add_cols_argument(parser)
    add_word_argument(parser)
    add_result_argument(parser)

    logger.debug("Parsing commands with `parse_args()`")
    # Parse newly added commands.
    args = parser.parse_args()

    logger.debug("Sending phrase request")
    # Ask urban dictionary for our word.
    soup = send_phrase_request(args.WORD)

    # NOTE: debugging purposes *ONLY* ...
    definition_object: Definition = Definition(soup=soup, order=args.result)
    logger.debug("Tag fetched")

    # NOTE: and this as well is debug only!
    print(definition_object.definition)

    logger.debug("stringify stuff done")


if __name__ == "__main__":
    main()
