# Summary
OSFST is a finite-state transducer for the Old Saxon language, built on the framework of Helsinki Finite-State Technologies (HFST) using Köbler's Old Saxon Dictionary. Current output forms are in forms.txt, while information about corpus coverage is in coverage.txt. 
This project was originally titled Muspilli. That legacy project is still on Github but is not being updated.

# Installation
1. Download and install the binaries for HFST.
2. Clone or download this github repository.

# Use
The makefile contains requisite command-line syntax to compile.
One compiled, use `hfst-lookup os.gen.hfst "string"` to search for specific strings.
