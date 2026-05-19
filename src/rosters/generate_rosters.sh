#!/bin/bash

FACTION_ROSTERS="../../faction_rosters"

if [ ! -d $FACTION_ROSTERS ]; then
    mkdir $FACTION_ROSTERS
fi

cd empire
python galactic_empire.py
pdflatex galactic_empire.tex
mv galactic_empire.pdf ../$FACTION_ROSTERS
cd ..

cd mandalore
python mandalore.py
pdflatex mandalore.tex
mv mandalore.pdf ../$FACTION_ROSTERS
cd ..

cd rebel
python rebel_alliance.py
pdflatex rebel_alliance.tex
mv rebel_alliance.pdf ../$FACTION_ROSTERS
cd ..

cd republic
python galactic_republic.py
pdflatex galactic_republic.tex
mv galactic_republic.pdf ../$FACTION_ROSTERS
cd ..

cd separatist
python separatist_alliance.py
pdflatex separatist_alliance.tex
mv separatist_alliance.pdf ../$FACTION_ROSTERS
cd ..

cd syndicates
python crime_syndicates.py
pdflatex crime_syndicates.tex
mv crime_syndicates.pdf ../$FACTION_ROSTERS
cd ..
