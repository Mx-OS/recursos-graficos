# Lista de archivos SVG en el directorio actual
SVGS := $(wildcard *.svg)

# Para cada archivo SVG, define el PNG correspondiente en output/
PNGS := $(patsubst %.svg,output/%.png,$(SVGS))

# Regla principal
all: $(PNGS)

# Asegura que la carpeta output/ exista antes de exportar PNGs
output/%.png: %.svg | output
	python ../svg2png.py "$<" -W 500 -H 500 -O "$@"

# Regla para crear la carpeta output si no existe
output:
	mkdir -p output

# Regla para limpiar todos los archivos generados
clean:
	rm -rf output
