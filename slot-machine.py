import random

# Define the symbols and their corresponding payouts
symbols = ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar", "Seven"]
payouts = {
    "Cherry": 2,
    "Lemon": 3,
    "Orange": 4,
    "Plum": 5,
    "Bell": 6,
    "Bar": 7,
    "Seven": 10
}

# Function to spin the slot machine
def spin_slot_machine():
    # Generate three random symbols
