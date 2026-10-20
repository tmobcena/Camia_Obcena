#=================================================================
#Name:            Teny Faye M. Obcena
#Section:         8 - Camia
#Program Name:    THREE-DOOR TREASURE HUNT
#=================================================================

def display_intro():
    print("=================================================================")
    print("                    THREE-DOOR TREASURE HUNT                     ")
    print("=================================================================")

    player = input("Enter your name: ")
    print(f"Welcome to the castle, {player}!")
    show_doors(player)

def show_doors(player):
    print("Choose your door: [1] Wooden  [2] Red [3] Golden")
    choice = input("Enter your choice: ")
    explore_door(choice, player)

def explore_door(choice, player):
    score = 20

    if choice == "1":
        print("You discovered a treasure chest!")
        print("You earned 50 points!")
        score += 50

    elif choice == "2":
        print("Oh no! You awakened a dragon!")
        print("You lost 20 points!")
        score -= 20

    else:
        print("You discovered a  magical key!")
        print("You earned 30 points!")
        score += 30
    display_result(player, score)

def display_result(player, score):
    print("---------------------GAME RESULT----------------------------")
    print(f"Player: {player}      Starting Points: 20")
    print(f"Total Score: {score}")

    if score >= 70:
        achievement = "TREASURE MASTER"

    elif 40 <= score >= 69:
        achievement = "BRAVE EXPLORER"

    else:
        achievement = "BEGINNER ADVENTURER"

    print(f"Achievement: {achievement}")

display_intro()