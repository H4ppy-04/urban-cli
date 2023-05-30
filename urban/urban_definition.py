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

        raw_soup = kwargs["soup"]
        order = kwargs["order"]

        filtered_soup_results = raw_soup.find_all("div", class_="definition")

        # NTS: `selected_definitions` is much smaller than `filtered_soup_results` 🙂
        self.selected_definitions = filtered_soup_results[order - 1]
        definitions_found = len(raw_soup.select(".definition"))

        if order > definitions_found:
            raise InvalidOrderError(definitions_found)

        # Instance-specific properties
        self._definition = self.definition

    @property
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, value):
        self._definition = value

    @definition.getter
    def definition(self):
        return (self.selected_definitions.select(".meaning")[0],)
