.. |check| raw:: html

    <input checked=""  type="checkbox">

.. |check_| raw:: html

    <input checked=""  disabled="" type="checkbox">

.. |uncheck| raw:: html

    <input type="checkbox">

.. |uncheck_| raw:: html

    <input disabled="" type="checkbox">


Rework
======

.. Note::

   The rework is basically almost finished. The remaining tasks are as follows:


   |uncheck_| Paragraphs between definition, example and author.

   |uncheck_| Highlighting

This project is being completely rebuilt from the ground up for the following reasons.

Modularity
-----------
The current code is monolithic, in that all code is stored in one file.
This causes severe technical debt for the future, and hinders the agility by which
the software can potentially be developed with.

Scalability
-----------
Separate modules to split the functionality of a codebase is not only good practice, but also
beneficial for scalability. By introducing different modules for things like data-classes, IO handling,
formatting data structures, and so on, sections of code can be visualized and split up, reducing complexity overhead.
