from abc import ABC, abstractmethod

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

class Animal(ABC):
    @abstractmethod
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    _protected_var = 1
    __private_var = 2
    __name = "abc"
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name: str):
        self.__name = name

    def speak(self):
        print(f"woof: {self.__name}")

    # @property
    # def dog_name(self):
    #     return f"{self.__name} is a dog"
    #
    # @dog_name.setter
    # def dog_name(self, name):
    #     print("sdadasdsa: ", name)
    #     self.__name = name

    def __getattr__(self, item):
        return self.__dict__[item]

    def __setattr__(self, key, value):
        self.__dict__[key] = value

# d1 = Dog("kkkk")
# d1.speak()
# print(d1)
#
# d2 = Dog("asdsad")
# d2.speak()
# print(d2)
# d1.dog_name = "abcooo"
# print(d1.dog_name)

# d1.name = "def"
# print(d1.name)



def num_gen():
    yield from range(10)

ng = num_gen()
print(next(ng))
print(next(ng))


