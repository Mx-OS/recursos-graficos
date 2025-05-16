# Lista de archivos SVG en el directorio actual
SVGS := $(wildcard *.svg)

# Para cada archivo SVG, define el PNG correspondiente en output/
PNGS := $(patsubst %.svg,output/%.png,$(SVGS))

# Regla principal
all: $(PNGS)

# Asegura que la carpeta output/ exista antes de exportar PNGs
output/%.png: %.svg | output
	inkscape "$<" -e "$@" --export-width=500 --export-height=500

# Regla para crear la carpeta output si no existe
output:
	mkdir -p output

# Regla para limpiar todos los archivos generados
clean:
	rm -rf output
