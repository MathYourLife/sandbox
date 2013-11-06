class Descriptor:
    def __init__(self, name=None):
        self.name = name
    def __get__(self, instance, cls):
        print("Get", self.name)
    def __set__(self, instance, value):
        print("Set", self.name, value)
    def __delete__(self, instance):
        print("Delete", self.name)

class Stock(object):
    shares = Descriptor('shares')

a = Stock()
a.shares = 4

