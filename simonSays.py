#Import our libraries
import random
import time

# Define the colors
COLORS = ["red", "green", "blue", "yellow"]

# Define the game parameters
SEQUENCE_LENGTH = 5
TIME_BETWEEN_MOVES = 2

# Store the generated sequence
sequence = []

# Function to generate the next move in the sequence
def generate_next_move():
    move = random.choice(COLORS)
    sequence.append(move)
    return move

# Function to display the sequence to the player
def display_sequence():
    for move in sequence:
        print("Simon says:", move)
        time.sleep(TIME_BETWEEN_MOVES)
        clear_console()

# Function to clear the console/terminal
def clear_console():
    print("\033c", end="")

# Function to handle player input and check if it matches the sequence
def handle_player_input():
    player_moves = []
    for move in sequence:
        player_move = input("Your turn: ").lower()
        player_moves.append(player_move)

        if player_move != move:
            player_loses()

    player_wins()

# Function when the player wins
def player_wins():
    print("Congratulations! You win!")

# Function when the player loses
def player_loses():
    print("Wrong move! Game over.")

# Generate the sequence and display it to the player
for _ in range(SEQUENCE_LENGTH):
    next_move = generate_next_move()

# Clear the console and display the sequence to the player
clear_console()
display_sequence()

# Start the game
handle_player_input()
