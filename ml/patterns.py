# -*- coding: utf-8 -*-
"""
Created on Wed May 23 00:19:27 2012

Pattern recognition algorithms

@author: gopi
"""

items=['i1','i2','i3','i4','i5']
transactions=[]

transactions.append([1,1,0,0,0])
transactions.append([0,1,0,1,0])
transactions.append([0,1,1,0,0])
transactions.append([1,1,0,1,0])
transactions.append([1,0,1,0,0])
transactions.append([1,0,1,0,0])
transactions.append([1,1,1,0,1])
transactions.append([1,1,1,0,0])

class apriori(object):

    def __init__(self):
        self.dataset = None
        self.minSupport = None

    def scanForCount(self,elements):
        count =0
        match=True
        if len(elements) == len(self.dataset[0]):
            for j in range(len(self.dataset)):
                for i in range(len(elements)):
                    if elements[i] != self.dataset[j][i]:
                        match=False
                if match:
                    count+=1
        return count
            
            


def main():
    apobj = apriori()
    apobj.dataset = transactions
    print apobj.scanForCount([1,0,0,0,0])
    
    
if __name__ == "__main__":
    main()
            
