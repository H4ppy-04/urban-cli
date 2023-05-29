"""
=====
Utils
=====

:Author: Joshua Rose
:Version: 2.0.0 of 2023/05/28
:License: `Apache 2.0 <https://gh-syn.github.io/urban-cli/license.html>`_
:File: urban_utils.py

This file contains utility functions and helper methods.
It is responsible for the following functions.

Data Manipulation
-----------------
When a request object is received, it needs to be formatted in a way that Python can understand
The beautifulsoup library helps beautifully ✨ with this. It parses html data in a way that can be
read and manipulated very easily.

I/O handling
------------
The argparse library can be thought of as boilerplate level code in addition to a few extra classes
that greatly help building a command line interface. It removes most of the argument logic and lets the
developer focus on what's important. Argparse is used in this file for showing and receiving data.

Common Data Structures
-----------------------
Common data structures such as a date, definition struct, lives in this file.
"""

import argparse

import rich


PARSER = argparse.ArgumentParser(
    prog="Urban",
    description="Get any definition from Urban Dictionary",
    # epilog="Licensed to Joshua Rose with Apache 2.0",
)
# NOTE: parser is a constant, thus is capitalised
"""Parser object as `argparse.ArgumentParser` constant"""


def show_does_not_exit_error(word: str):
    """
    Show does not exist error when invalid word is queried.

    A type error is not raised as data type is checked in `send_phrase_request` function.

    :param word: The invalid word that apparently doesn't exist.
    """

    rich.print("The word %s doesn't exist yet." % word, end=" ")
    rich.print(
        "You can change that by submitting a definition on the {link}".format(
            link="[link url='https://urbandictionary.com/']Urban Dictionary website.[/link]"
        )
    )
