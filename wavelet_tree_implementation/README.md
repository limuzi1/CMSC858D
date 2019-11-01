# wavelet_tree.py program

## Requirements for running the program
1. Python3.7
2. Python packages and modules: bitarray, math, itertools, sys, rank_support, select_support
3. Have the rank_support.py and select_support modules in your working directory or
add following code in the wavelet_tree.py program before importing the module
```
import sys
sys.path.append('path/to/your/module/')
```

## Functions
1. **build**  
The program can read the string from a input file, 
build a binary balanced tree based on the string, 
and write the wavelet tree into an output file.
The program will also print out the number of characters and 
the number of distinct characters in the string.
2. **access** 
The program can load the wavelet tree from the output file 
and access the character at ith position (0-based).
Access queries need to be stored in a file as a newline-separated list of indices.
3. **rank**  
The program can load the wavelet tree from the output file,
and find the number of a character in the string up to position i (1-based inclusive).
Rank queries need to be written in a file as a newline-separated list of <c>\t<i>.
c is the character, and i is the position.
4. **select**  
The program can load the wavelet tree from the output file,
and find the position (1-based) of a character when it occurs i times.
Select queries need to be stored in a file as a newline-separated list of <c>\t<i>.
c is the character, and i is the occurence of the character. 

## Example 
```
python build input_string.txt output_tree.txt
python access output_tree.txt access_queries.txt
python rank output_tree.txt rank_queries.txt
python select output_tree.txt select_queries.txt
```