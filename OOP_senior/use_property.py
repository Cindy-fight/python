class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0~100')
        self._score = score

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, birth):
        self._birth = birth

    @property
    def age(self):
        return 2017 - self._birth

s = Student()
s.score = 88
print(s.score)

s.birth = 1993
print(s.birth)

print(s.age)


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height

screen = Screen()
screen.width = 1024
screen.height = 768
print(screen.width)
print(screen.height)
print(screen.resolution)
assert screen.resolution == 786432, '1024 * 768 = %d ?' % screen.resolution
