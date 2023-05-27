Known Issues
============

The following paragraphs detail some of the known issues surrounding the project that are either platform specific bugs, or terminal specific bugs pertaining to fonts and displays.

Fonts and Colorization
----------------------

The current state of the project is fairly stable and performant. From the unit tests that have been written, all of them pass, and raw coverage stays seemingly around the 90% mark.

As for performance regarding the `rich` library, there seems to be some slight discrepancies around formatting visualizations. Formatted text will show as expected on 256 color
terminals, assuming that the font is also compatible. For example, if a regular, bold, and italic fonts have been outlined in the configuration file of the terminal (such as that of `alacritty`), then
the font will seemingly work as expected. The main issue arises when a font that doesn't have an italic style is used to render italic text. This will simply result in the same appearance as if
an initialization function for a color library had not been called in the first place.

Some libraries, such as `colorama`, are very good with compatibility, however because both `colorama` and `rich`
are font libraries being used in tandem with one another, performance may not be as expected if using an in-compatible font. My suggestion, as for most fonts, is to use a Nerd Font. Nerd fonts support
all current features from symbols to italics and are commonly used and recommended by developers and typography enthusiasts alike.

.. Note:: This has been fixed in `#29 <https://github.com/GH-Syn/urban-cli/pull/29>`_

LXML
----

Definition and their explanations/examples will occasionally not link to words. This normally happens when there are duplicate words, or words that aren't flagged by `lxml`.
This issue is currently being investigated and will be updated as soon as a fix is available. See `#28 <https://github.com/GH-Syn/urban-cli/issues/28>`_ for more details.

.. Note:: This has been fixed in `#30 <https://github.com/GH-Syn/urban-cli/pull/30>`_

Text Processing
---------------

Usernames that have characters such as ', @, ", and so on, that are normally replaced with symbols will show up as symbols, or rather, as processed by the browser URL. This is normally because
the username is extracted from a hyperlink reference tag, in which navigates users to a users profile. This can be troubling as spaces can show up as ``%20`` characters, and other strange things.
The text processing issue is actively being worked on. See `#27 <https://github.com/GH-Syn/urban-cli/issues/27>`_ for more details
