class Player(object):
    def __init__(self, name, hp=2000):
        self.name = name
        self.initial_hp = hp
        self.hp = hp
        self.targets = []

    def take_damage(self, hp):
        """Take 'hp' damage."""
        self.hp = min(self.initial_hp, max(0, self.hp - hp))

    def target(self, *targets):
        """Set the target list to 'targets'."""
        self.targets = targets

    def get_target(self):
        """Get the current target."""
        for target in self.targets:
            if target.hp > 0:
                return target

    def act(self, attack):
        """Perform attacks using the provided attack(target, hp) method.
        Return the number of seconds until the player can attack again.
        """
        attack(self.get_target(), 300)
        return 2

    def is_player(self):
        """Get whether this is a player."""
        return True


class Boss:
    def __init__(self, name):
        self.name = name
        self.hp = 30000
        self.targets = []

    def take_damage(self, hp):
        """Take 'hp' damage."""
        self.hp = max(0, self.hp - hp)

    def target(self, *targets):
        """Set the target list to 'targets'"""
        self.targets = targets

    def act(self, attack):
        """Perform attacks using the provided attack(target, hp) method.
        Return the number of seconds until the boss can attack again.
        """
        for target in self.targets:
            if target.hp > 0:
                attack(target, 1000)
                break
        return 2

    def is_player(self):
        """Get whether this is a player."""
        return False


def simulate(*actors):
    """Simulate the boss fight for the given list of actors. Actors are players as well as enemies."""
    # create initial heap
    import heapq
    heap = []
    actor_dict = {}
    for a in actors:
        heapq.heappush(heap, (0, a.name))
        actor_dict[a.name] = a

    while True:
        # get next actor
        time, name = heapq.heappop(heap)
        actor = actor_dict[name]

        # define attack function
        def attack(target, hp):
            """Attack 'target' for 'hp' damage."""
            if target is not None and target.hp > 0:
                # damage target
                old_hp = target.hp
                target.take_damage(hp)
                hp = target.hp - old_hp

                # give feedback
                print(time, 'sec:', actor.name, 'heals' if hp >= 0 else 'attacks', target.name, 'for', abs(hp), 'hp')
                if target.hp > 0:
                    print(time, 'sec:', target.name, 'has', target.hp, 'hp')
                else:
                    print(time, 'sec:', target.name, 'dies')

        # only allow actor to act if they are still alive
        if actor.hp > 0:
            # increase time by the amount of time the actor takes
            time += max(1, actor.act(attack) or 1)

            # add to heap
            heapq.heappush(heap, (time, actor.name))

        # terminate simulation if either players or enemies are all dead
        players_found = False
        enemies_found = False
        for time, name in heap:
            actor = actor_dict[name]
            if actor.is_player():
                players_found = True
            else:
                enemies_found = True
        if not players_found or not enemies_found:
             break
