# Makefile para exportación de folletos oficiales de la Fundación MxOS

SHELL := /bin/sh
.SHELLFLAGS := -ec
.DEFAULT_GOAL := all

OUTPUT_DIR ?= output
SVG2PNG ?= python3 ../svg2png.py

SVGS := $(wildcard *.svg)
PNGS := $(patsubst %.svg,$(OUTPUT_DIR)/%.png,$(SVGS))

.PHONY: all clean help

all: $(PNGS)

$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

$(PNGS): $(OUTPUT_DIR)/%.png: %.svg | $(OUTPUT_DIR)
	$(SVG2PNG) "$<" -O "$@"

clean:
	rm -rf $(OUTPUT_DIR)

help:
	@printf "Objetivos disponibles en brochures/:\n"
	@printf "  make all    - Rasteriza todos los folletos SVG a PNG en %s/\n" "$(OUTPUT_DIR)"
	@printf "  make clean  - Elimina los archivos generados en %s/\n" "$(OUTPUT_DIR)"
