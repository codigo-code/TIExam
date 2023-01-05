class Stats():
    def __init__(self, sortList):
        self.sortList = sortList.copy()

    def less(self, number):
        counter = 0
        while counter < len(self.sortList) and number > self.sortList[counter]:
            counter += 1
        return counter

    def higher(self, number):
        counter = 0
        for i in self.sortList:
            if number < i:
                counter += 1
        return counter

    def between(self, start_number, end_number):
        counter = 0
        for i in self.sortList:
            if i >= start_number and i <= end_number:
                counter += 1
            if i > end_number:
                break
        return counter