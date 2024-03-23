import argparse
import sys

from . import main2

__project_name__ = "itsport"


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dir", type=str, required=True, help="Directory containing PNG files"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_arguments()
    out = main2.render_template("extended.j2", data=args)
    sys.stdout.write(out)
    return 0
