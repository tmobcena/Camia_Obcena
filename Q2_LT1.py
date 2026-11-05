print("=================================================================")
print("                       TREASURE HUNT                             ")
print("                     The Number Challenge                        ")
print("=================================================================")
name = input("Enter player name: ")

for round in range(1,4):
    print(f"\n------- ROUND {round} -------")
    guess = int(input("Guess the secret number: "))
    def check_guess(guess):
        coins = 0
        if guess == 3:
            coins += 10
            print("Correct! You earned 10 points.")
        else:
            coins += 0
            print("Incorrect! You earned 0 coins.")
        return coins
    check_guess(guess)

def get_achievement(coins):
    if coins == 30:
        title = "Treasure Master"
    elif coins == 20:
        title = "Gold Explorer"
    elif coins == 10:
        title = "Bronze Explorer"
    else:
        title = "Treasure Beginner"
    return title

def display_result(name, coins, title):
    print("=================================================================")
    print("                          GAME RESULTS                           ")
    print("=================================================================")
    print(f"Player: {name}")
    print(f"Total Coins: {coins}")
    print(f"Achievement: {title}")
    print("=================================================================")
    print("Thank you for playing!")

coins = check_guess(guess)
name = get_achievement(coins)
title = get_achievement(coins)
display_result(name, coins, title)
