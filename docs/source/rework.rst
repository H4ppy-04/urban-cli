Rework
======

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
