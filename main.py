import csv

class InvalidChoiceError(Exception):
    pass
class Team():
    def __init__(self, player):
        self.player = player
        self.members = [None, None, None]
    def change_member(self,index,object):
        self.members[index] = object
class Pokemon():
    def __init__(self, id):
        self.id = id
        self.hp = int(pokereader[id][1])
        self.attack = int(pokereader[id][2])
        self.defense = int(pokereader[id][3])
        self.spattack = int(pokereader[id][4])
        self.spdefense = int(pokereader[id][5])
        self.speed = int(pokereader[id][6])
        self.type_primary = pokereader[id][7]
        self.type_secondary = pokereader[id][8]
        self.height = float(pokereader[id][9])
        self.weight = float(pokereader[id][10])
        self.gndr = pokereader[id][11][0]
        

with open('pokemon.csv', mode='r') as pokefile:
    pokereader = csv.reader(pokefile, delimiter=',')
    for indx, row in enumerate(pokereader):
        print(indx,row)


choice = None
while choice != "1": #Test the player's ability to follow basic instructions
    try:
        choice = input("\nType in the number corresponding to your choice.\n1: I understand.\n2: I do not understand.\n")
        if choice not in ["1","2"]:
            raise InvalidChoiceError("InvalidChoiceError: Input does not match with any options.")
    except InvalidChoiceError as e:
        print(e)


p1team = Team(1) #Team object for player 1
selection = True
while selection:
    try:
        choice = input("\nP1: What would you like to change?\n1: Change Team Members\n2: Modify Pokemon\n3: Done\n")
        if choice not in ["1","2", "3"]:
            raise InvalidChoiceError("InvalidChoiceError: Input does not match with any options.")
        subchoice = None
        if choice == "1": #Change Team Members
            while subchoice != "4":
                    subchoice = input(f"\nP1: What Pokemon do you want to change?\n1: {p1team.members[0]}\n2: {p1team.members[1]}\n3: {p1team.members[2]}\n4: Done\n")
                    if subchoice not in ["1","2","3","4"]:
                        print("InvalidChoiceError: Input does not match with any options.")
                    elif subchoice != "4":
                        change_pokemon = int(input("P1: Change to what Pokemon? (By Pokedex number)\n"))
                        p1team.change_member(int(subchoice)-1,Pokemon(change_pokemon))
        if choice == "3": #Check for valid team
            if None in p1team.members:
                print("InvalidTeamError: One or more team members are 'None'")
    except InvalidChoiceError as e:
        print(e)
game = True
while game:
    pass