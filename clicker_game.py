from clicker import Pet
#import time as t
#from Python import pynput
#import Key, Listener
print("Hello, in this game, you get coins every time you type.Your aim is to get the most coins, and you need to buy more pets or multipliers in order to do so. The pets are able to give you more coins: the higher the multiplier of the pet, the more coins you get, and the more expensive it costs. The multipliers multiply your total money outcome every second by a fixed amount, they cost money.")
print("To get to the shop, press 's'; to find out your coins, press 'c'; to see your pets, press 'p'; to see activated/equipt pets, press 'a'; to see income, press 'i'; to buy pets, press 'b', and then type the name when asked to do so.")
coins = 0
Wasp = Pet("Wasp", 2.5, 10)
Bunny = Pet("Bunny", 5, 60)
Rabbit = Pet("Rabbit", 7.5, 100)
Mole = Pet("Mole", 10, 1000)
Fox = Pet("Fox", 12.5, 1500)
Penguin = Pet("Penguin", 15, 2000)
Cat = Pet("Cat", 17.5, 3000)
Dog = Pet("Dog", 20, 5000)
Fast_Bunny = Pet ("Fast Bunny", 50, 6000)
Fast_Rabbit = Pet("Fast Rabbit", 75, 20000)
Fast_Mole = Pet("Fast Mole", 100, 100000)
Fast_Fox = Pet("Fast Fox", 125, 150000)
Fast_Penguin = Pet("Fast Penguin", 150, 300000)
Fast_Cat = Pet("Fast Cat", 175, 500000)
Fast_Dog = Pet("Fast Dog", 200, 1000000)
Elephant = Pet("Elephant", 50, 6000)
Leopard = Pet("Leopard", 60, 8000)
Tiger = Pet("Tiger", 70, 15000)
Alligator = Pet("Alligator", 80, 60000)
Scorpion = Pet("Scorpion", 90, 80000)
Rhinoceros = Pet("Rhinoceros", 100, 100000)
Wasps = Pet("Swarm of Wasps", 2500, 100000000)
Elephants = Pet("Herd of Elephants", 50000, 2000000000)
Leopards = Pet("Leap of Leopards", 60000, 300000000000)
Tigers = Pet("Streak of Tigers", 70000, 40000000000000)
Alligators = Pet("Congregation of Alligator", 80000, 8000000000000000)
Scorpions = Pet("Bed of Scorpions", 90000, 30000000000000000000)
Rhinoceroses = Pet("Crash of Rhinoceroses", 100000, 1000000000000000000000000)
pets_list = [Wasp, Bunny, Rabbit, Mole, Fox, Penguin, Cat, Dog, Fast_Bunny, Fast_Rabbit, Fast_Mole, Fast_Fox, Fast_Dog, Elephant, Leopard, Tiger, Alligator, Scorpion, Rhinoceros, Wasps, Elephants, Leopards, Tigers, Alligators, Scorpions, Rhinoceroses]
My_pets = []


"""
def key_press():
    key = input("")
    if key == 's':
        for item in pets_list:
            print(item.name)
            print(item.multiplier)
            print(item.cost)
    elif key == 'c':
        print(coins)
    elif key == 'b':
        answer = input("Please type the name of the pet you would like to buy")
        if coins > answer.cost:
            answer.buy
            coins = coins - answer.cost
            My_pets.insert(0, answer)
    elif key == 'e':
        answer = input("Please type the name of the pet you would like to equipt")
        if answer.active == True:
            for item in My_pets:
                item.active = False
            answer.active = True
        else:
            print("Pet is not owned or does not exist.")
    else:
        print("Please type in something suitable")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        key_press = key_press,
        on_release=on_release) as listener:
    listener.join()
"""
#experimenting with pynput, could not manage to get it to work

while True:
#    t.sleep(1)
    coins = coins + 1
    for pet in pets_list:
        if pet.active == True:
            coins = coins + pet.multiplier
        else:
            continue
    key = input("")
    if key == 's':
        for item in pets_list:
            print("Name: {0} , Multiplier: {1} , Cost: {2}".format(item.name, item.multiplier, item.cost))
#            print(item.multiplier)
#            print(item.cost)
    elif key == 'c':
        print(coins)
    elif key == 'b':
        answer = input("Please type the name of the pet you would like to buy: ")
        for item in pets_list:
            if item.name == answer:
                if coins > item.cost:
                    item.buy
                    coins = coins - item.cost
                    My_pets.append(item)
                    print("Pet bought!")
                else:
                    continue
            else:
                continue
#        if coins > answer.cost:
#           answer.buy
#            coins = coins - answer.cost
#            My_pets.insert(0, answer)
    elif key == 'e':
        answer = input("Please type the name of the pet you would like to activate/equipt: ")
        for item in My_pets:
            if item.name == answer:    #finding if the pet is owned
#                for item in My_pets:   #unactivating other pets in use... 
#                    item.acive = False       #I decided to make it so that pet stats can 'stack': they add to the amount of coins per second
                for item in My_pets:
                    if item.name == answer: #finding the pet that is owned (again)
                            item.active = True
                            print("All of that type of pet have been equipt!")
                    else:
                        continue
            else:
                print("Finding pet...")
    elif key == 'p':
#        print(My_pets)
        for item in My_pets:
            print(item.name)
#        if answer.active == True:
#            for item in My_pets:
#                item.active = False
#            answer.active = True
#        else:
#            print("Pet is not owned or does not exist.")
    elif key == 'a':
        for item in My_pets:
            if item.active == True:
                print("{} is activated".format(item.name))
            else:
                print("{} not activated...".format(item.name))
        if len(My_pets) == 0:
            print("No pets activated/equipt.")
    elif key == 'i':
        x = 0
        for item in My_pets:
            if item.active == True:
                x = x + item.multiplier + 1
            else:
                print("A pet is not active!")
        print("Current income: {}".format(x))
   # elif key == 'f':
   #     coins = 10000000000000000000000000000000000
    else:
        print("Please type in something suitable")





            