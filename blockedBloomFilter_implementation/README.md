# blockedBloomFilter class

## Requirements for running the program
1. Python3.7
2. Python packages and modules: sys, argparse, math, mmh3

## Command and command-line parameters
### build 
The command reads in the keys in the key file, 
builds the blocked Bloom filter data structure, 
and writes the structure into a file.
1. **-k**: the file containing input keys
2. **-f**: the desired target false positive rate
3. **-n**: the number of distinct keys in the key file
4. **-o**: the output file containing constructed blocked Bloom filter
### query
The command reads in the queries in the query file,
checkes the presence of the query in the constructed structure,
and outputs the results to standard out.
1. **-i**: the input file for query created by the build command
2. **-q**: the file containing queries

## Example 
```
python blockedBloomFilter.py build -k keyFile.txt -f FPR -n numOfUniqueKey -o structureFile.txt
python blockedBloomFilter.py query -i structureFile.txt -q queryFile.txt
python blockedBloomFilter.py -h
```
