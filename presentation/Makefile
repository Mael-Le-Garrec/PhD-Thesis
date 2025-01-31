SHELL=/bin/bash

PREZ="phd_presentation.pdf"
CURRENT_DIR=$$(basename $$(pwd))

all: cclean prez

prez:
	pandoc --number-sections \
		--slide-level=3 \
				-t beamer \
				--template template.tex \
				slides.md \
				-o slides.tex \
				--lua-filter=filter.lua
	TEXINPUTS=".:./resources//:" lualatex slides.tex
	bibtex slides
	TEXINPUTS=".:./resources//:" lualatex slides.tex
	mv slides.pdf ${PREZ}

clean:
	rm -f slides.{aux,log,nav,out,snm,toc,vrb,bcf,run.xml,bbl,blg}

cclean: clean
	rm -f slides.{tex,pdf}
	rm -f ${PREZ}
	rm -f *.pdf


.PHONY: prez, clean, cclean, all
