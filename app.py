import random

for i in range(3):
    print(random.randint(10, 20))

for i in range(3):
    print(random.random())

members = ["Hazel", "Mary", "Reyna"]
leader = random.choice(members)
print(f"The leader is {leader}")

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
