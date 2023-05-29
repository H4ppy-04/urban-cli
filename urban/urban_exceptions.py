"""
### Meta & Licensing
__File__: `urban_exceptions.py`
__License__: [Apache 2.0](https://gh-syn.github.io/urban-cli/license.html)
__Author__: Joshua Rose <joshuarose099@gmail.com>

### Module Description

Contains custom exception handlers.

This module handles custom exceptions specific to urban cli.
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
