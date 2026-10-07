# Makefile maestro para recursos gráficos de Fundación MxOS
#
#       (o_
#  (o_  //\
#  (/)_ V_/_
#

OUTPUT_DIR = output
SVG2PNG = python3 svg2png.py
SPHINXBUILD = sphinx-build

# Archivos SVG del manual en source/assets/
MANUAL_SVGS = $(wildcard source/assets/*.svg)
MANUAL_PNGS = $(patsubst source/assets/%.svg,source/assets/%.png,$(MANUAL_SVGS))

.PHONY: all logo wallpapers diagramas propuestas manual-html clean

# Objetivo por defecto: compilar logotipos oficiales y fondos
all: logo wallpapers diagramas

# Compilar logotipos oficiales a PNG
logo:
	$(MAKE) -C logo

# Compilar fondos de pantalla a PNG
wallpapers:
	$(MAKE) -C wallpapers

# Compilar diagramas de arquitectura D2
diagramas:
	$(MAKE) -C diagramas

# Compilar archivo histórico de propuestas
propuestas:
	$(MAKE) -C propuestas_logotipo

# Generar PNGs para los activos del manual
source/assets/%.png: source/assets/%.svg
	$(SVG2PNG) "$<" -O "$@"

# Compilar el Manual de Identidad Visual en HTML con Sphinx
manual-html: $(MANUAL_PNGS)
	$(SPHINXBUILD) -b html source source/_build/html

# Limpieza general
clean:
	rm -rf $(OUTPUT_DIR)
	rm -f source/assets/*.png
	rm -rf source/_build
	$(MAKE) -C logo clean
	$(MAKE) -C wallpapers clean
	$(MAKE) -C diagramas clean
	$(MAKE) -C propuestas_logotipo clean
