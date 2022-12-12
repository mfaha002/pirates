from game import event
import random
from game.combat import Combat
from game.combat import Itachi
from game.display import announce
import game.config as config


class ItachiUchiha(event.Event):

    def __init__(self):
        self.name = " itachi attacks"

    def process(self, world):
        result = {}
        result["message"] = "itachi the solo king is defeated! ...Those eyes are called the sharingan!"
        monsters = []
        n_appearing = random.randrange(0, 2)
        n = 1
        while n <= n_appearing:
            monsters.append(Itachi("Solo-King Itachi " + str(n)))
            n += 1
        announce("The crew is attacked by the solo king itachi!")
        Combat(monsters).combat()
        if random.randrange(2) == 0:
            result["newevents"] = [self]
        else:
            result["newevents"] = []
        config.the_player.ship.food += n_appearing * 2

        return result