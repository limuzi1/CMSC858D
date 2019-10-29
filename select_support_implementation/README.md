# select_support class

## Requirements for running the program
1. Python3.7
2. Python packages and modules: bitarray, math, itertools, rank_support
3. Have the rank_support.py and select_support modules in your working directory or
try following code before importing the module
```
import sys
sys.path.append('path/to/your/module/')
```

## Attributes and methods
### Attributes :
1. **rk**: an instance of rank_support class
### Methods:
1. **select1**: returns the position (1-based) of ith 1s in the bit-vector
2. **select0**: returns the position (1-based) of ith 0s in the bit-vector
3. **overhead**: returns the size of the select data structure (in bits)

## Example 
```
from select_support import *
bitvect = '1001011101001010'
slt = select_support(bitvect)
slt.select1(5)
slt.select0(5)
slt.overhead()
```
