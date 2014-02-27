#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2014 Martin Ueding <dev@martin-ueding.de>

import argparse
from PIL import Image
from PIL import ImageFont, ImageDraw

__docformat__ = "restructuredtext en"

def main():
    options = _parse_args()

    im = Image.open('flow.jpg')

    draw = ImageDraw.Draw(im)

    # use a truetype font
    font = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-R.ttf", 30)

    draw.text((10, 25), "world", font=font)

    im.show()


def _parse_args():
    """
    Parses the command line arguments.

    If the logging module is imported, set the level according to the number of
    ``-v`` given on the command line.

    :return: Namespace with arguments.
    :rtype: Namespace
    """
    parser = argparse.ArgumentParser(description="")
    #parser.add_argument("args", metavar="N", type=str, nargs="*", help="Positional arguments.")
    #parser.add_argument("", dest="", type="", default=, help=)
    #parser.add_argument("--version", action="version", version="<the version>")
    parser.add_argument("-v", dest='verbose', action="count", help='Enable verbose output. Can be supplied multiple times for even more verbosity.')

    options = parser.parse_args()

    # Try to set the logging level in case the logging module is imported.
    try:
        if options.verbose == 1:
            logging.basicConfig(level=logging.INFO)
        elif options.verbose == 2:
            logging.basicConfig(level=logging.DEBUG)
    except NameError as e:
        pass

    return options

if __name__ == "__main__":
    main()
