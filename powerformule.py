import math

class formula:
    def __init__(self):
        self._level = 1
        self._potential = 1
        self._rebirths = 0
        self._saint_help_lvl = 1
        self._hellish_help_lvl = 1
        self._hell_curse_lvl = 1
    
    def value(self):
        return self._level * math.pow((math.ldexp(self._potential, self._rebirths) * math.factorial(self._saint_help_lvl)), self._hellish_help_lvl / self._hell_curse_lvl)
    
    def parts(self):
        result = {
        "lvl" : self._level,
        "potential" : self._potential,
        "rebirth" : self._rebirths,
        "holy" : self._saint_help_lvl,
        "hellG" : self._hellish_help_lvl,
        "hellC" : self._hell_curse_lvl
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
        if value > 0 and isinstance(value, int):
            self._level = value
            
    @property
    def potential(self):
        return self._potential
    
    @potential.setter
    def potential(self, value):
        if value > 0 and isinstance(value, int):
            self._potential = value
    
    @property
    def rebirths(self):
        return self._rebirths
    
    @rebirths.setter(self, value)
    def rebirths(self, value):
        if value >= 0 and isinstance(value, int):
            self._rebirths = value
            
    @property
    def saint_help_lvl(self):
        return self._saint_help_lvl
    
    @saint_help_lvl.setter(self, value)
    def saint_help_lvl(self, value):
        if value > 0 and isinstance(value, int):
            self._saint_help_lvl = value
            
    @property
    def hellish_help_lvl(self):
        return self._hellish_help_lvl
    
    @hellish_help_lvl.setter(self, value)
    def hellish_help_lvl(self, value):
        if value > 0 and isinstance(value, int):
            self._hellish_help_lvl = value
    
    

form = formula()

print(form.level)
form.show()