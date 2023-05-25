About the Wiki
==============

You're probably thinking:

*"Why do you have hundreds of lines of code?"*

*"Why don't you split it up into different files?"*

And those are all great questions!

To answer both simultaneously, splitting this program up into different files is something that is generally considered good practice.
With that said, there are certain situations that may prevent you from doing this. This program is one of those situations.

This Wiki addresses topics that cannot be fully explained in repository files.

Topics
------

These topics are as follows.

1. Contribution practices pertaining to documentation, code formatting and git practices.
2. Semantic versioning as it pertains specifically to this project
3. Current and future development plans.

Documentation
-------------

As you'll likely recall in ``installation.sh``, only one file is added to path. If there are multiple files, everything gets really bizarre
and difficult to handle with relative imports. While it's *technically* possible, it's not worth the effort when code could work fine with just one file.

The most convenient part of all of this is configuring the documentation. The scale of the main file, despite how large, can be automatically documented as such.
It's for this reason I don't feel the need to split this documentation into sections, nor do I feel the need to make additional ``rst`` documentation.


Theme
-----

For those wondering about the theme, it's in the footer, but I'll mention it here as well. I'm using Sphinx to generate the documentation and markup that you see here.


Thank You 💛
------------

Thank you for looking at, and or using urban cli. It has been a pleasure working on it and crafting it's development.

