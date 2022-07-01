class estructList:
    def __init__(self):
        self.listTest01 = list()
        self.listTest02 = list()

    def addNumbersList01(self, newData):
        self.listTest01.append(int(newData))

    def addNumbersList02(self, newData):
        self.listTest02.append(int(newData))

    def removeNumsList01(self, newData):
        if newData is self.listTest01:
            self.listTest01.remove(newData)
        else:
            return "Element not exist in list01"

    def removeNumsList02(self, newData):
        if newData is self.listTest02:
            self.listTest02.remove(newData)
        else:
            return "Element not exist in list02"

    def mergeTwoLists(self):
        return self.listTest01 + self.listTest02

    def findMinValue(self):
        print(f"\nMinimun Value of List01: {min(self.listTest01)}")
        print(f"\nMinimun Value of List02: {min(self.listTest02)}")

    def maxSumSublist(self):
        print(f"\nSummation: {sum(self.listTest01)} + {sum(self.listTest02)}")

    def productAllElements(self):
        prod = 1

        for i in self.listTest01:
            prod *= self.listTest01[i]
        print(f"Elements List01(Product): {prod}")

        prod = 1  # return 'prod' to state 1

        for j in self.listTest02:
            prod *= self.listTest01[j]
        print(f"Elements List01(Product): {prod}")


studyList = estructList()

# Creating list01:

# Creating list02:

# Removing 1 element to list01:

# Removing 1 element to list02:

# Merge the 2 lists:

# Find Minimun Value of lists:

# Maximun Sum Sublists:

# Product all elements of lists:
