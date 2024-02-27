class Preprocess:
    def __init__(self,filePath):
        self.data=[]
        self.readData(filePath)
        self.scanData()

    def readData(self,filePath):
        self.filePath=filePath
        with open(filePath,"r") as f:
            for line in f.readlines():
                tmpLine=line.strip().split(", ")
                self.data.append(tmpLine[1:])
    
    def scanData(self):
        self.maxLen=0
        itemSet=[]
        for dataLine in self.data:
            if len(dataLine)>self.maxLen:
                self.maxLen=len(dataLine)
            for data in dataLine:
                if not data in itemSet:
                    itemSet.append(data)
        self.itemSet=set(itemSet)

