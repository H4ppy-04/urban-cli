"""
:Author: Joshua Rose
:Version: 2.0.0 of 2023/05/28
:License: `Apache 2.0 <https://gh-syn.github.io/urban-cli/license.html>`_
:File: urban_commands.py

The commands file contains individual command implementations for usage in the API.
It's practicality lies in modularizing the code through the use of functions.
"""

import argparse


def return_argument_parser():
    """
    Get argument parser.

    :return: Argument parser.
    :rtype: `ArgumentParser`
    """

    parser = argparse.ArgumentParser(
        prog="urban",
        description="Search the Urban Dictionary!",
        epilog=None,
        add_help=True,
        allow_abbrev=False,
    )

    return parser


def add_word_argument(
    parser: argparse.ArgumentParser | argparse._ArgumentGroup,
):
    """
    Add word argument to `parser`.

    :param parser: Command parser object.
    :raise TypeError: if `parser` is not of type `argparse.ArgumentParser`.
    """

    if not isinstance(
        parser, argparse.ArgumentParser | argparse._ArgumentGroup
    ):
        raise TypeError("Argument parser must be of type `ArgumentParser`")

    parser.add_argument(
        "WORD",
        type=str,
        help="Search the Urban Dictionary for a definition",
    )


def add_cols_argument(
    parser: argparse.ArgumentParser | argparse._ArgumentGroup,
):
    """
    Add column width argument to `parser`.

    Specifies the width of the column.
    For example, if the width was 10, then it look like (see below)

    the quick b
    rown fox...

    :param parser: Command parser object.
    :raise TypeError: if `parser` is not of type `argparse.ArgumentParser`.
    """

    if not isinstance(
        parser, argparse.ArgumentParser | argparse._ArgumentGroup
    ):
        raise TypeError("Argument parser must be of type `ArgumentParser`")

    parser.add_argument(
        "--cols",
        default=150,
        nargs=1,
        type=int,
        required=False,
        help="Adjust the definition column width - defaults to 150",
    )


def add_result_argument(parser: argparse.ArgumentParser):
    """
    Add result argument to `parser`.

    This command indexes a definition by ranking.
    For example, if the index value was 1, it would return the 1st definition and so on...

    :param parser: Command parser object.
    :raise TypeError: if `parser` is not of type `argparse.ArgumentParser`.
    """

    if not isinstance(
        parser, argparse.ArgumentParser | argparse._ArgumentGroup
    ):
        raise TypeError("Argument parser must be of type `ArgumentParser`")

    # ➡️➡️➡️ TODO➡️➡️➡️➡️  -1 returns all definitions!
    parser.add_argument(
        "--result",
        type=int,
        help="Retrieve a corresponding definition  - defaults to 1st result",
    )


def add_verbose_argument(
    parser: argparse.ArgumentParser | argparse._ArgumentGroup,
):
    """
    Add verbose argument to `parser`.

    This command prints more verbose output.
    For example, it would use the loguru module to give helpful debugging information.

    :param parser: Command parser object.
    :raise TypeError: if `parser` is not of type `argparse.ArgumentParser`.
    """

    if not isinstance(
        parser, argparse.ArgumentParser | argparse._ArgumentGroup
    ):
        raise TypeError("Argument parser must be of type `ArgumentParser`")

    parser.add_argument(
        "--verbose",
        default=False,
        required=False,
        help="Show more information for debugging and tracing",
        action="store_true",
    )
