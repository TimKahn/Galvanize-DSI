class Fruit(object):
    def __init__(self, weight):
        self.weight = weight

    def grow(self):
        print("Fruit is grown!")

    def eat(self):
        print("Fruit is eaten!")


class Banana(Fruit):
    def __init__(self, weight):
        super(Banana, self).__init__(weight)

    def peel(self, percentage):
        print("Banana is {}% peeled".format(percentage))

    def eat(self):
        for percentage in [50, 80, 92, 100]:
            self.peel(percentage)
            print("Eating some banana...")
        print("Banana is eaten!")


class Orange(Fruit):
    def __init__(self, weight):
        super(Orange, self).__init__(weight)

    def peel(self):
        print("Orange is peeled fully.")

    def eat(self):
        self.peel()
        print("Orange is eaten!")


class Apple(Fruit):
    def __init__(self, weight):
        super(Apple, self).__init__(weight)

    def wash(self):
        print("Apple is washed.")

    def eat(self):
        self.wash()
        print("Apple is eaten!")



if __name__ == '__main__':

    print("\nBanana:")
    banana = Banana(4.3)
    banana.grow()
    banana.eat()

    print("\nOrange:")
    orange = Orange(7.4)
    orange.grow()
    orange.eat()

    print("\nApple:")
    apple = Apple(6.5)
    apple.grow()
    apple.eat()
