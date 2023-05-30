# Contributing
Contributions are welcome and highly appreciated and as such, guidelines are not enforced, rather simply recommendations. 

## Formatting

This project is formatted using the [Black](https://pypi.org/project/black/) code style. All formatting is followed as stipulated in python's pep documentation.
[Black](https://pypi.org/project/black/) is not a part of `requirements.txt` and as such, needs to be installed manually.
Installation is fairly straightforward and is typically done as follows. Please refer to the [refactoring guide](refactoring_guide.md) for more information on formatting and refactoring.

```sh
exec python -m pip install --user black
```
> For a global installation, omit the `--user` parameter

## Commits

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

### Implementing a commit template locally
As to not copy and paste a string of text or manually type out / memorize a template (although memorization might actually be preferable in this case), git features a global configuration option for setting the commit. The alternative is editing your git configuration manually, however, the former will be easier in most cases.
```sh
git config --global commit.template path/to/commit-template.txt
```

## Branches

For branches, you can generally have the following options:

### `docs/branch-name`
If the branch pertains to documentation such as the wiki, a `readme` file, any images or resources that might need to be added, a license, contributing file and so on, this is the branch that it will come under. Typically, you will never need to make a docs branch if you are only introducing a small commit, but commits greater than 10 lines should typically have their own branch.

### `feat/branch-name`
For any medium-large feature that will need likely revision before its integrated, the feature branch will be prefixed with `feat`. This is the most common type of branch, and using this is probably your best call if you're not sure.

### `fix/branch-name`
If a bug is listed in issues this is the branch you'll be using. It'll most likely already be created because each issue has its own branch regardless of the size. Normally this isn't good practice, but because release-notes actions aren't configured, I want to be able to list comprehensive bug-fixes in the release notes automatically.

Please note that if it's not listed in issues, make an issue and request a branch be made for it. 
