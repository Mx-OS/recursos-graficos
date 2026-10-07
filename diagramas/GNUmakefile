src = *.d2

all: mxos-general.pdf mxos-general.png mxos-general.svg mxos-general.txt mxos-reducido.pdf mxos-reducido.png mxos-reducido.svg mxos-reducido.txt


%.pdf: %.d2
	d2 $*.d2 $@

%.png: %.d2
	d2 $*.d2 $@

%.svg: %.d2
	d2 $*.d2 $@

%.txt: %.d2
	d2 $*.d2 $@

.PHONY: all clean fmt validate
clean:
	rm -f *.pdf
	rm -f *.png
	rm -f *.svg
	rm -f *.txt

fmt: $(src)
	d2 fmt $^

validate: $(src)
	d2 validate $^

