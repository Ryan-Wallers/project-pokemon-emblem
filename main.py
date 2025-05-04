import csv
import time
import random

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
        self.state = None

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

class Game():
    def __init__(self,team1,team2):
        self.teams = [team1,team2]
        self.field = [None,None]
        self.movechoice = [None,None]
        self.turn_order = [0,1]

with open('pokemon.csv', mode='r') as pokefile:
    pokereader = csv.reader(pokefile, delimiter=';')
    pokedex = []
    for row in pokereader:
        pokedex.append(row)

with open('moves.csv', mode='r') as movefile:
    movereader = csv.reader(movefile, delimiter=',')
    movedex = []
    for row in movereader:
        movedex.append(row)

#pokedex and movedex are lists of lists, with each list in them corresponding to a specific Pokemon or move. List 0 is the header in both variables.

def displayteam(team):
    for num, member in enumerate(team.members):
        if member == None:
            print(f'{num+1}: -')
        elif member.state != None:
            print(f'{num+1}: {member.name} - {member.state}')
        else:
            print(f'{num+1}: {member.name}')

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
                        displayteam(team)
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
                    print(f"\n{name}: What Pokemon do you want to modify?")
                    displayteam(team)
                    print("4: Done")
                    secchoice = input()
                    if secchoice not in ["1","2","3","4"]:
                        print("InvalidChoiceError: Input does not match with any options.")
                    elif secchoice != "4":
                        if team.members[int(secchoice)-1] == None:
                            print("InvalidChoiceError: Selected Pokemon does not exist.")
                        else:
                            terchoice = None
                            while terchoice != "2": #Picking what to modify
                                terchoice = input(f'\n{name}: What aspect would you like to modify?\n1: Moves\n2: Done\n')
                                if terchoice not in ["1","2"]:
                                    print("InvalidChoiceError: Input does not match with any options.")
                                elif terchoice != "2":
                                    quachoice = None
                                    while quachoice != "6": #Changing moves
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
                        if member != None:
                            if all(x == None for x in member.moves):
                                raise InvalidTeamError("InvalidTeamError: Each member must have at least one move.")
                            
                    selection = False
        except InvalidChoiceError as e:
            print(e)
        except InvalidTeamError as e:
            print(e)

def switch(team): #Switches Pokemon in battle
    sendout = True
    while sendout:
        print(f'\nP{team.player+1}: Which Pokemon will you send out?')
        displayteam(team)
        if battle.field[team.player] != None:
            print('5: Cancel')
        choice = input()
        if battle.field[team.player] != None and choice == "5":
            sendout = False
            return True
        elif choice not in ["1","2","3","4"]:
            print("InvalidChoiceError: Input does not match with any options.")
        elif team.members[int(choice)-1] == None:
            print("InvalidChoiceError: Selected Pokemon does not exist.")
        elif team.members[int(choice)-1].state == "faint":
            print("InvalidChoiceError: Selected Pokemon has fainted.")
        elif team.members[int(choice)-1] == battle.field[team.player]:
            print("InvalidChoiceError: Selected Pokemon is already on the field.")
        else:
            battle.field[team.player] = team.members[int(choice)-1]
            battle.movechoice[team.player] = "switch"
            sendout = False
            return False

def movechoose(team):
    choose = True
    while choose:
        print(f"\nP{team.player+1}: What will {battle.field[team.player].name} do?")
        for num, move in enumerate(battle.field[team.player].moves):
            if move == None:
                print(f'{num+1}: -')
            else:
                print(f'{num+1}: {move.name}')
        print("5: Switch")
        choice = input()
        if choice not in ["1","2","3","4","5"]:
            print("InvalidChoiceError: Input does not match with any options.")
        elif choice == "5":
            choose = switch(p1team)
        elif battle.field[team.player].moves[int(choice)-1] == None:
            print("InvalidChoiceError: Selected move does not exist.")
        else:
            battle.movechoice[team.player] = battle.field[team.player].moves[int(choice)-1]
            choose = False

def calcdamage(move, attacker, defender):
    if move.category == "special":
        atk = attacker.spattack
        dfs = defender.spdefense
    else:
        atk = attacker.attack
        dfs = defender.defense
    if move.type == attacker.type_primary or move.type == attacker.type_secondary:
        stab = 1.5
    else:
        stab = 1
    typ_bonus = 1
    return (int((((((2*25)/5+2)*move.power*atk/dfs)/50+2)*stab*typ_bonus*random.randint(217,255))//255), typ_bonus)



#--------------------------- Interactive portion begins HERE ----------------------------



choice = None
while choice != "1": #Test the player's ability to follow basic instructions
    try:
        choice = input("\nType in the number corresponding to your choice.\n1: I understand.\n2: I do not understand.\n")
        if choice not in ["1","2"]:
            raise InvalidChoiceError("InvalidChoiceError: Input does not match with any options.")
    except InvalidChoiceError as e:
        print(e)


p1team = Team(0) #Team object for player 1
teamselect(p1team, "P1")
print("\n\n\n-----[No peeking, Player two!]-----\n\n\n")
p2team = Team(1) #Team object for player 2
teamselect(p2team, "P2")

battle = Game(p1team, p2team)


print("\n\n\n-----[GAME ]-----\n-----[START]-----\n\n\n")

switch(p1team)
print("\n\n\n-----[No peeking, Player two!]-----\n\n\n")
switch(p2team)

game = True
while game:
    movechoose(p1team)
    print("\n\n\n-----[No peeking, Player two!]-----\n\n\n")
    movechoose(p2team)
    input("\n\n\n\n\n\nAre both players ready? (Type anything to continue)")
    if battle.movechoice[0] == "switch":
        print(f"P1 swapped to {battle.field[0].name}!")
        time.sleep(1)
    if battle.movechoice[1] == "switch":
        print(f"P2 swapped to {battle.field[1].name}!")
        time.sleep(1)
    battle.turn_order = [0,1]
    if battle.field[1].speed > battle.field[0].speed:
        battle.turn_order = battle.turn_order[::-1]
    first = battle.turn_order[0]
    second = battle.turn_order[1]
    if battle.movechoice[first] != "switch":
        print(f"P{first+1}'s {battle.field[first].name} used {battle.movechoice[first].name}!")
        time.sleep(1.5)
        if random.randint(1, 100) <= battle.movechoice[first].accuracy:
            damage, effective = calcdamage(battle.movechoice[first], battle.field[first], battle.field[second])
            if effective > 1:
                print("It's super effective!")
            elif effective < 1:
                print("It's not very effective...")
            battle.field[second].hp -= damage
            print("It dealt",damage,"damage!")
        else:
            print("But it missed!")
        time.sleep(1.5)
    if battle.field[second].hp < 1:
        battle.field[second].state = "faint"
        print(f"P{second+1}'s {battle.field[second].name} fainted!")
        time.sleep(1.5)
        wiped = True
        for member in battle.teams[second].members:
            if member != None:
                if member.state != "faint":
                    wiped = False
        if wiped:
            game = False
            winner = "Player 2"
            break
        else:
            switch(battle.teams[second])
    else:
        if battle.movechoice[second] != "switch":
            print(f"P{second+1}'s {battle.field[second].name} used {battle.movechoice[second].name}!")
            time.sleep(1.5)
            if random.randint(1, 100) <= battle.movechoice[second].accuracy:
                damage, effective = calcdamage(battle.movechoice[second], battle.field[second], battle.field[first])
                if effective > 1:
                    print("It's super effective!")
                elif effective < 1:
                    print("It's not very effective...")
                battle.field[second].hp -= damage
                print("It dealt",damage,"damage!")
            else:
                print("But it missed!")
            time.sleep(1.5)
    if battle.field[first].hp < 1:
        battle.field[first].state = "faint"
        print(f"P{first+1}'s {battle.field[first].name} fainted!")
        time.sleep(1.5)
        for member in battle.teams[first].members:
            if member != None:
                if member.state != "faint":
                    wiped = False
        if wiped:
            game = False
            winner = "Player 2"
            break
        else:
            switch(battle.teams[first])

print(winner,"WINS!!!")

        