class Employee:
    def __init__(self, fname=None, lname=None):
        self._fname = fname
        self.__lname = lname
        self._set_firstname("Amit")

    def _set_firstname(self, fname):
        self._fname = fname

    def __set_lastname(self, lname):
        self.__lname = lname

    def _get_fname(self):
        return self._fname

    def get_test(self, ok):
        return f"qa_{ok}"

    def get_fullname(self):
        # self.okay()
        return f"{self._get_fname()} {self.__lname}"

    def okay(self):
        raise Exception("Hello world")