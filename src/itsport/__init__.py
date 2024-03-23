
import sys
import argparse
import logging
from . import main2

__project_name__ = "itsport"

def parse_arguments():
   parser = argparse.ArgumentParser()
   parser.add_argument('--dir', type=str, required=True, help='Directory containing PNG files')
   parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
   return parser.parse_args()

def setup_logging(verbose=False):
   log_level = logging.DEBUG if verbose else logging.INFO
   logging.basicConfig(level=log_level, format='%(levelname)s: %(message)s')

def main() -> int:
   args = parse_arguments()
   setup_logging(args.verbose)
   exif_data = main2.get_exif_data(args.dir)
   out = main2.render_output(exif_data)
   sys.stdout.write(out)
   return 0

