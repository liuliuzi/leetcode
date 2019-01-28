class TwoSum (object):
    def __init__(self):
        self.numDict={}
    def add(self, i):
        if self.numDict.has_key(i):
            self.numDict[i]+=1
        else:
            self.numDict[i]=1
    
    def find(self, i):
        for k in self.numDict:
            rest = i-k
            if rest==k and self.numDict[k]>1:
                return True
            elif self.numDict.has_key(rest):
                return True
        return False





sol=TwoSum()
sol.add(2)
sol.add(3)
sol.add(5)
sol.add(5)

print sol.find(8)
print sol.find(10)
print sol.find(12)