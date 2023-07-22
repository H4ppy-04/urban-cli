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
import sys

from loguru import logger
from rich import print
import rich

from urban_api import send_phrase_request
from urban_commands import add_cols_argument, add_verbose_argument
from urban_commands import add_result_argument, add_word_argument
from urban_commands import return_argument_parser
from urban_definition import Definition
from urban_utils import format_sentences


def main():
    """
    Entry point that utilizes the parser and API for Urban.

    Raises will not be stipulated as there are too many.
     > Furthermore, it would be silly.
    """

    # Remove all handlers added so far, including the default one.
    logger.remove()

    logger.debug("Instantiating parser object from `return_argument_parser()`")
    parser: ArgumentParser = return_argument_parser()

    logger.debug("Adding commands to parser (cols, word, result)")

    # Add argument groups
    output_group = parser.add_argument_group(
        "output", "configure and customize console output"
    )

    # Add commands to output
    add_word_argument(parser)
    add_result_argument(parser)
    add_cols_argument(output_group)
    add_verbose_argument(output_group)

    # Parse newly added commands.
    args = parser.parse_args()

    if args.verbose:
        logger.add(sys.stderr, level="DEBUG")
    else:
        logger.add(sys.stderr, level="WARNING")

    # logger.debug(args.result)

    # Ask urban dictionary for our word.
    soup = send_phrase_request(args.WORD)

    definition_object: Definition = Definition(soup=soup, order=args.result)

    # logger.debug(definition_object)

    rich.print("Definition\n==========")

    print(
        format_sentences(
            definition_object.definition_string, max_length=args.cols
        ),
        end="\n\n",
    )

    rich.print("Example\n=======")

    print(
        format_sentences(
            definition_object.example_string, max_length=args.cols
        ),
        end="\n\n",
    )
    # Print the definition example
    print(f"Defined by [cyan]{definition_object.author}")


if __name__ == "__main__":
    main()
