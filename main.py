#Class that represents a case with the number of strings and a list of the strings
class Case:
    def __init__(self,number,stringList):
        #Variable that represents the number of strings 
        self.number = number
        
        #The list of strings
        self.stringList = stringList

#Function that parses the input file and returns a list of cases
def parseInput(filename):
    inputFile = open(filename,'r')
    lines = inputFile.readlines() #"lines" contains every lines in the file
    for i in range(1,lines.length):
        
    
#The list of cases    
cases = parseInput(sys.argv[1])


    