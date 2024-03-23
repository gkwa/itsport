
import sys
import argparse
from . import main2

__project_name__ = "itsport"

def parse_arguments():
   parser = argparse.ArgumentParser()
   parser.add_argument('--dir', type=str, required=True, help='Directory containing PNG files')
   return parser.parse_args()

def main() -> int:
   args = parse_arguments()
   exif_data = main2.get_exif_data(args.dir)
   out = main2.render_output(exif_data)
   sys.stdout.write(out)
   return 0

