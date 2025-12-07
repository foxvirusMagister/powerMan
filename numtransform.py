class transformer:
    def __init__(self):
        self._num = 0
        self._pre = 0
        self._less = 1
        self._prelist = ["", "K", "M", "B", "T", "Qd", "Qn", "Sx", "Sp", "Oc"]

    def check(self, number):
        self._pre = 0
        self._less = 1
        while number >= 1000 and self._pre < len(self._prelist) - 1:
            number /= 1000
            self._less *= 1000
            self._pre += 1
        self._num = number

    @property
    def num(self):
        return self._num

    @property
    def less(self):
        return self._less

    @property
    def pre(self):
        return self._prelist[self._pre]
