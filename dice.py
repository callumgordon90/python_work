from random import randint

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        rolls = randint(1, self.sides)
        print(f"You have rolled the dice {rolls} times!!!")

cally_dice = Dice(6)

cally_dice.roll_dice()
cally_dice.roll_dice()
cally_dice.roll_dice()
cally_dice.roll_dice()
cally_dice.roll_dice()

sumny_dice = Dice(10)

sumny_dice.roll_dice()
sumny_dice.roll_dice()
sumny_dice.roll_dice()
sumny_dice.roll_dice()
sumny_dice.roll_dice()


tharan_dice = Dice(20)

tharan_dice.roll_dice()
tharan_dice.roll_dice()
tharan_dice.roll_dice()
tharan_dice.roll_dice()
tharan_dice.roll_dice()

