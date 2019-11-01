from bitarray import bitarray
import math
from itertools import product

class rank_support:
    def __init__(self, bv):
        self.bv = bitarray(bv)
        
        n = self.bv.length()
        s = math.log(n,2)**2/2
        b = math.ceil(math.log(n,2)/2)
        if s%b == 0:
            s = int(s)
        else:
            s = (math.floor(s/b)+1)*b
        self.n = n
        self.s = s
        self.b = b
        
        rb = []
        for j in range(0, n, s):
            if j == 0:
                rs = [0]
            else:
                rs.append(rs[-1]+sum(self.bv[j-s:j])) 
            if j+s <= n:
                for k in range(j, j+s, b):
                    if k == j:
                        rb_sub = [0]
                    else:
                        rb_sub.append(rb_sub[-1]+sum(self.bv[k-b:k]))
            else:
                for k in range(j, n, b):
                    if k == j:
                        rb_sub = [0]
                    else:
                        rb_sub.append(rb_sub[-1]+sum(self.bv[k-b:k]))
            rb.append(rb_sub)
        self.rs = rs
        self.rb = rb
        
        prod = list(product([0,1], repeat=b))
        rp = {}
        for key in prod:
            value = []
            for p in range(0, len(key)):
                value.append(sum(key[0:p+1]))
            rp[key] = value
        self.rp = rp
        
    def rank1(self, i):
        j = math.floor((i-1)/self.s)
        ns = self.rs[j]
        
        k = math.floor((i-1-j*self.s)/self.b)
        nb = self.rb[j][k]
        
        if i%self.b == 0:
            start = i-self.b
        else:
            start = i-i%self.b
        if start+self.b > self.n:
            key = self.bv[start:self.n]
            key.extend([0]*(self.b-key.length()))
            key = tuple(map(int, list(key)))
        else:
            key = tuple(map(int, list(self.bv[start:start+self.b])))
        np = self.rp[key][i%self.b-1]
        
        rank1 = ns+nb+np
        return rank1
    
    def rank0(self, i):
        return i-self.rank1(i)
    
    def overhead(self):
        Srs = 0
        for srs in self.rs:
            Srs += len(bin(srs)[2:])
            
        Srb = 0
        for sublist in self.rb:
            for srb in sublist:
                Srb += len(bin(srb)[2:])
                
        Srp = 0
        for key, value in self.rp.items():
            for k in key:
                Srp += len(bin(k)[2:])
            for v in value:
                Srp += len(bin(v)[2:])
                
        return self.n+Srs+Srb+Srp
    
        
    