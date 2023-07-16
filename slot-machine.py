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
    reels = [random.choice(symbols) for _ in range(3)]
    return reels

# Function to calculate the payout
def calculate_payout(reels):
    # Check if all three symbols are the same
    if len(set(reels)) == 1:
        symbol = reels[0]
        return payouts[symbol] * 10
    # Check if any two symbols are the same
    elif len(set(reels)) == 2:
        symbol = max(set(reels), key=reels.count)
        return payouts[symbol]
    else:
        return 0

# Function to play the game
def play_game():
    money = 100
    while money > 0:
        print("----- Slot Machine -----")
        print(f"Current Money: ${money}")
        input("Press Enter to spin the slot machine.")
        
        # Spin the slot machine
        reels = spin_slot_machine()
        
        # Calculate the payout
        payout = calculate_payout(reels)
        
        # Update the money balance
        money += payout
