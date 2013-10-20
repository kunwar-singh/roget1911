This directory contains data files and python scripts used to generate
the output files "roget.xml" and "syblists.txt".

Output Files:
roget.xml -- clean, canonical XML version of Roget's Thesaurs (1911 Edition).
synlists.txt -- collection of synonym lists generated from roget.xml

Data files:
roget11raw.txt, roget11.txt, wordcnts.txt, mobythesaurus.txt

Python scripts:
makexml.py -- generate roget.xml
makesyns.py -- generate synlists.txt
thesaurus.py -- interactive thesaurus, based on synlists.txt

