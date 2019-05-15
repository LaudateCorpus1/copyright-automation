# -*- coding: utf-8 -*-

"""Console script for copyright_automation."""
import sys
import argparse


def parse_args(args):
    """Returns parsed commandline arguments.
    """

    parser = argparse.ArgumentParser(description="Commandline interface for copyright_automation")
    parser.add_argument("--foo")
    return parser.parse_args(args)


def main():
    """Console script for copyright_automation."""
    parse_args(sys.argv[1:])
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
