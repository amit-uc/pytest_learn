
class NumberSum:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def get_sum(self):
        return self.__a + self.__b

def okay(a, b):
    return NumberSum(a,b)

def sumd(a, b):
    return okay(a, b)