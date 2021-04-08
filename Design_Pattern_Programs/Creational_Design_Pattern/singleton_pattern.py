class SingletonPattern(object):
    instance = None

    @classmethod
    def instances(cls):
        if cls.instance is None:
            cls.instance = SingletonPattern()
        return cls.instance

    def __init__(self):
        if self.instance is not None:
            raise ValueError("A Singleton Methods instance is already existing")

    def set_data(self, number):
        self.number = number

    def get_data(self):
        return self.number


SingletonPattern.instances().set_data(input("Please enter number : "))
print("Data is : ", SingletonPattern.instances().get_data())
