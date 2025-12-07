import math
from numtransform import transformer


class formula:
    def __init__(self):
        self._level = 1
        self._potential = 1
        self._rebirths = 0
        self._saint_help_lvl = 1
        self._hellish_help_lvl = 1
        self._hell_curse_lvl = 1
        self._transr = transformer()
        self._power = 0

    @property
    def value(self):
        return self._power

    def calc(self):
        self._power = (self._level * self._potential * (2 ** self._rebirths) * math.factorial(self._saint_help_lvl)) ** (self._hellish_help_lvl / self._hell_curse_lvl)

    @property
    def correct_value(self):
        self._transr.check(self._power)
        return round(self.value / self._transr.less, 2)

    @property
    def transformer(self):
        return self._transr

    def parts(self):
        result = {
            "lvl": self._level,
            "potential": self._potential,
            "rebirth": self._rebirths,
            "holy": self._saint_help_lvl,
            "hellG": self._hellish_help_lvl,
            "hellC": self._hell_curse_lvl
        }
        return result

    def show(self):
        nums = self.parts()
        print(f"Level : {nums['lvl']}\nPotential : {nums['potential']}\nRebirths : {nums['rebirth']}\nSaint gift level : {nums['holy']}\nSatan gift level : {nums['hellG']}\nSatan curse level : {nums['hellC']}")

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if can_int(value):
            if not isinstance(value, int):
                value = int(value)
            if value == -1:
                self._level = 1
            elif value > 0 and isinstance(value, int):
                self._level = value

    @property
    def potential(self):
        return self._potential

    @potential.setter
    def potential(self, value):
        if can_int(value):
            if not isinstance(value, int):
                value = int(value)
            if value == -1:
                self._potential = 1
            elif value > 0 and isinstance(value, int):
                self._potential = value

    @property
    def rebirths(self):
        return self._rebirths

    @rebirths.setter
    def rebirths(self, value):
        if can_int(value):
            if not isinstance(value, int):
                value = int(value)
            if value == -1:
                self._rebirths = 0
            elif value >= 0 and isinstance(value, int):
                self._rebirths = value

    @property
    def saint_help_lvl(self):
        return self._saint_help_lvl

    @saint_help_lvl.setter
    def saint_help_lvl(self, value):
        if can_int(value):
            if not isinstance(value, int):
                value = int(value)
            if value == -1:
                self._saint_help_lvl = 1
            elif value > 0 and isinstance(value, int):
                self._saint_help_lvl = value

    @property
    def hellish_help_lvl(self):
        return self._hellish_help_lvl

    @hellish_help_lvl.setter
    def hellish_help_lvl(self, value):
        if can_int(value):
            if not isinstance(value, int):
                value = int(value)
            if value == -1:
                self._hellish_help_lvl = 1
            elif value > 0 and isinstance(value, int):
                self._hellish_help_lvl = value

    @property
    def hellish_curse_lvl(self):
        return self._hell_curse_lvl

    @hellish_curse_lvl.setter
    def hellish_curse_lvl(self, value):
        if can_int(value):
            if not isinstance(value, int):
                value = int(value)
            if value == -1:
                self._hell_curse_lvl = 1
            elif value > 0 and isinstance(value, int):
                self._hell_curse_lvl = value


def get_val(text):
    res = input(text + ": ")
    if can_int(res):
        return int(res)
    else:
        return -1


def can_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    formule = formula()
    formule.level = get_val("level")
    formule.potential = get_val("potential")
    formule.rebirths = get_val("rebirths")
    formule.saint_help_lvl = get_val("saint help lvl")
    formule.hellish_help_lvl = get_val("hellish help lvl")
    formule.hellish_curse_lvl = get_val("hellish curse lvl")

    print()

    print(f"Power is {formule.value}\n")
    formule.show()
