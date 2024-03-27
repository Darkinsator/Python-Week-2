class Dog:
    _legs = 4
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + 'says: Bark!')

    def getLegs(self):
        return self._legs


class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says yap yap')

    def wagTail(self):
        print('Vigorously wagging!')

dog = Chihuahua('Roxy')
dog.speak()
dog.wagTail()

myDog = Dog('Rover')
myDog.speak()