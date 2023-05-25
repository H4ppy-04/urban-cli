# Contributing
Thank you for considering contributing to this code. As always, there are certain guidelines that I recommend you follow. This of course, is advised and not strictly enforced. **Your contribution will still be looked at regardless of the standard of code.**

## Formatting

This project is formatted using the 'Black' code style. All formatting is followed as stipulated in python's pep documentation.

### Imports

Imports are structured through `pyright` and follow pep linting conventions. For a brief summary, all *internal* libraries that are part of Python's standard libraries are imported first, followed by external dependencies, finally followed by local imports.

#### Imports Example
```python
# Stdlib packages
import os
import sys
import math

# External dependencies
import numpy
import pandas

# Local files
import my_local_module_a
import my_local_module_b
import my_local_module_c
```

### Comments

Comments are seldom reached (generally) in most of the codebase, regarding in-line comments. Doc-strings however, are very common. All of these things should be consistent so that code is readable and debug-able. 

#### Inline comments
1. If the column with will remain under 79 chars with an inline comment, you must ensure that there is two white spaces between the code and the comment.

```python
print("The five leaping wizards...")  # Why do they leap?
                                  # ^ two spaces before comment
```
> Ignore the second line; it's for showing where the spaces are.

2. If the column width will exceed 79 chars, even when placed above the line, make it a doc-string as follows in the next section.



#### Multi-line comments
```python
class API(Controller):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        for i in a:
            """
            The quick brown fox
            """
            if len(a) + len(b) == c:
                raise Warning("Some stupidly specific warning")
```
> This is for demonstration. Don't do even half the things you see here.

Otherwise, if it doesn't exceed the column width you can simply do an in-line comment. The only thing to consider 

### Linting Standards and `LSP` usage

Regarding auto-linting, you can use whatever `LSP` you want, however some may differ in the way that they lint things. If you want to minimize the possibility of merge conflicts, the majority of commits in this codebase are defined by the 'black' code-style and linted with `pyright` (`pyright` imports as well). 


## Git
Git on the other hand, is much more important than `LSP` usage, linting practices and comments. The reason for this, is that it is _very_ hard to re-write commits. To re-write or go back on a commit without losing any progress when you're hundreds of commits into a codebase is a challenge that even Linus Torvalds himself would find daunting. It is for this reason that it is absolutely, very much important, that you stick to this section's policy as closely as possible, because it greatly helps the efficiency of indexing, bisecting, stashing, grepping, and a whole lot more things that would be very hard with inconsistent and or reduced effort with Git.
 
### Commits

The commit structure is very simple. You effectively just have to replace the template with whatever you have.

```markdown
type(scope): subject

This commit introduces / changes / implements ...

(any additional comments)

Issue: #1, #2, ...
Pull Request: #3, #4, ...
Related commit: c5n23f9, ad9f219
Tag: v1.9.3

Authored-by: John Smith <johnsmith@yourprovider.com>
```
#### Implementing a commit template locally
As to not copy and paste a string of text or  manually type out / memorize a template (although memorization might actually be preferable in this case), git features a global configuration option for setting the commit. The alternative is editing your git configuration manually, however, the former will be easier in most cases.
```sh
git config --global commit.template path/to/commit-template.txt
```

### Pull Requests

Pull requests are less of a problem, but following the template provided is ideal:

```markdown
## Pull Request

### Description
[Provide a brief description of the changes introduced by this pull request.]

### Motivation and Context
[Explain the motivation behind the changes. What problem does this pull request solve?]

### Changes Made
[List the specific changes made in this pull request. Be as detailed as possible.]

### Related Issues
[Reference any related issues or tickets by mentioning their numbers or providing relevant links.]

### Testing Done
[Describe the testing performed to validate the changes. Include any steps, commands, or test cases.]

### Screenshots or Recordings (if applicable)
[Attach any relevant screenshots, recordings, or visual representations of the changes made.]

### Checklist
- [ ] I have reviewed my code and ensured it follows the project's coding standards.
- [ ] I have tested my changes and verified that they work as intended.
- [ ] I have added appropriate documentation or updated the existing documentation.
- [ ] I have reviewed the diff to ensure only the intended changes are included.
- [ ] I have assigned reviewers to this pull request.

### Additional Notes
[Include any additional information, considerations, or instructions for reviewers or future maintainers.]
```

### Branches

For branches, you can generally have the following options:

#### `docs/branch-name`
If the branch pertains to documentation such as the wiki, a `readme` file, any images or resources that might need to be added, a license, contributing file and so on, this is the branch that it will come under. Typically, you will never need to make a docs branch if you are only introducing a small commit, but commits greater than 10 lines should typically have their own branch.

#### `feat/branch-name`
For any medium-large feature that will need likely revision before its integrated, the feature branch will be prefixed with `feat`. This is the most common type of branch, and using this is probably your best call if your not sure.

#### `fix/branch-name`
If a bug is listed in issues this is the branch you'll be using. It'll most likely already be created because each issue has its own branch regardless of the size. Normally this isn't good practice, but because release-notes actions aren't configured, I want to be able to list comprehensive bug-fixes in the release notes automatically.

Please note that if it's not listed in issues, make an issue and request a branch be made for it. 
