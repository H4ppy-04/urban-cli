Documentation
-------------

This page covers each function in the program and what it does. Its main purpose is to help contributors understand the code.

.. autofunction:: urban.join_words

The `join_words` function is seldom but still of high importance.
It's useful for when one or more words are entered into the command line.

For example, if ``urban foo bar`` was entered, ``foo bar`` would
be converted into a string and treated as one word. This is ideal because when querying a word,
if multiple words can be concatenated in the search query, then we can be confident that we'll receive
a correct and accurate response.

.. autofunction:: urban.deinit_sys_exit

This function is used, mainly as a practice of `DRY`_\. First, it removes any pre-existing formatting on the command line.
This means that if the program printing colored text, it will revert the font style to its default state before existing.
This is then followed by an exit call, reason being, a raised `SystemExit` can be tested.

.. autofunction:: urban.fetch_response_from_URL

This function matches the response from `url`.
I originally plan/planned on making each status code message individual. I haven't
This can also been seen to some extent in the actual library, see `status_codes <https://github.com/psf/requests/blob/main/requests/status_codes.py>`_.
Please note that individual error message handling for ``requests.Response`` objects have yet to be implemented.

.. autofunction:: urban.display_requests_error

This function handles requests response values that exceed a given range.
This is used in conjunction with ``fetch_response_from_URL`` and is called when the response
doesn't match response code `200`.

..
    Links and stuff. don't touch

.. _DRY: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3886731/#s5title
.. _codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
