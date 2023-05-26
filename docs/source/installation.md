# Installation

```sh
python -m pip install --user -r requirements.txt
```
> All platforms must install requirements before running.

## Linux

On Linux platforms, run `sh install.sh`.
Please note that this assumes that ~/.local/bin/ is present. This folder should contain your user-level executable files / links to executable files.
The installation script creates a link to `urban.py`, and adds it to your `.bashrc`. The installation script also assumes that `.bashrc` is located in 
your default home directory (denoted via `~`). 

## Windows
Windows will have to run `usage.py` directly, as installation is not currently available with pip.
If you don't want to have to run `usage.py` directly, _which I'm assuming you don't_, then you'll likely have to add `urban.py` to your path.
From there you'll have to type `python urban.py` instead of simply `urban`. The exception being you've installed WSL; through which you can run `install.sh`.

## Mac
There is no current support for Apple distributions.
