"""
========
Commands
========

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
        usage="usage line here...",
        description="Search the Urban Dictionary!",
        epilog=None,
        add_help=True,
        allow_abbrev=False,
    )

    return parser

def add_word_argument(parser: argparse.ArgumentParser):
    """
    Add word argument to `parser`.

    :param parser: Command parser object.
    :raise TypeError: if `parser` is not of type `argparse.ArgumentParser`.
    """

    if not isinstance(parser, argparse.ArgumentParser):
        raise TypeError("Argument parser must be of type `ArgumentParser`")

    parser.add_argument(
        "WORD",
        type=str,
        help="Search the Urban Dictionary for a definition",
    )

def add_cols_argument(parser: argparse.ArgumentParser):
    """
    Add column width argument to `parser`.

    :param parser: Command parser object.
    :raise TypeError: if `parser` is not of type `argparse.ArgumentParser`.
    """

    if not isinstance(parser, argparse.ArgumentParser):
        raise TypeError("Argument parser must be of type `ArgumentParser`")

    parser.add_argument(
        "--cols",
        default=150,
        nargs=1,
        type=int,
        help="Adjust the definition column width",
    )
