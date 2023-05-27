Documentation
-------------

This page covers each function in the program and what it does. Its main purpose is to help contributors understand the code.

.. py:function:: join_words(words)
   :noindex:


   Joins multiple words into a single string.


   :raises IndexError: If no words are specified or the list is empty

   :param words: A list of one or more words into the interpreter.
   :return: A string that merges one or more words together.

The `join_words` function is seldom but still of high importance.
It's useful for when one or more words are entered into the command line.

For example, if ``urban foo bar`` was entered, ``foo bar`` would
be converted into a string and treated as one word. This is ideal because when querying a word,
if multiple words can be concatenated in the search query, then we can be confident that we'll receive
a correct and accurate response.

.. py:function:: deinit_sys_exit(exit_code)
   :noindex:


   Resets `colorama` and raises `SystemExit` to exit the program.


   :raises TypeError: If `exit_code` is not an integer a `TypeError` is raised.
   :param exit_code: A number passed into `sys.exit` that raises an error code to `System`.

   :return: `None`


This function is used, mainly as a practice of `DRY`_\. First, it removes any pre-existing formatting on the command line.
This means that if the program printing colored text, it will revert the font style to its default state before existing.
This is then followed by an exit call, reason being, a raised `SystemExit` can be tested.

.. py:function:: fetch_response_from_URL(_url, _response)
   :noindex:

   Filters status code in the process of fetching `_url`.

   :raises SystemExit: if response status code is not in the range of an acceptable value.

   :param preface: If an error occurs, this will be used to provide additional context.

   :param _url: Url query as a `str` type
   :param _response: If the response code is already known

   :return: `requests.Response` / response object from which `content` is derived.

This function matches the response from `url`.
I originally plan/planned on making each status code message individual. I haven't
This can also been seen to some extent in the actual library, see `status_codes <https://github.com/psf/requests/blob/main/requests/status_codes.py>`_.
Please note that individual error message handling for ``requests.Response`` objects have yet to be implemented.

.. py:function:: display_requests_error(_response, preface)
    :noindex:


    Handles and displays formatted output from a `requests.Response` object.

    :raises SystemExit: If `response.status_code` or `_response` is not in the standard range.

    :param response: A `requests` response object, assumedly one that is unexpected.
    :param preface: If an error occurs, this will be used to provide additional context.

    :return: `integer`

This function handles requests response values that exceed a given range.
This is used in conjunction with ``fetch_response_from_URL`` and is called when the response
doesn't match response code `200`.

..
    Links and stuff. don't touch

.. _DRY: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3886731/#s5title
.. _codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
