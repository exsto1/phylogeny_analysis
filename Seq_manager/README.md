# Seq manager

## Pfam download
Scripts for automatic sequence download from Pfam database.
Uses set of families' names as an input

### Note
It is recommended to use Pfam **Names**, not Pfam IDs (PF00000) in the input list - Pfam might sometimes not recognize codes correctly.

## Seq worker
Set of scripts for alignment manipulation - adding family prefix, combine multiple files into one and filtering.
There are two filtering scripts
- simple filter checks the length and picks sequences around family average value
- advanced filter filters sequences position-based
