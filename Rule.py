import itertools
class Rule:
    def __init__(self,itemSet,data):
        self.miniConfidence=0.9
        self.frequentSets=self.trimSet(itemSet)
        self.transanctions=data
        self.rules=[]
        self.generateRules()

    def generateRules(self):
        for frequentSet in self.frequentSets:
            subSets=self.generateSubsets(frequentSet)
            for subSet in subSets:
                remainSet= set(frequentSet)-set(subSet)
                if len(remainSet)>0:
                    result=self.calculateConfidence(frequentSet,subSet)
                    if result[2]>=self.miniConfidence:
                        self.rules.append((subSet,result[0],remainSet,result[1],round(result[2],5)))

    def generateSubsets(self,frequentSet):
        subsets = []
        for i in range(1, len(frequentSet)+1):
            subsets.extend(itertools.combinations(frequentSet, i))
        return subsets

    def calculateConfidence(self,numeratorSet,denominatorSet):
        numerator=0
        denominator=0
        for transaction in self.transanctions:
            if set(numeratorSet).issubset(set(transaction)):
                numerator+=1
            if set(denominatorSet).issubset(set(transaction)):
                denominator+=1
        quotient=numerator/denominator
        return numerator,denominator,quotient

    def trimSet(self,itemSet):
        return [s for s in itemSet if len(s)>1]
