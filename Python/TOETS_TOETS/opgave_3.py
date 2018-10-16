from simulate import *
from collections import namedtuple

class Game():
    def __init__(_):
        _.players = []
        _.enemies = []

game_1 = Game()
game_1.players.append( Player("Jan") )
game_1.players.append( Player("Piet") )
game_1.players.append( Player("Hein") )
game_1.players.append( Player("Klaasen") )
game_1.players.append( Player("Henk") )

enemies = []
enemies.append( Boss("'Een moeilijke toets'") )



for speler in game_1.players:
    speler.target(*enemies)

for bozerik in enemies:
    bozerik.target(*game_1.players)


simulate( *game_1.players)


for speler in game_1.players:
    print(speler.name, speler.hp)

for bozerik in enemies:
    print(bozerik.name, bozerik.hp)







# OPGAVE 3 b

game_2 = Game()

class Mage(Player):
    def __init__(self, *args):
        super().__init__(*args)



class Warrior(Player):
    def __init__(self, *args):
        super().__init__(*args)
        self.hp = 5000
    
    def take_damage(self, hp):
        """Take 'hp' damage."""
        self.hp = min(self.initial_hp, max(0, self.hp - int(hp / 2)))

    def act(self, attack):
        """Perform attacks using the provided attack(target, hp) method.
        Return the number of seconds until the player can attack again.
        """
        attack(self.get_target(), 50)
        return 1



class Priest(Player):
    def __init__(self, *args):
        super().__init__(*args)
        self.hp = 2500
    
    def act(self, attack):
        """Perform attacks using the provided attack(target, hp) method.
        Return the number of seconds until the player can attack again.
        """
        attack(self.get_target(), 300)

        global game_2    # DIT IS HARDCODED DOOR TIJDGEBREK
        for player in game_2.players:
            player.hp += 200

        return 2





# OPGAVE 3 c
game_2.players.append( Warrior("Jan") )
game_2.players.append( Mage("Piet") )
game_2.players.append( Mage("Hein") )
game_2.players.append( Priest("Klaasen") )
game_2.players.append( Priest("Henk") )

enemies = []
enemies.append( Boss("'Een moeilijke toets'") )



for speler in game_2.players:
    speler.target(*enemies)

for bozerik in enemies:
    bozerik.target(*game_2.players)


simulate( *game_2.players)


for speler in game_2.players:
    print(speler.name, speler.hp)

for bozerik in enemies:
    print(bozerik.name, bozerik.hp)







# OPGAVE 3 d
class RaidBoss(Boss):
    def __init__(self, *args):
        super().__init__(*args)
    
    def act(self, attack):
        """Perform attacks using the provided attack(target, hp) method.
        Return the number of seconds until the boss can attack again.
        """
        for target in self.targets:
            if target.hp > 0:
                for target2 in self.targets:
                    if target2.hp > 0:
                        attack(target2, 50)

                attack(target, 1000)
                break
        return 2



game_3 = Game()
game_3.players.append( Warrior("Jan") )
game_3.players.append( Mage("Piet") )
game_3.players.append( Mage("Hein") )
game_3.players.append( Priest("Klaasen") )
game_3.players.append( Priest("Henk") )

enemies = []
enemies.append( RaidBoss("'Een moeilijke toets'") )



for speler in game_3.players:
    speler.target(*enemies)

for bozerik in enemies:
    bozerik.target(*game_3.players)


simulate( *game_3.players)


for speler in game_3.players:
    print(speler.name, speler.hp)

for bozerik in enemies:
    print(bozerik.name, bozerik.hp)