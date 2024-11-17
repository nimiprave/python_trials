class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('running')


player1 = PlayerCharacter('Cindy')
print(player1.name)
player1.run()
print(type(player1))
print(player1)

player2 = PlayerCharacter('Tom')
print(player2.name)


# Member variables
class Player:
    # class object attribute
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showSelf(self):
        print(self.name + ' ' + str(self.age))


tony = Player('Tony', 23)
tony.showSelf()
