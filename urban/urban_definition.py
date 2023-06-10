"""
==========
Definition
==========

:Author: Joshua Rose
:Version: 2.0.0 of 2023/05/28
:License: `Apache 2.0 <https://gh-syn.github.io/urban-cli/license.html>`_
:File: urban_definition.py

To prevent monolithic code practices, I've decided to seperate the definition class,
which previously existed in `urban_utils.py` and let it have it's own file.

This decision came about as a result of the size that the file ended up taking, which wasn't
anticipated in its genesis.
"""

from datetime import datetime

from bs4 import Tag
from loguru import logger

from urban_exceptions import InvalidOrderError
import urban_utils


class Definition:
    def __init__(
        self,
        example: str | None = None,
        date: datetime = datetime.now(),
        **kwargs,
    ):
        """
        Definition class to manage defitions easier.

        It's times like these when I really wish I was using rust.

        :param example: The definition usage / example
        :param author: Username of definition OP
        :param date: datetime object
        :param definition: The main definition string

        **kwargs: Kwargs such as soup objects, order, etc ...
        """

        self.example = example
        """Definition example as listed inside of `soup` - can be `None` or `str`"""

        self.date = date
        """Date as a `datetime` object"""

        self.kwargs = kwargs
        """Kwargs can contain soup object, order, etc ..."""

        self.definition_results = self.get_definition_results()
        """All definitions found (as html) for 'soup' defined in kwargs"""

        # Specific defenition from property
        # self._definition = self.definition
        """Specific definition from property `definition`"""

        self.definition = self.get_definition_order(order=kwargs["order"])

        # Get author div
        self.author_div: Tag = self.definition.find_next(
            "div", class_="contributor"
        )

        # Format definition once author has been found
        self.definition_string = self.get_formatted_definition()
        """ Definition as a readable string - can be printed """

        # Derive author from author div
        self.author = [i for i in self.author_div.stripped_strings][1]

        # TODO: optimize this:
        self.date = [i for i in self.author_div.stripped_strings][2]
        """The author of `definition` - derived from `soup`"""

    def get_formatted_definition(self) -> str:
        """
        Retrieves and formats a definition object from HTML.

        :return: A string representation of the formatted definition object.
        """

        definition_div: Tag = self.definition.find_next("div", class_="meaning")
        definition_div_stripped_list = list(definition_div.stripped_strings)
        definition_joined_words = " ".join(definition_div_stripped_list)
        definition_gramaticised = urban_utils.remove_punctuation_spacing(
            definition_joined_words
        )

        return definition_gramaticised

    def get_definition_results(self):
        """
        Get definition result from a soup object.
        > Warns if no result index has been specified.

        :raise IndexError: If soup has not been provided in `kwargs`.
        :raise InvalidOrderError: If the order/result_index is greater than the number of definitions.
        :return: `ResultSet` array or `Tag` found from soup.
        """

        if "soup" not in self.kwargs.keys():
            raise IndexError("Soup has not been provided in `kwargs`.")

        soup = self.kwargs["soup"]
        soup_results = soup.find_all("div", class_="definition")

        return soup_results

    def get_definition_order(self, order):
        """
        Returns an html phrase from all definitions that have been found.

        :return: *specific* definition html from array of html definitions.
        """

        # Get definition results from index
        logger.debug(f"order: {self.kwargs['order']}")
        if "order" in self.kwargs.keys():
            if self.kwargs["order"] == None:
                logger.warning("No result number specified")
                order = 0
            else:
                order = self.kwargs["order"] - 1

        # Raise `InvalidOrderError` if `order` is greater than definitions found
        if order > len(self.get_definition_results()):
            raise InvalidOrderError(len(self.get_definition_results()))

        return self.definition_results[order]
