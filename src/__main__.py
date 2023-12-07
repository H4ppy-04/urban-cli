"""
:Copyright: 2023 Joshua Rose
:Version: 2.0.0 of 2023/05/28
:File: __main__.py.py
"""

import argparse
import sys

from request import Request
from definition import Definition


def build_argument_parser():
    parser = argparse.ArgumentParser(
        prog="urban",
        description="Search the Urban Dictionary",
        epilog=None,
        add_help=True,
        allow_abbrev=True,
    )
    parser.add_argument(
        "--verbose",
        default=False,
        required=False,
        help="Show additional debug info",
        action="store_true",
    )
    parser.add_argument(
        "--result",
        type=int,
        help="Get the nth definition result",
    )
    parser.add_argument(
        "--all",
        required=False,
        default=False,
        help="Show all definition information",
        action="store_true",
    )
    parser.add_argument(
        "--example",
        required=False,
        default=True,
        help="Show example usage of the word",
        action="store_true",
    )
    parser.add_argument(
        "--author",
        required=False,
        default=True,
        help="Show the definition author",
        action="store_true",
    )
    parser.add_argument(
        "--rating",
        required=False,
        default=True,
        help="Show the like/dislike ratio of the definition",
        action="store_true",
    )
    parser.add_argument(
        "--date",
        required=False,
        default=True,
        help="Show the date the definition was published",
        action="store_true",
    )
    parser.add_argument(
        "word",
        type=str,
        help="Search the Urban Dictionary",
    )
    return parser


def main():
    parser = build_argument_parser()
    args = parser.parse_args()
    request = Request(args.word)
    results = request.search()

    if not len(results):
        Definition.show_does_not_exit_error(args.word)
        sys.exit()

    if args.result:
        if args.result - 1 > len(results):
            print(f"Index value for --result too high ({len(results.definitions)} results)")
            sys.exit(1)
        results[args].display(args.example, args.author, args.rating, args.date)
        sys.exit(0)
    results[0].display(args.example, args.author, args.rating, args.date)

if __name__ == "__main__":
    main()
