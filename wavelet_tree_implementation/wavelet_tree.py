import sys
import math
from rank_support import *
from select_support import *

method = sys.argv[1]
file1 = sys.argv[2]
file2 = sys.argv[3]
 
def build(file1, file2):
    f1 = open(file1, 'r')
    f2 = open(file2, 'w')
    
    root = ''.join(map(str.strip, f1.readlines()))
    hist = {}
    count = 0
    for c in root:
        count += 1
        if c not in hist:
            hist[c] = 1
        else: 
            hist[c] += 1
    stdout1 = ''
    for k, v in hist.items():
        stdout1 += k + ':' + str(v) + ' '
    sys.stdout.write('The number of distinct characters in the input stirng: ' + stdout1 + '\n')
    sys.stdout.write('The number of characters in the input stirng: ' + str(count) + '\n')
    

    unique = len(set(root))
    queue = [root]
    flag = set()
    for s in queue:
        chars = sorted(set(s))
        if len(chars) == 1:
            chars = chars[0]
            flag.add(chars)
            if len(flag) == unique:
                f2.write(chars + '\n')
                break
            else:
                f2.write(chars + '\n')
                queue.append(chars)
                queue.append(chars)
                continue
        mid = chars[math.ceil((0+len(chars))/2)]
        left = ''
        right = ''
        bitVect = ''
        for c in s:
            if c < mid:
                left += c
                bitVect += '0'
            else:
                right += c
                bitVect += '1'
        f2.write(mid + '\t' + bitVect + '\n')
        queue.append(left)
        queue.append(right)
        
    f1.close()
    f2.close()
    
def access(file1, file2):
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    wt = []
    for line in f1:
        values = line.strip().split('\t')
        wt.append(values)
    acc = []
    for line in f2:
        acc.append(int(line.strip()))
        
    for i in acc:
        i = i+1
        n = 0
        node = wt[n]
        bv = rank_support(node[1])
        while len(node)>1:
            if bv.bv[i-1] == 0:
                n = 2*n+1
                i = bv.rank0(i)
            else:
                n = 2*n+2
                i = bv.rank1(i)
            node = wt[n]
            if len(node) == 1:
                sys.stdout.write(node[0] + '\n')
            else:
                bv = rank_support(node[1])

    f1.close()
    f2.close()

def rank(file1, file2):
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    wt = []
    for line in f1:
        values = line.strip().split('\t')
        wt.append(values)
    rnk = []
    for line in f2:
        values = line.strip().split('\t')
        rnk.append((values[0], int(values[1])))
        
    for r in rnk:
        c = r[0]
        i = r[1]
        n = 0
        node = wt[n]
        mid = node[0]
        bv = rank_support(node[1])
        while len(node)>1:
            if c < mid:
                n = 2*n+1
                i = bv.rank0(i)
                if i == 0:
                    sys.stdout.write('0' + '\n')
                    break
            else:
                n = 2*n+2
                i = bv.rank1(i)
                if i == 0:
                    sys.stdout.write('0' + '\n')
                    break
            node = wt[n]
            if len(node) == 1:
                sys.stdout.write(str(i) + '\n')
            else:
                mid = node[0]
                bv = bv = rank_support(node[1])
                           
    f1.close()
    f2.close()
       
def select(file1, file2):
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    wt = []
    for line in f1:
        values = line.strip().split('\t')
        wt.append(values)
    slt = []
    for line in f2:
        values = line.strip().split('\t')
        slt.append((values[0], int(values[1])))
    
    for s in slt:
        c = s[0]
        i = s[1]
        try:
            n = wt.index([c])
        except:
            sys.stdout.write('0' + '\n')
            continue
        if (n-1)%2 == 0:
            n = int((n-1)/2)
        else:
            n = int((n-2)/2)
        node = wt[n]
        mid = node[0]
        bv = select_support(node[1])
        while n>0:
            if c < mid:
                i = bv.select0(i)
            else:
                i= bv.select1(i)
            if (n-1)%2 == 0:
                n = int((n-1)/2)
            else:
                n = int((n-2)/2)
            node = wt[n]
            mid = node[0]
            bv = select_support(node[1])
        if c < mid:
            i = bv.select0(i)
        else:
            i= bv.select1(i)
        sys.stdout.write(str(i) + '\n')
    
    f1.close()
    f2.close()
            

if method == 'build':
    build(file1, file2)
elif method == 'access':
    access(file1, file2)
elif method == 'rank':
    rank(file1, file2)
elif method == 'select':
    select(file1, file2)
