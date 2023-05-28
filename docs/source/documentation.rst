Documentation
-------------

This page covers each function in the program and what it does. Its main purpose is to help contributors understand the code.

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
