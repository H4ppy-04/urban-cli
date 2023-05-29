"""
Centralized urban file that is calls the API.
"""

from argparse import ArgumentParser

from urban_api import send_phrase_request
from urban_commands import add_cols_argument, add_word_argument
from urban_commands import return_argument_parser


def main():
    parser: ArgumentParser = return_argument_parser()

    # Add commands to `parser`.
    add_cols_argument(parser)
    add_word_argument(parser)

    # Parse newly added commands.
    args = parser.parse_args()

    # Ask urban dictionary for our word.
    send_phrase_request(args.WORD)

if __name__ == "__main__":
    main()
