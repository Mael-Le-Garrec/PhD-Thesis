all: pdf

pdf:
	lualatex main.tex
	makeglossaries main
	lualatex main.tex
	lualatex main.tex

lean:
	rm -f *{aux,log,ist,idx,gls,glo,glg,toc,fdb_latexmk}
