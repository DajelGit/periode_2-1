import simulate

print("Opgave a:")

vijand1 = simulate.Boss("NAM")

players = [simulate.Player("Loppersum " + str(i)) for i in range(0, 5)]

print(players)

vijand1.target(*players)

for p in players:
    p.target(vijand1)

simulate.simulate(vijand1, *players)

print(vijand1.name, vijand1.hp)

for p in players:
    print(p.name, p.hp)

# ---

print("\n---\nOpgave b:")

class Mage(simulate.Player):
    pass

class Warrior(simulate.Player):
    def __init__(self, name, hp=5000):
        super().__init__(name, hp)

    def act(self, attack):
        attack(self.get_target(), 50)
        return 1

    def take_damage(self, hp):
        super().take_damage(hp/2)

class Priest(simulate.Player):
    companions = []

    def __init__(self, name, hp=2500):
        super().__init__(name, hp)

    def act(self, attack):
        alive = [c for c in self.companions if c.hp > 0]
        to_cure = min([self, *alive], key=lambda x: x.hp-x.initial_hp)
        print(self.name, "to_cure:", to_cure.name, to_cure.hp, to_cure.initial_hp)
        to_cure.take_damage(-400)
        print("after:", to_cure.hp)
        return 2

    def take_damage(self, hp):
        super().take_damage(hp/2)

# ---

print("\n---\nOpgave c:")

vijand2 = simulate.Boss("Shell")

players2 = [
    Warrior("Farmsum Warrior"),
    Mage("Farmsum Mage 1"),
    Mage("Farmsum Mage 2"),
    Priest("Farmsum Priest 1"),
    Priest("Farmsum Priest 2"),
]

players2[3].companions = players2
players2[4].companions = players2

vijand2.target(*players2)

for p in players2:
    p.target(vijand2)

simulate.simulate(vijand2, *players2)

print(vijand2.name, vijand2.hp)

for p in players2:
    print(p.name, p.hp)

# ---

print("\n---\nOpgave d:")

class RaidBoss(simulate.Boss):
    def act(self, attack):
        for t in self.targets:
            print("RaidBoss AOE damage")
            attack(t, 50)
        super().act(attack)
        return 2


vijand3 = RaidBoss("Raidboss Exxon")

players3 = [
    Warrior("Farmsum Warrior"),
    Mage("Farmsum Mage 1"),
    Mage("Farmsum Mage 2"),
    Priest("Farmsum Priest 1"),
    Priest("Farmsum Priest 2"),
]

players3[3].companions = players3
players3[4].companions = players3

vijand3.target(*players3)

for p in players3:
    p.target(vijand3)

simulate.simulate(vijand3, *players3)

print(vijand3.name, vijand3.hp)

for p in players3:
    print(p.name, p.hp)

