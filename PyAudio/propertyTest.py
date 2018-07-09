class dog(object):
    def __init__(self, age, poop):
        self._age = age
        self.poop = poop

    @property
    def age(self):
        print('property')
        return self._age

    @age.setter
    def age(self, value):
        self._age += value


a = dog(10, 10)
print(a.age)