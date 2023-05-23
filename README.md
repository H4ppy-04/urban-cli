<div align="center">

  <h1>Urban CLI</h1>

   <a href="_blank">
     <img
          width="64px"
          alt="book icon"
          src="https://github.com/GH-Syn/urban-cli/blob/main/.github/images/book.png"/></a>
    <br>
  <code>A command line interface for the infamous <a href="https://www.urbandictionary.com/">Urban Dictionary</a></code>
</div>



## Installation

__All platforms__

All platforms must install requirements before running.
 > This won't be needed in the next planned release for Linux and WSL.

Windows will have to run `usage.py` directly, as urban-cli is not installable via pip, however there are [alternatives](https://github.com/GH-Syn/urban-cli/edit/main/README.md#windows).

```sh
python -m pip install --user -r requirements.txt
```

#### Linux

On Linux platforms, run `sh install.sh`.
> This assumes that ~/.local/bin is present

#### Windows
> If you don't want to run `usage.py` directly

For Windows, you'll have to manually modify your path environment variables to add:
`%USERPROFILE%/Downloads/urban-cli/src/urban.py`

From there you'll have to type `urban.py` instead of `urban`.
The exception of course is you've installed WSL through which you can run `install.sh`.

## Usage

<img alt="usage example" src="https://github.com/GH-Syn/urban-cli/blob/main/.github/images/output-2023-05-23_16.06.38.gif"/></img>

## License

This project is licensed under the common MIT license, the details of which you'll find in `LICENSE` in the repository files.
