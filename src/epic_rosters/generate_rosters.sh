#!/bin/bash

FACTION_ROSTERS="../../epic_faction_rosters"

if [ ! -d $FACTION_ROSTERS ]; then
    mkdir $FACTION_ROSTERS
fi

cd republic
python galactic_republic.py 2>&1 | tee log.py_gar
pdflatex galactic_republic.tex
mv galactic_republic.pdf ../$FACTION_ROSTERS
cd ..

cd separatist
python separatist_alliance.py 2>&1 | tee log.py_cis
pdflatex separatist_alliance.tex
mv separatist_alliance.pdf ../$FACTION_ROSTERS
cd ..