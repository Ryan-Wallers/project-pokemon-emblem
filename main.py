import csv

class InvalidChoiceError(Exception):
    pass

class InvalidTeamError(Exception):
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
        self.name = pokedex[id][0].capitalize()
        self.hp = int(pokedex[id][1])
        self.attack = int(pokedex[id][2])
        self.defense = int(pokedex[id][3])
        self.spattack = int(pokedex[id][4])
        self.spdefense = int(pokedex[id][5])
        self.speed = int(pokedex[id][6])
        self.type_primary = pokedex[id][7]
        self.type_secondary = pokedex[id][8]
        self.height = float(pokedex[id][9])
        self.weight = float(pokedex[id][10])
        self.gndr = pokedex[id][11][0]
        self.moves = [None, None, None, None]

class Move():
    def __init__(self, id):
        self.id = id
        self.name = movedex[id][0].capitalize()
        self.type = movedex[id][1]
        self.category = movedex[id][2]
        self.power = int(movedex[id][3])
        self.accuracy = int(movedex[id][4])
        self.power_points = int(movedex[id][5])
        self.contact = movedex[id][6] == "yes"

with open('pokemon.csv', mode='r') as pokefile:
    pokereader = csv.reader(pokefile, delimiter=',')
    pokedex = []
    for row in pokereader:
        pokedex.append(row)

with open('moves.csv', mode='r') as movefile:
    movereader = csv.reader(movefile, delimiter=',')
    movedex = []
    for row in movereader:
        movedex.append(row)

def teamselect(team, name):
    selection = True
    while selection:
        try:
            choice = input(f"\n{name}: What would you like to change?\n1: Change Team Members\n2: Modify Pokemon\n3: Done\n")
            if choice not in ["1","2", "3"]:
                raise InvalidChoiceError("InvalidChoiceError: Input does not match with any options.")
            secchoice = None
            if choice == "1": #Change Team Members
                while secchoice != "4":
                        print(f"\n{name}: What Pokemon do you want to change?")
                        for num, member in enumerate(team.members):
                            if member == None:
                                print(f'{num+1}: -')
                            else:
                                print(f'{num+1}: {member.name}')
                        print("4: Done")
                        secchoice = input()
                        if secchoice not in ["1","2","3","4"]:
                            print("InvalidChoiceError: Input does not match with any options.")
                        elif secchoice != "4":
                            try:
                                change_pokemon = int(input(f"\n{name}: Change to what Pokemon? (By Pokedex number)\n"))
                                team.change_member(int(secchoice)-1,Pokemon(change_pokemon))
                            except ValueError as e:
                                print('ValueError: Input is not a number')
                            except IndexError as e:
                                print('IndexError: Input outside of range.')
            if choice == "2": #Modify Pokemon
                while secchoice != "4":
                    print(f"\n{name}: What Pokemon do you want to change?")
                    for num, member in enumerate(team.members):
                        if member == None:
                            print(f'{num+1}: -')
                        else:
                            print(f'{num+1}: {member.name}')
                    print("4: Done")
                    secchoice = input()
                    if secchoice not in ["1","2","3","4"]:
                        print("InvalidChoiceError: Input does not match with any options.")
                    elif secchoice != "4":
                        if team.members[int(secchoice)-1] == None:
                            print("InvalidChoiceError: Selected Pokemon does not exist.")
                        else:
                            terchoice = None
                            while terchoice != "2":
                                terchoice = input(f'\n{name}: What aspect would you like to change?\n1: Moves\n2: Done\n')
                                if terchoice not in ["1","2"]:
                                    print("InvalidChoiceError: Input does not match with any options.")
                                elif terchoice != "2":
                                    quachoice = None
                                    while quachoice != "6":
                                        print(f"\n{name}: What move do you want to change?")
                                        for num, move in enumerate(team.members[int(secchoice)-1].moves):
                                            if move == None:
                                                print(f'{num+1}: -')
                                            else:
                                                print(f'{num+1}: {move.name}')
                                        print("5: View Options")
                                        print("6: Done")
                                        quachoice = input()
                                        if quachoice not in ["1","2","3","4","5","6"]:
                                            print("InvalidChoiceError: Input does not match with any options.")
                                        elif quachoice == "5":
                                            for i, move in enumerate(movedex):
                                                if i != 0:
                                                    print(f'{i}: {move[0].capitalize()}')
                                        elif quachoice != "6":
                                            try:
                                                qinchoice = int(input(f"\n{name}: Change to what move? (By number)\n"))
                                                team.members[int(secchoice)-1].moves[int(quachoice)-1] = Move(qinchoice)
                                            except ValueError as e:
                                                print('ValueError: Input is not a number')
                                            except IndexError as e:
                                                print('IndexError: Input outside of range.')
            if choice == "3": #Check for valid team
                if all(x == None for x in team.members):
                    raise InvalidTeamError("InvalidTeamError: One or more team members are needed.")
                else:
                    for member in team.members:
                        if all(x == None for x in member.moves):
                            raise InvalidTeamError("InvalidTeamError: Each member must have at least one move.")
                            
                    selection = False
        except InvalidChoiceError as e:
            print(e)
        except InvalidTeamError as e:
            print(e)

choice = None
while choice != "1": #Test the player's ability to follow basic instructions
    try:
        choice = input("\nType in the number corresponding to your choice.\n1: I understand.\n2: I do not understand.\n")
        if choice not in ["1","2"]:
            raise InvalidChoiceError("InvalidChoiceError: Input does not match with any options.")
    except InvalidChoiceError as e:
        print(e)


p1team = Team(1) #Team object for player 1
teamselect(p1team, "P1")
p2team = Team(2)
teamselect(p2team, "P2")



game = True
while game:
    break