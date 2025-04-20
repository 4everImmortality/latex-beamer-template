out/slides.pdf: slides.tex style/beamercolorthememit.sty
    mkdir -p out compile
    pdflatex -output-directory=compile slides.tex
    pdflatex -output-directory=compile slides.tex
    if [ -f compile/slides.pdf ]; then cp compile/slides.pdf out/slides.pdf; else echo "PDF not generated!"; exit 1; fi

view-xpdf: out/slides.pdf
    xpdf out/slides.pdf &

view-okular: out/slides.pdf
    okular out/slides.pdf &

view-acroread: out/slides.pdf
    acroread out/slides.pdf &

clean:
    rm -rf out compile