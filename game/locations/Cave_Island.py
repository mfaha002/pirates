from game import location
from game import config
from game.display import announce
from game.events import *



class Island (location.Location):

    def __init__ (self, x, y, w):
        super().__init__(x, y, w)
        self.name = "Cave Island"
        self.symbol = 'C'
        self.visitable = True
        self.starting_location = Beach_with_ship(self)
        self.locations = {}
        self.locations["beach"] = self.starting_location
        self.locations["Cave Entrance"] = Cave_Entrance(self)
        self.locations["First Room"] = First_Room(self)
        self.locations["Second Room"] = Second_Room(self)
        self.locations["Third Room"] = Third_Room(self)
        self.locations["Fourth Room"] = Fourth_Room(self)
        self.locations["Fifth Room"] = Fifth_Room(self)

    def enter (self, ship):
        print("There seems to be an island in with a cave in the distance.")

    def visit (self):
        config.the_player.location = self.starting_location
        config.the_player.location.enter()
        super().visit()

class Beach_with_ship (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "beach"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self

        

    def enter (self):
        announce ("You have anchored on the beach and are walking towards the cave's entrance.")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            announce ("You return to your ship.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["Cave Entrance"]
        else:
            announce ("It seems the Island is enchanted making you lose your sense of direction. You can only go "
                      "'north' or 'south'!")


class Cave_Entrance (location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "Cave Entrance"
        self.event_chance = 100
        self.events.append(white_zetsu.WhiteZetsu())


    def enter (self):
        announce("You have arrived at the front of the Cave's entrance.")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south" ):
            config.the_player.next_loc = self.main_location.locations["beach"]
        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["First Room"]


class First_Room (location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "First Room"
        self.verbs['read'] = self
        self.tries = 0
        self.solved = False

    def enter (self):
        announce("You defeated the enemies guarding the entrance. You notice a staircase leading downwards.")
        announce("You walk down the stairs to enter the first room of the dungeon. It seems to be a sign on the wall.")
        announce("The sign has a riddle written on it. You should probably READ it!")

    def process_verb(self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.locations["Cave Entrance"]
        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["Second Room"]
        elif (verb == "read"):
            while self.solved == False:
                print("If you want to make it to the next room you must first solve this riddle!"
                  " The riddle states: 'I have keys but no locks.; I have a space but no room.; "
                  "You can enter but can't go outside. What am I")
                print("You can enter the answer to the riddle or ask for a hint ")
                answer = input("What is the answer to the riddle?: ")
                if answer == "keyboard":
                    announce("You have unlocked the door to the next room!")
                    config.the_player.next_loc = self.main_location.locations["Second Room"]
                    self.solved = True
                elif answer == "hint":
                    print("I can be used by anyone no matter the WPM!")
                elif self.tries >= 2:
                    print("You have gotten it wrong. It was an easy riddle! Time to burn to death!")
                    config.the_player.gameInProgress = False
                    config.the_player.kill_all_pirates("Burned in the dungeon!")
                self.tries += 1



class Second_Room(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "Second Room"
        self.event_chance = 100
        self.events.append(itachi_uchiha.ItachiUchiha())

    def enter(self):
        announce("You made it past the first room! Congratulations, you get to fight to the death against Itachi Uchiha. ")

    def process_verb(self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.locations["First Room"]
        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["Third Room"]


#
#
class Third_Room(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "Third Room"
        self.event_chance = 100
        self.events.append(tobi.TobiObito())



    def enter(self):
        announce("You have made it to the third room. What's this Tobi is challenging you to a fight!")

    def process_verb(self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.locations["Second Room"]
        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["Fourth Room"]



#
#
class Fourth_Room(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "Fourth Room"
        self.event_chance = 100
        self.events.append(nagato_uzumaki.NagatoUzumaki())

    def enter(self):
        announce("You have managed to beat Tobi. Nagato of the Rinnegan was waiting for you! You think you have the will to face him. ")

    def process_verb(self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.locations["Third Room"]
        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["Fifth Room"]

#
#
class Fifth_Room(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "Fifth Room"


    def enter(self):
        announce("You make it to the last room of the dungeon where you thought you would find "
                 "a legendary sword like Samehada! But you were mistaken you fool!!!")

    def process_verb(self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.locations["Fourth Room"]
        if (verb == "north"):
            announce("You return to your ship.There was nothing in the dungeon for you to take!\n"
                     "Next time do not be so curious about a random cave!\n"
                     "You should listen to your parents because curiosity kills the cat!")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False







