# Versioning
This project follows [semantic versioning website](https://semver.org ). If you are interested about the release process of this project, it is 'suggested reading' before looking at this page.

This project is not an API. As such, it uses a 'modified' versioning system in which versioning components are representative of similar things.
Most branches retain the same functionality except for the major branch. This is because it's impossible to have a backwards compatible change if you're not developing a library.
However, a backwards compatible change in this case, would be considered something like removing a command or function in favor of a new one. Another example might be deprecating a function in favor of a new one.
This would all be considered a 'breaking change' and would rightly warrant incrementing the major branch.
