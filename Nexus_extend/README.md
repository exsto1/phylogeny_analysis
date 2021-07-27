# Nexus extend

## pdb mapping
Script for automatic mapping between set of Pfam families (provided as an .fasta file) and pdbmap database file.
As an output user can read list of PDB IDs connected with provided families.

## matrix builder
Set of scripts to parse data from additional files (structural info, publication mining) and extend provided nexus file as a feature matrix.
Nexus file is the standard input file for the MrBayes program.
Script is both extending sequences and modyfing all the necessary info (like new seq length) so MrBayes is able to read it properly.
