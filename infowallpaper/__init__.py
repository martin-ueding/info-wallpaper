#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2014 Martin Ueding <dev@martin-ueding.de>

import argparse
import configparser
import subprocess
from PIL import Image
from PIL import ImageFont, ImageDraw

__docformat__ = "restructuredtext en"

def main():
    options = _parse_args()

    devices = configparser.ConfigParser()
    devices.read('hardware.ini')

    ubuntu_regular = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-R.ttf", 30)
    ubuntu_bold = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-B.ttf", 30)


    for device in devices:
        if device == 'DEFAULT':
            continue

        print(device)

        filename = 'flow.jpg'

        im = Image.open(filename)
        draw = ImageDraw.Draw(im)

        x_pos = 100
        y_pos = 100

        draw.text((x_pos, y_pos), device, font=ubuntu_bold)
        y_pos += 10

        for component in ['CPU', 'RAM', 'GPU', 'HDD', 'OS', 'Resolution']:
            if not component in devices[device]:
                continue
            y_pos += 35
            draw.text((x_pos, y_pos), component, font=ubuntu_regular)
            draw.text((x_pos + 180, y_pos), devices[device][component], font=ubuntu_regular)

        im.save(device + '.png')


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
