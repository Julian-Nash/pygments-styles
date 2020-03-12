class AwesomeClass(object):
    """ Just an awesome class """

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        """ Say hello to the world """
        return "hello " + self.name
