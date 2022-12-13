from game import event
import random
from game.combat import Combat
from game.combat import Itachi
from game.display import announce

class ItachiUchiha (event.Event):

    def __init__(self):
        self.name = " It is foolish to fear what we have yet to see and know!! "

    def process (self, world):
        result = {}
        result["message"] = " Itachi of the Sharingan is defeated!"
        monsters = [Itachi("Itachi of the Sharingan ")]
        announce ("You are facing Itachi of the Sharingan! It is foolish to fear what we have yet to see and know!!")
        Combat(monsters).combat()
        result["newevents"] = [ self ]
        return result