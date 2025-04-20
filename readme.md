# latex-beamer-presentation

## Overview
This project is a LaTeX Beamer presentation template designed for creating professional presentations. It is based on a custom color theme and includes automation scripts for building and viewing the presentation.

## Directory Structure
```
latex-beamer-presentation/
├── slides.tex                  # Main content of the Beamer presentation
├── style/
│   └── beamercolorthememit.sty # Custom color theme for the presentation
├── images/                     # Directory for images used in the presentation
│   └── example.png
├── out/                        # Output directory for the final PDF
│   └── slides.pdf
├── compile/                    # Directory for LaTeX intermediate build files
├── Makefile                    # Automation for building the presentation
├── build-daemon.py             # Script to monitor changes and rebuild the presentation
└── README.md                   # Documentation for the project
```

## Dependencies
- LaTeX Beamer class (version 3.0.7 or higher)
- TeX Live (2008 or higher)
- Optional: Automake (for running pdflatex commands)

## Installation
To set up the project, clone the repository from GitHub:

```bash
git clone <repository-url>
cd latex-beamer-presentation
```

## Generating the Presentation
1. Customize the `slides.tex` file to your liking:

```bash
vim slides.tex
```

2. Change to the project directory and run `make` to generate the presentation PDF:

```bash
make
```

3. View the resulting PDF, named `slides.pdf`, in the `out` directory:

```bash
xpdf out/slides.pdf
```

4. You can also use the provided Makefile to view the presentation automatically with different PDF viewers:

```bash
make view-xpdf
make view-okular
make view-acroread
```

## Customizing the Presentation
- Modify the `slides.tex` file to change the content of your slides.
- Update the `style/beamercolorthememit.sty` file to customize the color theme as needed.
- Add any images you want to use in the presentation to the `images/` directory.

## Running the Build Daemon
To automatically rebuild the presentation when changes are detected, you can run the `build-daemon.py` script:

```bash
python build-daemon.py --fork
```

This will run the script in the background and monitor for changes in the project files.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.