#!/bin/bash
# Copyright © 2014 Martin Ueding <dev@martin-ueding.de>

set -e
set -u

for resolution in 1920x1200 1680x1050 1280x1024 1024x768
do
    convert Martin-X220.png -resize $resolution^ -gravity Center -crop $resolution+0+0 +repage Test-$resolution.png
done
