# Separate

If original scripts (in master folder) will not work, try to copy paste scripts from alternative_version folder to master and use them instead. 


## Dependencies
Program tested on Linux Ubuntu 18.04.2. Should be also working on Windows however it's not recommended.

Those scripts need [Python3](https://www.python.org/) and are using those libraries (they should be built-in):
* argparse
* os
* re
* numpy (not necessary - used in flag -P in separate_Pfam_to_counts.py ($ sudo pip3 install numpy))
* matplotlib (not necessary - used in flag -P in separate_Pfam_to_counts.py ($ sudo pip3 install matplotlib))  

To install them quickly you can just type: $ pip3 install -r requirements.txt   


## simple_filter_by_length.py

Filters sequences by their length (number of letters). It helps to filter longer or shorter seq than average but will
not filter if seq is missing some part but is longer in other while length stays similar to others. 

Flag | Description                                       | Default
---- | ------------------------------------------------- | ----
-F   | Directory to the file                             | 
-R   | Recursive search - Directory to folder with files | 
-A   | More or less value than average                   |

Example usage:  
`python3 simple_filter_by_length.py -F files_from_separate_groups_to_counts/put-here-file-name -A 15`  
or for recursive search:  
`python3 simple_filter_by_length.py -R files_from_separate_groups_to_counts -A 10`  


## advanced_filter_by_value.py

Example can be found below

Flag | Description                                       | Default
---- | ------------------------------------------------- | ----
-F   | Directory to the file                             | 
-R   | Recursive search - Directory to folder with files | 
-M   | Error margin                                      | 0.4
-A   | Acceptable number of errors                       | 10
-O   | Detailed output                                   | False

Example usage:  
`python3 advanced_filter_by_value.py -F files_from_separate_groups_to_counts/put-here-file-name'`  
for recursive search:  
`python3 advanced_filter_by_value.py -R files_from_separate_groups_to_counts'`  
to change parameters:  
`python3 advanced_filter_by_value.py -R files_from_separate_groups_to_counts -M 0.5 -A 20'` 


## About advanced_filter_by_value.py

Example for:  
margin = 0.4  
error = 1

Sequence    | col 1 | col 2 | col 3 | col 4 | col 5 | Comment
------------|-------|-------|-------|-------|-------|-----------------------------
S1          |   -   |   -   |   -   |   -   |   A   |
S2          |   -   |   -   |   -   |   A   |   A   |
S3          |   -   |   -   |   A   |   A   |   A   |
S4          |   -   |   A   |   A   |   A   |   A   |
S5          |   A   |   A   |   A   |   A   |   A   |
Value       |  0.2  |  0.4  |  0.6  |  0.8  |   1   |
Compare S1  |  OK   |  OK   |   X   |   X   |  OK   | Error: 2 - Sequence deleted
Compare S2  |  OK   |  OK   |   X   |  OK   |  OK   | Error: 1 - Sequence is OK
Compare S3  |  OK   |  OK   |  OK   |  OK   |  OK   | Error: 0 - Sequence is OK
Compare S4  |  OK   |   X   |  OK   |  OK   |  OK   | Error: 1 - Sequence is OK
Compare S5  |   X   |   X   |  OK   |  OK   |  OK   | Error: 2 - Sequence deleted

So too long and too short sequence are deleted. Notice, that even if columns are in different order result will be the same.


## rename_sequences.py

Adds prefix to each sequence name - helpful if you want to later merge more fasta files into one.

Flag | Description                                       | Default
---- | ------------------------------------------------- | ----
-F   | Directory to the file                             | 
-R   | Recursive search - Directory to folder with files | 

Example usage:  
`python3 rename_sequences.py -F directory/filename.txt`  
or  
`python3 rename_sequences.py -R ./directory/to/folder`  


## merge_into_one_file.py

Merge fasta files. Note that all files you want to merge must be in one folder.

Flag | Description                    | Default
---- | -------------------------------| ----
-R   | Directory to folder with files | 
-O   | Name of the output file        | merged

Example usage:  
`python3 merge_into_one_file.py -R ./directory/to/folder -O output_filename`
