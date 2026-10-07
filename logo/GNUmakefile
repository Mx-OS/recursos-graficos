# Makefile para exportación de logotipos oficiales de Fundación MxOS

OUTPUT_DIR = output
SVG2PNG = python3 ../svg2png.py

SVGS = $(wildcard *.svg)
PNGS = $(patsubst %.svg,$(OUTPUT_DIR)/%.png,$(SVGS))

.PHONY: all clean

all: $(PNGS)

$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

$(OUTPUT_DIR)/%.png: %.svg | $(OUTPUT_DIR)
	$(SVG2PNG) "$<" -O "$@"

clean:
	rm -rf $(OUTPUT_DIR)
