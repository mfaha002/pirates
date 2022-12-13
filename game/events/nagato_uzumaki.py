from game import event
import random
from game.combat import Combat
from game.combat import Nagato
from game.display import announce

class NagatoUzumaki (event.Event):

    def __init__(self):
        self.name = " The world shall know pain!! "

    def process (self, world):
        result = {}
        result["message"] = " Nagato of the Rinnegan is defeated!"
        monsters = [Nagato("Nagato of the Rinnegan ")]
        announce ("The world shall know pain!! You are facing Nagato of the Rinnegan!")
        Combat(monsters).combat()
        result["newevents"] = [ self ]
        return result
