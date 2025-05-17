#!/usr/bin/env python3

import argparse
import os
import sys
import cairosvg

def main():
    parser = argparse.ArgumentParser(
        description="Convierte un archivo SVG a PNG usando cairosvg"
    )
    parser.add_argument(
        "input_svg",
        help="Ruta al archivo de entrada .svg"
    )
    parser.add_argument(
        "-O", "--output",
        help="Ruta del archivo de salida .png (opcional, por defecto reemplaza la extensión)"
    )
    parser.add_argument(
        "-W", "--width",
        type=int,
        help="Ancho del PNG resultante (en píxeles)"
    )
    parser.add_argument(
        "-H", "--height",
        type=int,
        help="Alto del PNG resultante (en píxeles)"
    )

    args = parser.parse_args()

    input_path = args.input_svg

    if not os.path.isfile(input_path):
        print(f"❌ Error: El archivo '{input_path}' no existe.")
        sys.exit(1)

    output_path = args.output
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".png"
    try:
        cairosvg.svg2png(
            url=input_path,
            write_to=output_path,
            output_width=args.width,
            output_height=args.height
        )
        print(f"✅ Convertido: {input_path} → {output_path}")
    except Exception as e:
        print(f"❌ Error al convertir SVG a PNG: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
