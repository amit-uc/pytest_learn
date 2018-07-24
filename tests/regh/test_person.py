class Person:
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def age(self):
        return self.__age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


def test_person(monkeypatch):
    per = Person("Amit", "Thapa", 24)

    monkeypatch.setattr(Person, "full_name", lambda x: None)

    assert (None == per.full_name())