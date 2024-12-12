#######################################
#Name: Emmanuel Agboli
#Student: Number: A00300779
#ANA1001: Midterm Project
#Coursename: Programming for Analytics
#######################################


import random

#Welcome message

print("WELCOME TO MY BORING SPACE DRAGON ADVENTURE GAME!!!!")


# Initialize game variables
rooms = {
    'Space Station': {
        'description': 'A bustling space station with various shops and people.',
        'greeting': 'Welcome to the Space Station! The hub of intergalactic trade and travel.',
        'items': ['Laser Gun'],
        'characters': ['Merchant']
    }, # dictionary for Space Station
    'Dragon Lair': {
        'description': 'A dark, eerie lair with the dragon lurking in the shadows.',
        'greeting': 'You have entered the Dragon Lair! Beware of the mighty dragon.',
        'items': ['Treasure'],
        'characters': ['Dragon']
    }, # dictionary for Dragon Lair
    'Starship Bridge': {
        'description': 'The command center of a starship, with many controls and displays.',
        'greeting': 'Welcome to the Starship Bridge! Control the universe from here.',
        'items': [],
        'characters': ['Captain']
    }, # dictionary for Starship Bridge
    'Alien Planet': {
        'description': 'A strange planet with unusual flora and fauna.',
        'greeting': 'Welcome to the Alien Planet! Explore the unknown.',
        'items': ['Alien Artifact'],
        'characters': ['Alien']
    }, # dictionary for Alien Planet
    'Abandoned Mine': {
        'description': 'An old, deserted mine with rusty equipment.',
        'greeting': 'You have entered the Abandoned Mine! Watch your step.',
        'items': ['Gemstone'],
        'characters': []
    }, # dictionary for Abandoned Mine
}

room_list = list(rooms.keys()) # list of rooms
current_room = 'Space Station'
health = 100 # starting health of the player
money = 50  # Starting credits
backpack = [] # empty(starting) list for backpack
visited_rooms = set() # empty set for visited rooms

# Helper functions
def show_status(): # function to show status
    print(f"\nYou are in {current_room}") # print current room
    if current_room not in visited_rooms: 
        print(rooms[current_room]['greeting']) # print greeting for visited room
        visited_rooms.add(current_room)
    print(rooms[current_room]['description']) # print description for current room
    print(f"Health: {health}, Money: {money}, Backpack: {backpack}") # print health, money and backpack
    if rooms[current_room]['items']: # if there are items in the room
        print(f"You see the following items: {', '.join(rooms[current_room]['items'])}") # print items in the room
    if rooms[current_room]['characters']: # if there are characters in the room
        print(f"You see the following characters: {', '.join(rooms[current_room]['characters'])}") # print characters in the room

def show_rooms(): # function to show rooms
    print("\nRooms:") # print rooms
    for idx, room in enumerate(room_list, start=1): # loop through rooms
        print(f"{idx}. {room}") # print room number and name

def move_to_room(room_number): # function to move to room
    global current_room # use global variable
    if 1 <= room_number <= len(room_list): # if room number is valid
        current_room = room_list[room_number - 1] # move to room
        print(f"You move to the {current_room}.") # print message when you moved to a room
    else:
        print("Invalid room number!") # print message when you entered an invalid room number

def pick_up_item(item): # function to pick up item
    if item in rooms[current_room]['items']: 
        backpack.append(item) # add item to backpack
        rooms[current_room]['items'].remove(item) # remove item from room
        print(f"You picked up the {item}.") # print message when you picked up an item
        
        if item == 'Treasure':
            print("You found some money with the treasure!")
            increase_money(50) # increase money by 50
    else:
        print(f"There is no {item} here.") # print message when you entered an invalid item

def talk_to(character): # function to talk to a character
    if character in rooms[current_room]['characters']: # if character is in the room
        if character == 'Merchant': # if character is a merchant
            print("Merchant: I have many goods for sale.") # print merchant's message
            buy_or_sell = input("Do you want to buy a Laser Gun for 20 credits? (yes/no): ").strip().lower() # ask if you want to buy a Laser Gun
            if buy_or_sell == 'yes':
                buy_item('Laser Gun', 20) # buy a Laser Gun
        elif character == 'Dragon':# if character is a dragon
            print("Dragon: ROAR! You dare enter my lair!") # print dragon's message
            fight('Dragon') # fight the dragon
        elif character == 'Captain': # if character is a captain
            print("Captain: Welcome aboard, space traveler.") # print captain's message
        elif character == 'Alien': # if character is an alien
            print("Alien: *speaks in an alien language*") # print alien's message
    else:
        print(f"There is no {character} here.") # print message when you entered an invalid character

def fight(enemy): # function to fight an enemy
    global health # use global variable
    if enemy == 'Dragon':  # if enemy is a dragon
        print("You fight the dragon!") # print message when you fight a dragon
        outcome = random.choice(['win', 'lose']) # randomly choose win or lose
        if outcome == 'win': # if you win
            print("You defeated the dragon and took the treasure!") # print message when you defeated the dragon
            backpack.append('Treasure') # add treasure to backpack
            rooms[current_room]['characters'].remove('Dragon') # remove dragon from room
            increase_money(100)  # Reward for defeating the dragon
        else:
            print("The dragon defeated you.")
            decrease_health(50)  # Penalty for losing the fight

def increase_health(amount): # function to increase health
    global health
    health += amount # increase health by amount
    print(f"Your health increased by {amount} points. Current health: {health}") # print message when you increase health

def decrease_health(amount): # function to decrease health
    global health
    health -= amount # decrease health by amount
    print(f"Your health decreased by {amount} points. Current health: {health}") # print message when you decrease health
    if health <= 0: 
        print("You have died. Game over.") # print this message when your health is less than or equal to 0
        exit()

def increase_money(amount):
    global money
    money += amount
    print(f"You gained {amount} credits. Current money: {money}") # print message when you increase money

def decrease_money(amount):
    global money
    money -= amount
    print(f"You lost {amount} credits. Current money: {money}") # print message when you decrease money
    if money < 0:
        money = 0

def buy_item(item, cost):
    global money
    if money >= cost:
        money -= cost
        backpack.append(item)
        print(f"You bought a {item}. Current money: {money}") # print message when you buy an item
    else:
        print("You don't have enough money to buy this item.") # print message when you don't have enough money to buy an item

# Main game loop
while health > 0:
    show_status()
    show_rooms()
    action = input("\nWhat do you want to do? (move, pick up, talk, quit): ").strip().lower() # ask what you want to do

    if action == 'move':
        try:
            room_number = int(input("Enter the number of the room you want to go to: ").strip()) # ask what room you want to go to
            move_to_room(room_number)
        except ValueError:
            print("Invalid input! Please enter a number.") # print message when you entered an invalid input
    elif action == 'pick up':
        item = input("What do you want to pick up? ").strip().title() # ask what you want to pick up
        pick_up_item(item) # pick up item
    elif action == 'talk':
        character = input("Who do you want to talk to? ").strip().title() # ask who you want to talk to
        talk_to(character) # talk to character
    elif action == 'quit': # if you want to quit
        print("Thanks for playing!") # print message when you quit
        break
    else:
        print("Invalid action! Please choose move, pick up, talk, or quit.") # print message when you entered an invalid action

    if health <= 0:
        print("Game over! You have died.") # print message when your health is less than or equal to 0
        break
