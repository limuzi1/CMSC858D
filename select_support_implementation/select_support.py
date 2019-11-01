from rank_support import *
import math  

class select_support:
    def __init__(self, bv):
        self.rk = rank_support(bv)
        
    def select1(self, i):
        start = 0
        end = self.rk.n - 1
        while start < end:
            mid = math.floor((start+end)/2)
            if self.rk.rank1(mid+1) < i:
                start = mid+1
            else:
                end = mid
        return start+1
    
    def select0(self, i):
        start = 0
        end = self.rk.n - 1
        while start < end:
            mid = math.floor((start+end)/2)
            if mid+1-self.rk.rank1(mid+1) < i:
                start = mid+1
            else:
                end = mid
        return start+1
    
    def overhead(self):
        Srs = 0
        for srs in self.rk.rs:
            Srs += len(bin(srs)[2:])
            
        Srb = 0
        for sublist in self.rk.rb:
            for srb in sublist:
                Srb += len(bin(srb)[2:])
                
        Srp = 0
        for key, value in self.rk.rp.items():
            for k in key:
                Srp += len(bin(k)[2:])
            for v in value:
                Srp += len(bin(v)[2:])
                
        return self.rk.n+Srs+Srb+Srp
