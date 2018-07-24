from datetime import datetime
class Dummy:
    def __init__(self):
        self.__test = 2

    def okay(self, a, b):
        return f"amit/{a}/{b}"

    @property
    def test(self):
        return self.__test

    def get_test(self):
        return self.__test

    def get_time(self):
        return str(datetime.now()).replace(' ', '_') + str(self.__test)