import stats

class DataCapture():
    def __init__(self):
        self.number_list = []

    def add(self, number):
        self.number_list.append(number)

    def build_stats(self):
        self.number_list.sort()
        return stats.Stats(self.number_list)