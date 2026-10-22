#=================================================================
#Name:            Teny Faye M. Obcena
#Section:         8 - Camia
#Date:            October 22, 2026
#Program Name:
#=================================================================

def display_intro():
    print("=================================================================")
    print("                    THREE-DOOR TREASURE HUNT                     ")
    print("=================================================================")

    player = input("Enter player name: ")

def show_weapons():
    print("Choose your weapon:")
    print("[1] Iron Sword - 30 Attack")
    print("[2] Magic Staff - 45 Attack")
    print("[3] Golden Axe - 60 Attack")

def choose_weapon(choice):
    choice = int(input("Enter weapon choice: "))
    if choice == 1:
        attack = 30
        return attack

    elif choice == 2:
        attack = 45
        return attack

    elif choice == 3:
        attack = 60
        return attack

def show_monsters():
    print("Choose your opponent:")
    print("[1] Green Slime - 20 Damage")
    print("[2] Forest Goblin - 40 Damage")
    print("[3] Fire Dragon - 70 Damage")

def monster_attack(monster):
    monster = 50
    monster = int(input("Enter monster choice: "))
    print("The monster attacks!")

    if monster == 1:
        damage = 20
        print(f"You received {damage} damage!")
        return damage

    elif monster == 2:
        damage = 40
        print(f"You received {damage} damage!")
        return damage

    elif monster == 3:
        damage = 70
        print(f"You received {damage} damage!")
        return damage

    print("You attacked using your weapon!")
    print(f"Attack Power: x ")

def calculate_health(health, damage):
    health = 100
    health = health - damage
    return health

def battle_result(attack, health, monster):


def get_rank(points):
    if points >= 70:
        rank = "LEGENDARY WARRIOR"
        return rank

    elif 40 <= points <= 69:
        rank = "ELITE FIGHTER"
        return rank

    elif 20 <= points <= 39:
        rank = "BRAVE BEGINNER"
        return rank

    else:
        rank ="ROOKIE WARRIOR"
        return rank

def display_report(player, health, points, rank, result):
    print("-------- BATTLE REPORT --------")
    print(f"Player: {player}")
    print(f"Remaining Health: {health}")
    print(f"Battle Points: {points}")
    print(f"Warrior Rank: {rank}")

    if attack >= 50 and health >= 0:
        print("Battle Result: VICTORY! ")

    else:
        print("Battle Result: DEFEAT! ")
    print("-------------------------------")


