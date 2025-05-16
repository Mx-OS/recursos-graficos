#!/bin/bash
# Genera los archivos PNGs a partir de los svgs existentes.
# Requiere inkscape

for svg in *.svg; do
    base_name="./pngs/${svg%.svg}"
    inkscape "$svg" -e "${base_name}.png" --export-width=500 --export-height=500
done
