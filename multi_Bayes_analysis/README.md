# multi Bayes analysis

## "batching"

"Batching" folder contains scripts to prepare for MrBayes server batch running.
Creates working directory and the batch file itself.
Script is randomizing the seed and setting it up manually, as batched version always runs on set seed - this way we avoid running 150 identical trees.


## "single" and "multi"
Set of scripts to analyse trees, calculate statistics and present them on the plots.

Plot scripts use .mcmc files as an input data (standard mrBayes output)
Colouring scripts use .contree files (saved tree state in extended .json format)
