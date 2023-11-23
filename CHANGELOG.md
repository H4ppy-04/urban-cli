# Changelog

All notable changes to this project will be documented in this file.

## [unreleased]

### Bug Fixes

- Change executable permissions for install

### Documentation

- Attempt 2 ( docs pipeline )
- Reduce verbosity of docstrings

### Features

- Add structs file; modify documentation

### Miscellaneous Tasks

- Ignore universal ctags
- Add todo feat

### Refactor

- Make pipeline more relevant from fbff7cc

### Wip

- Attempt at getting pages to work again

## [1.1.1] - 2023-08-07

### Bug Fixes

- Add edge case chars to formatter
- Apostrophe character whitespace error
- Remove redundant warning log
- Add `?` to spacing index utility, fixes #74
- Fixes cols argument, closes #59
- Add instance check, closes #78
- Relative imports

### Documentation

- Add tasks to rework page

### Features

- Implements optimized logging args
- Display example below definition
- Add spacing between paragraphs (#80)

### Miscellaneous Tasks

- Checked of `todo` item
- Revoke coverage from index
- Update todo

### Refactor

- Remove releases in favour of e383a03

### Styling

- Limit column width to 80 chars
- Minor formatting changes
- Align documentation strings to `80`
- Format code with black linter

### Testing

- Fixed pytest configuration

### Implement

- Add type checks for tests

### Pyenv

- Ignore local version

### Types

- Fixed typecheck issue

## [1.1.0] - 2023-06-03

### Bug Fixes

- Instance properties order
- Instance properties order
- Fix `remove_punctuation_spacing` bug
- Fix parser issue for periods
- Fix `remove_punctuation_spacing` bug
- Fix parser issue for periods
- Fix definition object issue
- Fix `ImportError`
- `NameError` bug for multiple params on input
- Fix `--result` functionality, `--order` warns
- Fixes punctuation spacing for backticks

### Documentation

- Add rework, merge about.rst and index.rst
- Add file docstrings
- Add documentation for api
- Add documentation index
- Add rework, merge about.rst and index.rst
- Important developmeent note
- Add refactoring guide
- Add documentation for api
- Add rework, merge about.rst and index.rst
- Important developmeent note
- Add documentation for api
- Add documentation for api
- Add rework, merge about.rst and index.rst
- Add documentation for api
- Add refactoring guide

### Features

- Implement invalid word exception
- Add `--verbose` functionality
- Pytest unit configuration
- Add type tests
- Add smoke tests
- Add working tests
- Implement `pytest.ini`, edit `.gitignore`
- Adds argparse and url request functions
- Add tests for commands
- Invalid order class
- NOW WE ARE COOKING!
- Result filter, dataclass, result parse works
- Wotd definition, refactor definition
- Implement invalid word exception
- Add `--verbose` functionality
- Remove book icon
- Fix logger warning `urban_definition`
- Remove book icon
- Fix logger warning `urban_definition`
- Add formatting to output for definition
- Add `--cols` formatting argument

### Miscellaneous Tasks

- Lint files
- Show error function, additional parser.
- Refactor function return
- Lint files
- Lint files with black code-style lint
- Lint files with black code-style lint
- Ignore constructor file imports
- Organize imports constructor

### Refactor

- Definition
- Help menu, refactors, docstring stubs
- Rename urban, fix relative imports
- Rename src to urban on imports
- Exception handling
- Definition
- Help menu, refactors, docstring stubs
- Omit redundant module imports
- Omit `urban.py` file
- Omit redundant module imports
- Omit `urban.py` file
- Delete duplicate in `src` folder
- Delete old unit tests
- Delete deprecated functions
- Remove un-used variable in `__main__.py`
- Remove dead code

### Implement

- Author hyperlink reference 'extractor'
- Url handling, custom exception
- Author hyperlink reference 'extractor'
- Add grammar function, checks string var
- Add grammar function, checks string var

## [1.0.2] - 2023-05-30

### Bug Fixes

- Remove duplicate row
- Add consecutive headers
- Example not provided edge case
- Refactor test datta
- Test data
- Test data (x2)
- Test data
- Test data
- Test data
- License reference

### Documentation

- Update 1.0.1 roadmap
- Refactor versioning
- Add deprecated admonition
- Add file docstrings
- Add documentation for api
- Add documentation index
- Correct typo in contributing
- Correct typo in contributing
- Add refactoring guide

### Features

- Import contributing from docs
- Add bug and feature template(s)
- Create SECURITY.md stub file
- Add .coveragerc to ignore tests
- `urllib` decode on word input
- Add tests for word input decoder
- Add todo
- Add note about contributing
- Add todo
- Add note about contributing
- Fix test data
- Loguru testing
- Add `-sv` to actions
- Boilerplate argparse parser
- `--cols` command functionality integration
- Format words as string tests; black
- License
- Link to license
- Link to license
- License implementation
- Update default column width
- Pytest unit configuration
- Add type tests
- Add smoke tests
- Add working tests
- Implement `pytest.ini`, edit `.gitignore`
- Adds argparse and url request functions
- Add tests for commands
- Invalid order class
- NOW WE ARE COOKING!
- Result filter, dataclass, result parse works
- Wotd definition, refactor definition

### Miscellaneous Tasks

- Add documentation head
- Remove .coveragerc, run coverage
- Omit
- Rm code_of_conduct
- Tick off contributing
- Omit actions file
- Check off todo items
- Blacken code
- Show error function, additional parser.
- Refactor function return

### Refactor

- Shorten contributing
- Refactored release table
- Refactored release table
- Seperate release page
- Update code from wiki
- Introduce new test data
- Sphinx autofunction
- Comment bracket on arguments
- Priority table; add 1.1.0
- Omit dead code
- Relocate releases
- Remove redundant argument from function
- Omit preface output unit test
- Project about page
- Omit redundant code
- Update documentation
- Change hyperlink casing
- Rename urban, fix relative imports
- Rename src to urban on imports
- Exception handling

### Styling

- Reformat requirements by criteria

### Implement

- `--cols` parameter for argparse
- Url handling, custom exception

## [1.0.1] - 2023-05-27

### Bug Fixes

- Attempts to fix release drafter not working
- Format release notes
- Definition mismatch
- Remove required system args
- Add check for log folder

### Documentation

- Add note on requests

### Features

- Add status code referencing
- Add roadmap
- Toggle release status for 1.0.0
- Add loguru instance
- Add loguru dependency to requirements
- Installs dependencies when installer run
- Omit scaffolds
- Omit scaffolds

### Miscellaneous Tasks

- Grammar fix
- Blacken code
- Upload coverage
- Upload coverage
- Blacken code

### Refactor

- Version note
- Refactor roadmap layout
- Remove redundant tests
- Remove test stubbing
- Remove static tests
- Remove unused imports
- Remove unused imports

### Revert

- [**breaking**] Revert release drafter

## [1.0.0] - 2023-05-27

### Bug Fixes

- Correct spelling error
- Chmod executable in bin
- Error code handling for url
- Space issue. easiest fix of my life holy shit
- Space issue. easiest fix of my life holy shit
- Update labeler.yml
- Grammar issue regarding parsing of strings
- Break substitution (#20)
- Spacing input bug
- Test data
- Python-app.yml
- Docstrings

### Documentation

- Add preface to readme referring to wiki
- Add preface to readme referring to wiki
- Resolves issues
- Refactor type to rst

### Features

- Readme document and assets
- Add image and document title
- Add usage and license section
- Add license file
- Add .gitignore file
- Add installer and uninstaller
- Add usage instructions
- [**breaking**] Works 🎉, closes #1
- Refactors, type safety, tests
- GIF demonstration of tool
- Add gif demo
- Add video to readme
- Refactor documentation 
- Show author with definition
- Show author with definition
- Add github actions testing
- Add failing CI
- Initial testing of labeler configuration
- Create stale.yml
- Add github actions testing
- Add failing CI
- Initial testing of labeler configuration
- Create stale.yml
- Initial commit for release drafter
- Show definition example
- New/updated demo video with more features
- Formatting
- Add coverage
- Upload coverage
- Update codecov.yml
- Update codecov.yml
- Update codecov.yml
- Additional tests
- Additional coverage
- Update sphinx theme
- Add documentation markdown
- Create sphinx.yml
- Type checks
- Add word concat test
- Add requests and response unit tests
- Tests entry point
- Coverage page
- Refactor about page
- Refactor
- Installation
- Refactor readme
- Installation
- Omit coverage
- Update release-drafter.yml
- Add date next to author; lint
- Add additional documentation
- Documentation, fix index error

### Miscellaneous Tasks

- Add note for dependency installation
- Removes dependencies from requirements
- Fix code indentation
- Add dependencies
- Add parser library as dependency
- Add dependencies
- Add parser library as dependency
- Add setup.py

### Refactor

- Breaking html to markdown
- Split platform sections
- Rename project -> urban cli
- Dependency cleanup
- Formatting strings, test refactors
- Switch statements to if statement
- Additional return types
- Comment deprecated function
- Comment deprecated function
- Omit duplicate functions
- Omit duplicate functions
- Modularized unit and integ testing
- Docstrings and instance checks
- Blacken code
- Test data
- Relocate readme sections
- Delete test_urban.py
- Link
- Update wiki
- Modifications to index algorithm
- Date and author tags
- Requests test case

### Testing

- Result set unit

<!-- generated by git-cliff -->
