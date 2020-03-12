class HelloWorld(object):
    """ Hello world class """

    def __init__(self, name: str):
        self.name = name

    def say_hello(self) -> str:
        """ Say hello to the world """
        return "hello " + self.name
