import sys
from itertools import izip

#Class that represents a case with the number of strings and a list of the strings
class Case:
    def __init__(self,number,stringList):
        #Variable that represents the number of strings 
        self.number = number
        
        #The list of strings
        self.stringList = stringList

    def split(self, string):
        l = []
        cur = string[0]
        count = 0
        for c in string:
            if cur == c:
                count += 1
            else:
                t = (cur,count)
                l.append(t)
                count = 1
                cur = c
        l.append((cur,count))
        return l

    def countMove(self, splitted):
        #print("count")
        listTuple = izip(*splitted)
        cpt = 0
        for t in listTuple:
            chars = [i[0] for i in t]
            counts = [i[1] for i in t]
            chars.sort()

            if chars[0] != chars[-1]:
                return None

            s = sum(counts)
            m = min(counts)
            mean = s / len(counts)
            
            
            mod = sum([abs(i-mean) for i in counts])
            print(counts, s, mean,m, mod)
            cpt += mod
        return cpt

    def solve(self):
        splitted = []
        for s in self.stringList:
            splitted.append(self.split(s))

        return self.countMove(splitted)

        

#Function that parses the input file and returns a list of cases
def parseInput(filename):
    with open(filename,'r') as inputFile:
        lines = int(inputFile.readline()) #"lines" contains every lines in the file
        for i in range(lines):
            n = int(inputFile.readline())
            l= [inputFile.readline().strip() for j in range(n)]
            yield Case(n,l)
    
#The list of cases

filename = "sample.txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]
cases = parseInput(filename)


res = [c.solve() for c in cases]

with open(filename +".res",'w') as f:
    cpt = 1
    for i in res:
        f.write("Case #")
        f.write(str(cpt))
        cpt += 1
        f.write(": ")
        if i == None:
            f.write("Fegla Won")
        else:
            f.write(str(i))
        f.write("\n")

