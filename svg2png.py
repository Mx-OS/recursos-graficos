#!/usr/bin/env python3

import argparse
import os
import sys
import cairosvg
import xml.etree.ElementTree as ET

def parse_svg_dimensions(file_path):
    """Parsea el ancho y alto desde el archivo SVG si no se especifican por línea de comandos."""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        width = root.get("width")
        height = root.get("height")

        # Remueve unidades como 'px' si están presentes
        if width and width.endswith("px"):
            width = width.replace("px", "")
        if height and height.endswith("px"):
            height = height.replace("px", "")

        return int(float(width)) if width else None, int(float(height)) if height else None
    except Exception as e:
        print(f"⚠️ Advertencia: No se pudo parsear dimensiones del SVG: {e}")
        return None, None

def main():
    parser = argparse.ArgumentParser(
        description="Convierte un archivo SVG a PNG usando cairosvg"
    )
    parser.add_argument("input_svg", help="Ruta al archivo de entrada .svg")
    parser.add_argument("-O", "--output", help="Ruta del archivo de salida .png (opcional)")
    parser.add_argument("-W", "--width", type=int, help="Ancho del PNG (en píxeles)")
    parser.add_argument("-H", "--height", type=int, help="Alto del PNG (en píxeles)")
    args = parser.parse_args()

    input_path = args.input_svg
    if not os.path.isfile(input_path):
        print(f"❌ Error: El archivo '{input_path}' no existe.")
        sys.exit(1)

    output_path = args.output or os.path.splitext(input_path)[0] + ".png"

    width = args.width
    height = args.height

    # Si no se especificaron dimensiones, intenta leerlas del SVG
    if width is None or height is None:
        svg_width, svg_height = parse_svg_dimensions(input_path)
        width = width or svg_width
        height = height or svg_height

    try:
        cairosvg.svg2png(
            url=input_path,
            write_to=output_path,
            output_width=width,
            output_height=height
        )
        print(f"✅ Convertido: {input_path} → {output_path} ({width}x{height})")
    except Exception as e:
        print(f"❌ Error al convertir SVG a PNG: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
