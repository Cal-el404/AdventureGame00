import time
import random


def print_sleep(string):
    print(string)
    time.sleep(1)


def intro(enemy):
    print_sleep("Welcome to the land of Middle-Upper Earth.\n")
    print_sleep("You find yourself standing in a lush green valley, "
                "along with your three unnamed traveling companions.\n")
    print_sleep("In front of you runs a dirt road.\n")
    print_sleep("To your right is a thriving village called Brie.\n")
    print_sleep("To your left a mountain towers over the horizon.\n")
    print_sleep("Your quest is to bring the magic thimble to Lord Elfron "
                "in Riverdale.\n")
    print_sleep(f"Suddenly, a {enemy} appears on the roadway. \n")
    print_sleep("With a queasy feeling, you know he is searching for you.\n")
    print_sleep("We'd best hide somewhere, you mutter to your companions.\n")


def choice(items, enemy):
    response = input("Where would you like to go?\n"
                     "1. Go to the village tavern.\n"
                     "2. Travel along the roadway.\n"
                     "3. Hike up into the mountain.\n").lower()
    if response == '1':
        tavern(items, enemy)
    elif response == '2':
        black_knight(items, enemy)
    elif response == '3':
        mountain(items, enemy)
    else:
        choice(items, enemy)


def tavern(items, enemy):
    if 'ranger' in items:
        print_sleep("The ranger-guide says, 'We really should be on our way.'")
        choice(items, enemy)
    else:
        print_sleep("You and your companions make your way to the village "
                    "tavern called the Frolicking Foal.\n")
        print_sleep("There you meet a Ranger who offers to take you to "
                    "your destination as your guide.\n")
        print_sleep("He reveals he is an ally of your mutual wizard "
                    "friend Gandwarf.\n")
        print_sleep("You heartily accept the offer.\n")
        items.append('ranger')
        choice(items, enemy)


def black_knight(items, enemy):
    if 'ranger' and 'wizard' in items:
        print_sleep(f"With the combined power of your team's ranger, "
                    f"wizard, and your sneakiness; the {enemy} "
                    "turns tail and flees all the way back to Mardor.")
        print_sleep("You safely arrive in Riverdale and deliver the "
                    "magic thimble to Lord Elfron.\n")
        print_sleep("You have successfully accomplished your quest!")
        play_again()
    elif 'ranger' in items:
        print_sleep(f"The ranger advises you that it is best to avoid the "
                    f"{enemy} for now, and head into the mountain.\n")
        print_sleep(f"There you can avoid danger and possibly find a way to "
                    f"defeat the {enemy}.\n")
        choice(items, enemy)
    else:
        print_sleep(f"As you begin to walk down the road way. The {enemy} "
                    "appears to grow larger and more menacing.\n")
        print_sleep("You feel a sense of dread growing in the"
                    " pit of your stomach.")
        print_sleep("Suddenly you feel your friends grab your cloak.\n")
        print_sleep("They drag you back to the green valley where "
                    "it was last safe.\n")
        choice(items, enemy)


def mountain(items, enemy):
    if 'wizard' in items:
        print_sleep("There is nothing else to do on the mountain.\n")
        choice(items, enemy)
    elif 'ranger' in items:
        print_sleep("The ranger shows you a hidden pass.\n")
        print_sleep("Halfway through the mountain pass, you meet your wizard "
                    "friend Gandwarf!")
        print_sleep("He joins your party, and your quest!\n")
        print_sleep(f"Your party advises you that they are now ready "
                    f"to face the {enemy}.\n")
        items.append('wizard')
        choice(items, enemy)
    else:
        print_sleep("You start up the mountain, but are snowed out "
                    "by a blizzard.\n")
        print_sleep("The mountain doesn't seem to want to let "
                    "you through yet.\n")
        print_sleep("Your friends say you need a guide to navigate "
                    "the mountain.\n")
        print_sleep("Maybe there is a guide back at Brie...?\n")
        choice(items, enemy)


def play_again():
    again = input("Would you like to play again?\n"
                  "Please say yes or no.\n").lower()
    if again == 'yes':
        play_game()
    elif again == 'no':
        print_sleep("Goodbye.")
    else:
        play_again()


def play_game():
    enemies = ['black knight', 'ogre', 'dragon', 'screaming banshee', 'pirate']
    enemy = random.choice(enemies)
    items = []
    intro(enemy)
    choice(items, enemy)


play_game()
