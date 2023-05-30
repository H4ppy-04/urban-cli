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

from bs4 import BeautifulSoup

from urban_exceptions import InvalidOrderError


class Definition:
    def __init__(
        self,
        example: str | None = None,
        author: str = "John Doe",
        date: datetime = datetime.now(),
        **kwargs
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

        # Instance variables from constructor
        self.example = example
        self.author = author
        self.date = date
        self.kwargs = kwargs

        # All definitions found for the word
        self.definition_results = self.get_definition_results()

        # Specific defenition from property
        self._definition = self.definition


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

    @property
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, value):
        self._definition = value

    @definition.getter
    def definition(self):
        """
        This property getter returns an html phrase from all definitions that have been found.

        :return: *specific* definition html from array of html definitions.
        """

        # Specific definition from order
        order = 0
        # Get definition results from index
        if "order" not in self.kwargs.keys():
            Warning(
                "No result tag specified. Defaulting to first instance of definition class."
            )
        else:
            order = self.kwargs["order"] - 1

        # Raise `InvalidOrderError` if `order` is greater than definitions found
        if order > len(self.definition_results):
            raise InvalidOrderError(len(self.definition_results))

        return self.definition_results[order]
