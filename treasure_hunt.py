print("=================================")
print("            TREASURE HUNT        ")
print("      The Number Challenge       ")
print("=================================")

name = input("Enter player name: ")
coins = 0

for round in range (1, 4):
    print(f"\n---------ROUND {round}---------")
    guess = int(input("Guess the secret number: "))
    def check_guess(guess):
        if guess == 3:
            print("Correct! You earned 10 coins.")
            return 10
        else:
            print("Incorrect! You earned 0 coins.")
            return 0
    coins += check_guess(guess)

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
    title = get_achievement(coins)

def display_result(name, coins, title):
    print("\n=================================")
    print("            GAME RESULTS         ")
    print("=================================")
    print(f"Player: {name}")
    print(f"Total Coins: {coins}")
    print(f"Achievement: {title}")
    print("=================================")
    print("Thank you for playing!")
display_result(name, coins, title)
