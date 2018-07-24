import math

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

class Distance:
    def __init__(self, point_1, point_2):
        self.point_1:Point = point_1
        self.point_2:Point = point_2

        self.__distance = 0
        self._calculate_distance()

    @property
    def distance(self):
        return self.__distance

    def __get_square(self, v1, v2):
        return math.pow((v1 - v2), 2)


    def _calculate_distance(self):
        self.__distance = math.sqrt(self.__get_square(self.point_1.x, self.point_2.x) + self.__get_square(self.point_1.y, self.point_2.y))

        # 13-5
        # 7-4