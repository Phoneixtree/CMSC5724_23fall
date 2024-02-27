class Apriori:
    def __init__(self, attribute):
        self.minSup = 100
        self.data = attribute["data"]
        self.itemSet = self.apriori(self.data, self.minSup)
        self.itemSet = self.trimSet(self.itemSet)

    def generateCandidates(self, itemSets, k):
        candidates = []
        n = len(itemSets)
        for i in range(n):
            for j in range(i + 1, n):
                itemset1 = set(itemSets[i])
                itemset2 = set(itemSets[j])
                candidate = sorted(itemset1.union(itemset2))
                if len(candidate) == k:
                    candidates.append(candidate)
        return candidates

    def prune(self, itemSets, candidates, k):
        prunedCandidates = []
        for candidate in candidates:
            isValid = True
            for i in range(k):
                subset = candidate[:i] + candidate[i + 1:]
                if subset not in itemSets:
                    isValid = False
                    break
            if isValid:
                prunedCandidates.append(candidate)
        return prunedCandidates

    def apriori(self, transactions, minSup):
        itemSets = []
        k = 1
        itemCounts = {}
        for transaction in transactions:
            for item in transaction:
                itemCounts[item] = itemCounts.get(item, 0) + 1
        Itemsets1 = []
        for item, count in itemCounts.items():
            if count >= minSup:
                Itemsets1.append([item])
        itemSets.extend(Itemsets1)

        while True:
            k += 1
            candidates = self.generateCandidates(itemSets, k)
            prunedCandidates = self.prune(itemSets, candidates, k)
            kItemsets = []
            for candidate in prunedCandidates:
                count = 0
                for transaction in transactions:
                    if set(candidate).issubset(set(transaction)):
                        count += 1
                if count >= minSup:
                    kItemsets.append(candidate)
            if len(kItemsets) == 0:
                break
            itemSets.extend(kItemsets)
        return itemSets
    
    def trimSet(self,arr):
        return sorted([list(x) for x in set(tuple(x) for x in arr)],key=len)