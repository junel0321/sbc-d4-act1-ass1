import random

print("Welcome to Bootcamp Lottery!")

# User inputs their bet numbers
user_coordinates = []
for i in range(3):
    coordinate = int(input(f"Enter Coordinate {i+1} (0-9): "))
    user_coordinates.append(coordinate)

print("Your Bootcamp Coordinates are:", *user_coordinates)

# Generate random winning numbers
winning_numbers = [random.randint(0, 9) for _ in range(3)]
print("The Winning Bootcamp Coordinates are:", *winning_numbers)

# Check if user wins
if user_coordinates == winning_numbers:
    print("Congratulations, You've hit the Jackpot!")
elif sorted(user_coordinates) == sorted(winning_numbers):
    print("Hapit ra gyd You've Partial Win!")
else:
    print("Patad pa basin diay mo daug naka!")
