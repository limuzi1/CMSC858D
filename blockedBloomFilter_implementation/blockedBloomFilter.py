import sys
import argparse
import math
import mmh3

parser = argparse.ArgumentParser(description="Blocked Bloom Filter")

parser.add_argument("command", help="build/query blocked Bloom filter data structure")
parser.add_argument("-k", dest="keyFile", help="the file containing input keys")
parser.add_argument("-f", dest="FPR", type=float, help="the desired target false positive rate")
parser.add_argument("-n", dest="n", type=int, help="the number of distinct keys in the key file")
parser.add_argument("-o", dest="outputFile", help="the output file containing constructed blocked Bloom filter")
parser.add_argument("-i", dest = "inputFile", help = "the input file for query created by the build command")
parser.add_argument("-q", dest = "queryFile", help = "the file containing queries")

args = parser.parse_args()
command = args.command
keyFile = args.keyFile
FPR = args.FPR
n = args.n
outputFile = args.outputFile
inputFile = args.inputFile
queryFile = args.queryFile

class blockedBloomFilter:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        m = int(n * math.log(p) / (math.log(2)**2) * -1)
        self.m = m
        k = int(m / n * math.log(2))
        self.k = k
        b = math.ceil(m / 512)
        self.b = b
        bv = [['0']*512 for _ in range(b)]
        self.bv = bv
        
    def insert(self, key):
        i = mmh3.hash(key, 0) % self.b
        for j in range(1, self.k):
            pos = mmh3.hash(key, j) % 512
            self.bv[i][pos] = '1'
            
    def query(self, qry):
        i = mmh3.hash(qry, 0) % self.b
        for j in range(1, self.k):
            pos = mmh3.hash(qry, j) % 512
            if self.bv[i][pos] == '0':
                return 'N'
        return 'Y'
    
def build(keyFile, FPR, n, outputFile):
    outputFile = open(outputFile, 'w')
    bf = blockedBloomFilter(n, FPR)
    outputFile.write(str(bf.n) + ',' + str(bf.p) + '\n')
    
    keyFile = open(keyFile, 'r')
    for line in keyFile:
        key = line.strip()
        bf.insert(key)
    for lst in bf.bv:
        outputFile.write(''.join(lst) + '\n')
        
    keyFile.close()
    outputFile.close()
        
def query(inputFile, queryFile):
    inputFile = open(inputFile, 'r')
    np = inputFile.readline().strip().split(',')
    bf = blockedBloomFilter(int(np[0]), float(np[1]))
    
    bf.bv = []
    for line in inputFile:
        bf.bv.append(list(line.strip()))
    
    queryFile = open(queryFile, 'r')
    for line in queryFile:
        qry = line.strip()
        sys.stdout.write(qry + ':'+ bf.query(qry) + '\n')
        
if command == 'build':
    build(keyFile, FPR, n, outputFile)
elif command == 'query':
    query(inputFile, queryFile)