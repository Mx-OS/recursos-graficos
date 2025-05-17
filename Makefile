# Fundación MX OS
#       (o_
#  (o_  //\
#  (/)_ V_/_
#

# Directorio donde se colocarán los archivos de salida (PDF y PNGs)
OUTPUT_DIR = output

# Encuentra todos los archivos SVG en source/assets/
SVG_FILES = $(wildcard source/assets/*.svg)

# Define los nombres de los archivos PNG equivalentes para cada SVG
# Ejemplo: source/assets/logo.svg -> source/assets/logo.png
PNG_FILES = $(patsubst source/assets/%.svg,source/assets/%.png,$(SVG_FILES))

# Define objetivos "falsos" que no representan archivos físicos
.PHONY: all clean

# Objetivo por defecto: genera PNGs desde los SVGs y luego compila el PDF
all: $(PNG_FILES)
	make -C source latexpdf                # Ejecuta `make latexpdf` dentro del directorio source/
	mv source/_build/latex/*.pdf $(OUTPUT_DIR)/  # Mueve el PDF generado al directorio de salida

# Crea el directorio de salida si no existe
$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

# Regla para convertir un archivo SVG a PNG usando Inkscape
# $< representa el archivo de entrada (SVG)
# $@ representa el archivo de salida (PNG)
source/assets/%.png: source/assets/%.svg | $(OUTPUT_DIR)
	inkscape $< -e $@                      # Usa Inkscape para convertir SVG a PNG

# Regla para limpiar: elimina el directorio de salida y los archivos temporales generados por Sphinx
clean:
	rm -rf $(OUTPUT_DIR)                  # Elimina el directorio output/
	make -C source clean                  # Limpia la carpeta build/ de Sphinx
