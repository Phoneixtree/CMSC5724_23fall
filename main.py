from Preprocess import Preprocess
from Apriori import Apriori
from Rule import Rule

if __name__ == "__main__":
    #inputFile="test.csv"
    inputFile="asso.csv"
    p=Preprocess(inputFile)
    #print(vars(p))
    a=Apriori(vars(p))
    #for item in a.itemSet:
    #    print(item)
    r=Rule(a.itemSet,a.data)
    for rule in r.rules:
        print(f"{rule[0]} -> {rule[1]} (confidence: {rule[2]})")