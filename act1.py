import random

# Initialize scores for three players
player1_scores, player2_scores, player3_scores = 0, 0, 0

# Main game loop
while True:
    # Player 1 (P1) inputs their choice: FOLD, UNFOLD, or EXIT to quit
    player1 = input("P1, choose FOLD or UNFOLD (or type 'exit' to quit): ").strip().upper()
    
    # Check if player1 wants to exit the game
    if player1 == "EXIT":
        break  # Exit the loop if player1 types 'exit'
    
    # Validate player1's choice
    elif player1 not in ["FOLD", "UNFOLD"]:
        print("Invalid choice. Please choose FOLD or UNFOLD.")
        continue  # Continue to the next iteration of the loop if choice is invalid

    # Computer players (Computer 1 and Computer 2) make random choices between FOLD and UNFOLD
    player2 = random.choice(["FOLD", "UNFOLD"])
    player3 = random.choice(["FOLD", "UNFOLD"])

    # Print out the choices made by all players
    print(f"P1: {player1}")
    print(f"Computer 1 picks: {player2}")
    print(f"Computer 2 picks: {player3}")

    # Determine the winner based on the choices
    if player1 != player2 and player1 != player3:
        print("P1 wins!\n")
        player1_scores += 1  # Increment P1's score if they win
    elif player2 != player1 and player2 != player3:
        print("Computer 1 wins!\n")
        player2_scores += 1  # Increment Computer 1's score if they win
    elif player3 != player1 and player3 != player2:
        print("Computer 2 wins!\n")
        player3_scores += 1  # Increment Computer 2's score if they win
    else:
        print("It's a tie!\n")

# After exiting the loop, print the final scores
print("FINAL SCORES")
print(f"P1: {player1_scores}, Computer 1: {player2_scores}, Computer 2: {player3_scores}")
