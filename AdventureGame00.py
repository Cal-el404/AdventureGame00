import time

def print_sleep(string):
    print(string)
    time.sleep(1)

def intro():
    print_sleep("Welcome to the land of Middle-Upper Earth.\n")
    print_sleep("You find yourself standing in a lush green valley.\n")
    print_sleep("In front of you runs a dirt road.\n")
    print_sleep("To your right is a thriving village called Brie.\n")
    print_sleep("To your left a mountain towers over the horizon.\n")
    print_sleep("Your quest is to bring the magic thimble to Lord Elfron "
                "in Riverdale.")
    print_sleep("Suddenly, a black knight appears on the roadway. "
                "With a queasy feeling, you know he is searching for you.")
    print_sleep("We'd best hide somewhere, you mutter to your companions.")

def choice():
    print_sleep("Where would you like to go?\n"
                "1. Go to the village tavern.\n"
                "2. Travel along the roadway.\n"
                "3. Hike up into the mountain.")

intro()
choice()