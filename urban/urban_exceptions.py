"""
Contains custom exceptions.
"""


class InvalidStatusCodeError(Exception):
    """
    Custom exception raised when a status code is invalid.

    :attr code: The invalid status code.
    """

    def __init__(self, code):
        """
        Initialize the InvalidStatusCodeError instance.

        :param code: The invalid status code.
        """

        self.code = code

    def __str__(self):
        """
        Return a string representation of the exception.

        :return: A string indicating the invalid status code and the required valid codes.
        """

        return f"Invalid status code: {self.code}. Must be 200 or 404."


class InvalidOrderError(Exception):
    """
    Custom exception raised when an order is greater than the definitions found for a word.

    :attr order: The invalid order number.
    """

    def __init__(self, order):
        """
        Initialize the InvalidOrder instance.

        :param order: The invalid order number.
        """

        self.order = order

    def __str__(self, definitions=0) -> str:
        """
        Return a string representation of the exception.

        :param definitions: The amount of definitions that have been found.
        :return: A string indicating the invalid order number and the amount of found orders.
        """

        match definitions:
            case 0:
                return f"Invalid order: {self.order} (no definitions found)"
            case 1:
                return f"Invalid order: {self.order} (found 1 definition)"
            case _:
                return f"Invalid order: {self.order} (found {definitions} definitions)"


class InvalidWordError(Exception):
    """
    Custom exception raised when a word doesn't exist.

    :attr word: The word in question
    """

    def __init__(self, word):
        """
        Initialize the InvalidWordError instance.

        :param word: The invalid word.
        """

        self.word = word

    def __str__(self) -> str:
        """
        Return a string representation of the exception.

        :return: A string indicating the word is invalid.
        """

        return f"{self.word} is not a valid word"
