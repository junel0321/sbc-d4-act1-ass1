import random  # Import the random module for generating random numbers

print("Welcome to Bootcamp Lottery!")  # Display a welcome message to the user

# User inputs their bet numbers
user_coordinates = []  # Initialize an empty list to store user's coordinates
for i in range(3):  # Loop three times to get three coordinates from the user
    coordinate = int(input(f"Enter Coordinate {i+1} (0-9): "))  # Prompt user to enter a coordinate
    user_coordinates.append(coordinate)  # Add the entered coordinate to the list

print("Your Bootcamp Coordinates are:", *user_coordinates)  # Display user's entered coordinates

# Generate random winning numbers
winning_numbers = [random.randint(0, 9) for _ in range(3)]  # Generate three random winning coordinates
print("The Winning Bootcamp Coordinates are:", *winning_numbers)  # Display randomly generated winning coordinates

# Check if user wins
if user_coordinates == winning_numbers:  # Check if user's coordinates match exactly with winning coordinates
    print("Congratulations, You've hit the Jackpot!")  # Display jackpot message if they match
elif sorted(user_coordinates) == sorted(winning_numbers):  # Check if sorted user's coordinates match sorted winning coordinates
    print("Hapit ra gyd You've Partial Win!")  # Display partial win message if they match in any order
else:
    print("Patad pa basin diay mo daug naka!")  # Display message indicating user did not win
