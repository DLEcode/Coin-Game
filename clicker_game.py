from clicker import Pet
import time as t
print("Hello, in this game you get coins every time you type.Your aim is to get the most coins, and you need to buy more pets or multipliers in order to do so. The pets are able to give you more coins: the higher the multiplier of the pet, the more coins you get, and the more expensive it is. The multipliers multiply your total money outcome every second by a fixed amount.")
print("To get to the shop, press 's'; to find out your coins, press 'c'; to see your pets, press 'p'; to see activated/equipt pets, press 'a'; to see income, press 'i'; to buy pets, press 'b', and then type the name when asked to do so.")
coins = 0
Wasp = Pet("wasp", 2.5, 10)
Bunny = Pet("bunny", 5, 60)
Rabbit = Pet("rabbit", 7.5, 100)
Mole = Pet("mole", 10, 1000)
Fox = Pet("fox", 12.5, 1500)
Penguin = Pet("penguin", 15, 2000)
Cat = Pet("cat", 17.5, 3000)
Dog = Pet("dog", 20, 5000)
Fast_Bunny = Pet ("fast bunny", 50, 6000)
Fast_Rabbit = Pet("fast rabbit", 75, 20000)
Fast_Mole = Pet("fast mole", 100, 100000)
Fast_Fox = Pet("fast fox", 125, 150000)
Fast_Penguin = Pet("fast penguin", 150, 300000)
Fast_Cat = Pet("fast cat", 175, 500000)
Fast_Dog = Pet("fast dog", 200, 1000000)
Elephant = Pet("elephant", 50, 6000)
Leopard = Pet("leopard", 60, 8000)
Tiger = Pet("tiger", 70, 15000)
Alligator = Pet("alligator", 80, 60000)
Scorpion = Pet("scorpion", 90, 80000)
Rhinoceros = Pet("rhinoceros", 100, 100000)
Wasps = Pet("swarm of wasps", 25000, 10000000)
Elephants = Pet("herd of elephants", 500000, 20000000)
Leopards = Pet("leap of leopards", 6000000, 300000000)
Tigers = Pet("streak of tigers", 70000000, 4000000000)
Alligators = Pet("congregation of alligators", 800000000, 80000000000)
Scorpions = Pet("bed of scorpions", 90000000000, 3000000000000)
Rhinoceroses = Pet("crash of rhinoceroses", 10000000000000, 100000000000000000)
pets_list = [Wasp, Bunny, Rabbit, Mole, Fox, Penguin, Cat, Dog, Fast_Bunny, Fast_Rabbit, Fast_Mole, Fast_Fox, Fast_Dog, Elephant, Leopard, Tiger, Alligator, Scorpion, Rhinoceros, Wasps, Elephants, Leopards, Tigers, Alligators, Scorpions, Rhinoceroses]
My_pets = []
My_pets_equipped = []
while True:
    t.sleep(0.001)
    coins = coins + 1
    for item in My_pets:
        if item.active == True:
            coins = coins + item.multiplier - 1
        else:
            continue
    key = input("")
    if key.lower() == 's' or key.lower() == 'shop':
        for item in pets_list:
            print("Name: {0} , Multiplier: {1} , Cost: {2}".format(item.name, item.multiplier, item.cost))
    elif key.lower() == 'c' or key.lower() == 'coins':
        print(coins)
    elif key.lower() == 'b' or key.lower() == 'buy':
        answer = input("Please type the name of the pet you would like to buy: ")
        for item in pets_list:
            if item.name == answer.lower():
                if coins > item.cost:
                    item.buy
                    coins = coins - item.cost
                    My_pets.append(item)
                    print("Pet bought! Press 'e' to equip")
                else:
                    continue
            else:
                continue
    elif key.lower() == 'e' or key.lower() == 'equip':
        answer = input("Please type the name of the pet you would like to activate or have equipped: ")
        for item in My_pets:
            if item.name == answer.lower():
                item.active = True
                My_pets_equipped.append(item)
                print("All of that type of pet have been equipped!")
                break
            else:
                print("Finding pet...")
    elif key.lower() == 'p' or key.lower() == 'pets':
        for item in My_pets:
            print(item.name)
#            print(item)
    elif key.lower() == 'a' or key.lower() == 'activated':
        for item in My_pets:
            if item.active == True:
                print("{} is activated".format(item.name))
            else:
                print("{} not activated...".format(item.name))
        if len(My_pets) == 0:
            print("No pets activated or equipped.")
        else:
            continue
    elif key.lower() == 'i' or key.lower() == 'income':
        x = 0
        for item in My_pets:
            if item.active == True:
                x = x + item.multiplier
            else:
                print("A pet is not activated or equipped!")
        print("Current income: {}".format(x))
    else:
        print("Please type in something suitable!")





            