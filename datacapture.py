from stats import Stats


class DataCapture():
    def __init__(self):
            self._inputs_added = []  # Inputs
            self._min_value = None  # Minimum value added
            self._max_value = None  # Maximum value added

    def add(self, input: int):

        self._set_min(input)
        self._set_max(input)
        self._inputs_added.append(input)
        # Original idea was to use a dictionary since the beginning
        # if self._inputs.get(input) == None:
        #     self._inputs[input] = 0
        # self._inputs[input] += 1

    def _set_min(self, input: int):

        if self._min_value is None:
            self._min_value = input

        if input < self._min_value:
            self._min_value = input

    def _set_max(self, input: int):

        if self._max_value is None:
            self._max_value = input

        if input > self._max_value:
            self._max_value = input

    def build_stats(self) -> Stats:
        inputs = sorted(self._inputs_added)
        inputs_index = {}

        # O(n)
        for index, input in enumerate(inputs):

            temp_list = []

            if input not in inputs_index:
                inputs_index[input] = []

            temp_list = inputs_index[input]
            temp_list.append(index)

            inputs_index[input] = temp_list

        return Stats(inputs_index, self._max_value)