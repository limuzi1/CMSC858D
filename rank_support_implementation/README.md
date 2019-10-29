# rank_support class

## Requirements for running the program
1. Python3.7
2. Python packages and modules: bitarray, math, itertools
3. Have the rank_support.py module in your working directory or
try following code before importing the module
```
import sys
sys.path.append('path/to/your/module/')
```

## Attributes and methods
### Attributes :
1. **bv**: bit-vector
2. **n**: size of the bit-vector
3. **s**: the number of superblocks
4. **b**: the number of blocks
5. **rs**: the table containing the rank from the start of each superblock to the start of the bit-vector
6. **rb**: the table containing the rank from the start of each block to the start of its superblock
7. **rp**: all possible in-block queries and corresponding ranks
### Methods:
1. **rank1**: returns the number of 1s in the bit-vector up to position i (1-based, inclusive)
2. **rank0**: returns the number of 0s in the bit-vector up to position i (1-based, inclusive)
3. **overhead**: returns the size of the rank data structure (in bits)

## Example 
```
from rank_support import *
bitvect = '1001011101001010'
rnk = rank_support(bitvect)
rnk.rank1(5)
rnk.rank0(9)
rnk.overhead()
```
