from game import event
import random
from game.combat import Combat
from game.combat import Tobi
from game.display import announce

class TobiObito (event.Event):

    def __init__(self):
        self.name = " It is not worth living in this world with only despair exists!! "

    def process (self, world):
        result = {}
        result["message"] = " Tobi of the Akatsuki is defeated!"
        monsters = [Tobi("Tobi of the Akatsuki ")]
        announce (" It is not worth living in this world with only despair exists. You are facing Tobi of the Akatsuki!")
        Combat(monsters).combat()
        result["newevents"] = [ self ]
        return result