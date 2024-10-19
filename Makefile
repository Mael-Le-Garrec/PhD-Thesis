SHELL=/bin/bash

all:
	latexmk -lualatex main.tex

clean:
	rm -f *.fls
	rm -f main.aux
	rm -f main.bbl
	rm -f main.beam-glg
	rm -f main.beam-glo
	rm -f main.beam-gls
	rm -f main-blx.bib
	rm -f main.equipment-glg
	rm -f main.equipment-glo
	rm -f main.equipment-gls
	rm -f main.fdb_latexmk
	rm -f main.fls
	rm -f main.log
	rm -f main.maf
	rm -f main.mtc
	rm -f main.mtc*
	rm -f main.nomenclature-glg
	rm -f main.nomenclature-glo
	rm -f main.nomenclature-gls
	rm -f main.symbols-glg
	rm -f main.symbols-glo
	rm -f main.symbols-gls
	rm -f main.tmb
	rm -f main.wrt
	rm -f main.acn
	rm -f main.blg
	rm -f main.glo
	rm -f main.acr
	rm -f main.alg
	rm -f main.glg
	rm -f main.gls
	rm -f main.lof
	rm -f main.lot
	rm -f main.toc
	rm -f main.ist
	rm -f main.out
	rm -f main.run.xml
	rm -f main.synctex.gz

.PHONY: all clean
