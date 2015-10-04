#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2014-2015 Martin Ueding <dev@martin-ueding.de>

import argparse
import configparser
import os.path
import subprocess

from PIL import Image
from PIL import ImageFont, ImageDraw
import jinja2

__docformat__ = "restructuredtext en"

def main():
    options = _parse_args()

    devices = configparser.ConfigParser()
    devices.read(os.path.expanduser('~/.config/info-wallpaper/devices.ini'))

    env = jinja2.Environment(loader=jinja2.PackageLoader('infowallpaper', 'templates'))
    template = env.get_template('template.html')

    ubuntu_regular = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-R.ttf", 30)
    ubuntu_bold = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-B.ttf", 30)

    components_to_list = [
        'Model', 'CPU', 'RAM', 'GPU', 'HDD', 'SSD',
        'Mainboard', 'PSU',
        'MAC', 'MAC LAN', 'MAC WLAN',
        'OS', 'Key',
        'Resolution', 'Diagonal', 'PPI',
        'Bogomips',
        'Year',
    ]

    with open('export.html', 'w') as f:
        f.write(template.render(devices=devices, ctl=components_to_list))

    for device in devices:
        if device == 'DEFAULT':
            continue

        print('Generating wallpaper for:', device)

        filename = os.path.expanduser(devices[device]['wallpaper'])

        im = Image.open(filename)
        draw = ImageDraw.Draw(im)

        x_pos = int(devices[device]['x_pos'])
        y_pos = int(devices[device]['y_pos'])
        x_offset = int(devices[device]['x_offset'])

        draw.text((x_pos, y_pos), device, font=ubuntu_bold)
        y_pos += int(devices[device]['y_margin'])

        for component in set(devices[device]) - set([x.lower() for x in components_to_list]):
            print('Unknown component:', component)

        for component in components_to_list:
            if not component in devices[device]:
                continue
            y_pos += int(devices[device]['y_step'])
            draw.text((x_pos, y_pos), component, font=ubuntu_regular)
            draw.text((x_pos + x_offset, y_pos), devices[device][component], font=ubuntu_regular)

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
