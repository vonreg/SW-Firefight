#!/bin/bash

cd empire
python galactic_empire.py
pdflatex galactic_empire.tex
cd ..

cd mandalore
python mandalore.py
pdflatex mandalore.tex
cd ..

cd rebel
python rebel_alliance.py
pdflatex rebel_alliance.tex
cd ..

cd republic
python galactic_republic.py
pdflatex galactic_republic.tex
cd ..

cd seperatist
python seperatist_alliance.py
pdflatex seperatist_alliance.tex
cd ..

cd syndicates
python crime_syndicates.py
pdflatex crime_syndicates.tex
cd ..
