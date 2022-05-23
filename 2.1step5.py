class Robot:
    @staticmethod
    def say_hello():
        print("Hello, human! My name is C-3PO")

    @staticmethod
    def say_bye():
        print("See u later alligator")


c3po = Robot()
c3po.say_hello()
c3po.say_bye()

r2d2 = Robot()
r2d2.say_hello()
r2d2.say_bye()
