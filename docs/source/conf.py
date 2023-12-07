# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(1, os.path.abspath("../../src"))
sys.path.insert(2, os.path.abspath("../../src/"))

html_theme = "press"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
    "myst_parser",
    "sphinx.ext.todo",
]

# paths that contain templates, *relative* to this file.
templates_path = ["_templates"]

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

# The master toctree document (without the file extension)
master_doc = "index"

project = "urban-cli"
copyright = "2024 Joshua Rose"
author = "Joshua Rose"

version = "1.0.2"
language = "en"
html_static_path = ["_static"]
