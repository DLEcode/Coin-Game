from clicker import *
import time as t
print("*"*30)
print("Hello, in this game you get coins every time you type.")
print("Your aim is to get the most coins, so type as much as possible!")
print("For example: if you type the word 'coins' you will be able to see your amount of coins, AND you will get 1 coin for typing")
print("However, 1 coin per 'type' is not enough! Your goal is to collect the most coins!")
print("\n")
print("*"*30)
print("\n")
print("""To get more coins, you can buy pets:
      Pets are able to give you more coins: 
      the higher the extra-coins of the pet, 
      the more additional coins you will recieve per 'type'""")
print("""However, the higher the additional coins of the pet, the more it costs!
      For example, a Wasp pet costs 10 coins, 
      and increases your total coin per 'type' income by 2.5,
      whereas the Crash of Rhinoceroses pets cost 100000000000000000, 
      and increases your total coins per 'type' income by 10000000000000.""")
print("\n")
print("*"*30)
print("\n")
print("""Here is a list of commands you will need to know to play the game
      To get to the shop: press 'S' or type 'Shop'
      To find out your coins: press 'C' or type 'Coins'
      To see your pets: press 'P' or type 'Pets'
      To see activated/equipped pets: press 'A' or type 'Activated'
      To see income: press 'I' or type 'Income
      To equip a pet: press 'E' or type 'Equip'
      To buy pets: press 'B' or type 'Buy', 
      and then type the name of the pet, 
      and then the number of that pet which you would like to buy.""")
print("\n")
print("*"*30)
print("\n")
print("""First, start typing anything. Everytime you type something and press enter, 
      you get a coin (with the additional coins from pets).
      So type away! You do not have to type commands, it can be totally random: 
      you can get a coin(s) for typing 'cheese'.
      After you have at least 10 coins, open the shop and see what you can buy!
      Then buy a pet and equip it using the given commands.
      Then check if the pet is activated, and carry on typing!
      As your coins per 'type' income gets higher, 
      you will be able to afford more pets, and will become rich!
      See if you can get enough coins to buy the Crash of Rhinoceroses pets!""")
print("\n")
print("*"*30)
print("""Note: currently the 'equip' command is only working for pet Wasp
      Note: currently the 'pets' command is not working as wanted""")

coins = 0
pets_list = ["Wasp", "Bunny", "Rabbit", "Mole", "Fox", "Penguin", "Cat",\
             "Dog", "Fast_Bunny", "Fast_Rabbit", "Fast_Mole", "Fast_Fox",\
                 "Fast_Cat", "Fast_Dog", "Elephant", "Leopard", "Tiger", \
                     "Alligator", "Scorpion", "Rhinoceros", "Wasps", \
                         "Elephants", "Leopards", "Tigers", "Alligators", \
                             "Scorpions", "Rhinoceroses"]
#for item in pets_list:
#    print("{}_list".format(item))
coins = 0
Wasp = Pet("wasp", 2.5, 10)
Bunny = Pet("bunny", 5, 60)
Rabbit = Pet("rabbit", 7.5, 100)
Mole = Pet("mole", 10, 1000)
Fox = Pet("fox", 12.5, 1500)                 #this list is for a 'reference' for price and multiplier
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
pet_stats = [Wasp, Bunny, Rabbit, Mole, Fox, Penguin, Cat, Dog, Fast_Bunny, Fast_Rabbit, Fast_Mole, Fast_Fox, Fast_Dog, Elephant, Leopard, Tiger, Alligator, Scorpion, Rhinoceros, Wasps, Elephants, Leopards, Tigers, Alligators, Scorpions, Rhinoceroses]

total_list = []
equipped_pets = []

Wasp_list = []
Bunny_list = []
Rabbit_list = []
Mole_list = []
Fox_list = []
Penguin_list = []
Cat_list = []
Dog_list = []
Fast_Bunny_list = []
Fast_Rabbit_list = []
Fast_Mole_list = []
Fast_Fox_list = []
Fast_Cat_list = []
Fast_Dog_list = []
Elephant_list = []
Leopard_list = []
Tiger_list = []
Alligator_list = []
Scorpion_list = []
Rhinoceros_list = []
Wasps_list = []
Elephants_list = []
Leopards_list = []
Tigers_list = []
Alligators_list = []
Scorpions_list = []
Rhinoceroses_list = []

while True:
    coins = coins + 1
    Input = input("")
    if Input.lower() == 'b' or Input.lower() == 'buy':
        Input = input("Please type the name of the pet you would like to buy: ")
        number_of_pets = input("Please type in the number of that pet which you would like to buy: ")
        x = int(number_of_pets)
        for item in pets_list:
            if Input.lower() == item.lower():
                    while x > 0 and coins >= 0:
                        if pets_list.index(item) == 0 and coins >= Wasp.cost:
                            pet = Wasp_("Wasp")
                            Wasp_list.append(pet)
                            total_list.append(pet)
                            x = x - 1
                            coins = coins - Wasp.cost   #using as reference for cost
                            print("Pet bought!")
                        elif pets_list.index(item) == 1 and coins >= Bunny.cost:
                            pet = Bunny_("Bunny")
                            Bunny_list.append(pet)
                            total_list.append(pet)
                            x = x - 1     
                            coins = coins - Bunny.cost
                        elif pets_list.index(item) == 2 and coins >= Rabbit.cost:
                            pet = Rabbit_("Rabbit")
                            Rabbit_list.append(pet)
                            total_list.append(pet)
                            x = x - 1     
                            coins = coins - Rabbit.cost                                         
                        elif pets_list.index(item) == 3 and coins >= Mole.cost:
                            pet = Mole_("Mole")
                            Mole_list.append(pet)
                            total_list.append(pet)
                            x = x - 1              
                            coins = coins - Mole.cost 
                        elif pets_list.index(item) == 4 and coins >= Fox.cost:
                            pet = Fox_("Fox")
                            Fox_list.append(pet)
                            total_list.append(pet)
                            x = x - 1               
                            coins = coins - Penguin.cost 
                        elif pets_list.index(item) == 5 and coins >= Penguin.cost:
                            pet = Penguin_("Penguin")
                            Penguin_list.append(pet)
                            total_list.append(pet)
                            x = x - 1                      
                            coins = coins - Penguin.cost 
                        elif pets_list.index(item) == 6 and coins >= Cat.cost:
                            pet = Cat_("Cat")
                            Cat_list.append(pet)
                            total_list.append(pet)
                            x = x - 1
                            coins = coins - Cat.cost 
                        elif pets_list.index(item) == 7 and coins >= Dog.cost:
                            pet = Dog_("Dog")
                            Dog_list.append(pet)
                            total_list.append(pet)
                            x = x - 1                       
                            coins = coins - Dog.cost 
                        elif pets_list.index(item) == 8 and coins >= Fast_Bunny.cost:
                            pet = Fast_Bunny_("Fast Bunny")
                            Fast_Bunny_list.append(pet)
                            total_list.append(pet)
                            x = x - 1                       
                            coins = coins - Fast_Bunny.cost 
                        elif pets_list.index(item) == 9 and coins >= Fast_Rabbit.cost:
                            pet = Fast_Rabbit_("Fast Rabbit")
                            Fast_Rabbit_list.append(pet)
                            total_list.append(pet)
                            x = x - 1             
                            coins = coins - Fast_Rabbit.cost 
                        elif pets_list.index(item) == 10 and coins >= Fast_Mole.cost:
                            pet = Fast_Mole_("Fast Mole")
                            Fast_Mole_list.append(pet)
                            total_list.append(pet)
                            x = x - 1                       
                            coins = coins - Fast_Mole.cost 
                        elif pets_list.index(item) == 11 and coins >= Fast_Fox.cost:
                            pet = Fast_Fox_("Fast Fox")
                            Fast_Fox_list.append(pet)
                            total_list.append(pet)
                            x = x - 1                       
                            coins = coins - Fast_Fox.cost 
                        elif pets_list.index(item) == 12 and coins >= Fast_Cat.cost:
                            pet = Fast_Cat_("Fast Cat")
                            Fast_Cat_list.append(pet)
                            total_list.append(pet)
                            x = x - 1                       
                            coins = coins - Fast_Cat.cost 
                        elif pets_list.index(item) == 13 and coins >= Fast_Dog.cost:
                            pet = Fast_Dog_("Fast Dog")
                            Fast_Dog_list.append(pet)
                            total_list.append(pet)
                            x = x - 1                       
                            coins = coins - Fast_Dog.cost 
                        elif pets_list.index(item) == 14 and coins >= Elephant.cost:
                            pet = Elephant_("Elephant")
                            Elephant_list.append(pet)
                            total_list.append(pet)
                            x = x - 1                       
                            coins = coins - Elephant.cost 
                        elif pets_list.index(item) == 15 and coins >= Leopard.cost:
                            pet = Leopard_("Leopard")
                            Leopard_list.append(pet)
                            total_list.append(pet)
                            x = x - 1            
                            coins = coins - Leopard.cost 
                        elif pets_list.index(item) == 16 and coins >= Tiger.cost:
                            pet = Tiger_("Tiger")
                            Tiger_list.append(pet)
                            total_list.append(pet)
                            x = x - 1
                            coins = coins - Tiger.cost 
                        elif pets_list.index(item) == 17 and coins >= Alligator.cost:
                            pet = Alligator_("Alligator")
                            Alligator_list.append(pet)
                            total_list.append(pet)
                            x = x - 1
                            coins = coins - Alligator.cost 
                        elif pets_list.index(item) == 18 and coins >= Scorpion.cost:
                            pet = Scorpion_object("Scorpion")
                            Scorpion_list.append(pet)
                            total_list.append(pet)
                            x = x - 1
                            coins = coins - Scorpion.cost 
                        elif pets_list.index(item) == 19 and coins >= Rhinoceros.cost:
                            pet = Rhinoceros_("Rhinoceros")
                            Rhinoceros_list.append(pet)
                            total_list.append(pet)
                            x = x - 1
                            coins = coins - Rhinoceros.cost 
                        elif pets_list.index(item) == 20 and coins >= Wasps.cost:
                            pet = Wasps_("Swarm of Wasps")
                            Wasps_list.append(pet)
                            total_list.append(pet)
                            x = x - 1
                            coins = coins - Wasps.cost 
                        elif pets_list.index(item) == 21 and coins >= Elephants.cost:
                            pet = Elephants_("Herd of Elephants")
                            Elephants_list.append(pet)
                            total_list.append(pet)
                            x = x - 1
                            coins = coins - Elephants.cost 
                        elif pets_list.index(item) == 22 and coins >= Leopards.cost:
                            pet = Leopards_("Leap of Leopards")
                            Leopards_list.append(pet)
                            total_list.append(pet)
                            x = x - 1
                            coins = coins - Leopards.cost 
                        elif pets_list.index(item) == 23 and coins >= Tigers.cost:
                            pet = Tigers_("Streak of Tigers")
                            Tigers.append(pet)
                            total_list.append(pet)
                            x = x - 1
                            coins = coins - Tigers.cost 
                        elif pets_list.index(item) == 24 and coins >= Alligators.cost:
                            pet = Alligators_("Congregation of Alligators")
                            Alligators_list.append(pet)
                            total_list.append(pet)
                            x = x - 1
                            coins = coins - Alligators.cost 
                        elif pets_list.index(item) == 25 and coins >= Scorpions.cost:
                            pet = Scorpions_("Bed of Scorpions")
                            Scorpions_list.append(pet)
                            total_list.append(pet)
                            x = x - 1
                            coins = coins - Scorpions.cost 
                        elif pets_list.index(item) == 26 and coins >= Rhinoceroses.cost:
                            pet = Rhinoceroses_("Crash of Rhinoceroses")
                            Rhinoceroses_list.append(pet)
                            total_list.append(pet)
                            x = x - 1
                            coins = coins - Rhinoceroses.cost 
                        else:
                            print("ERROR...")
                            print("Perhaps you do not have enough coins.")
            else:
                continue
    elif Input.lower() == 's' or Input.lower() == 'shop':
        print(pet_stats)

    elif Input.lower() == 'c' or Input.lower() == 'coins':
        print(coins)
    elif Input.lower() == 'i' or Input.lower() == 'income':
        x = 0
        for item in equipped_pets:
            x = x + item.extra-coins
            print(x)
    elif Input.lower() == 'p' or Input.lower() == 'pets':
        print(Wasp_list, Bunny_list, Rabbit_list, Mole_list, Fox_list, Penguin_list, Cat_list, Dog_list, Fast_Bunny_list, Fast_Rabbit_list, Fast_Mole_list, Fast_Fox_list, Fast_Cat_list, Fast_Dog_list, Elephant_list, Leopard_list, Tiger_list, Alligator_list, Scorpion_list, Rhinoceros_list, Wasps_list, Elephants_list, Leopards_list, Tigers_list, Alligators_list, Scorpions_list, Rhinoceroses_list)
    elif Input.lower() == 'e' or Input.lower == 'equip':
        Input = input("Please type in the name of the pet you would like to equip: ")
        number_of_pets = input("Please type in the number of that pet you would like to equip: ")
        x = int(number_of_pets)
        for item in total_list:
            while x > 0:
                if Input.lower() == "wasp":
                    for item in Wasp_list:
                        item.active = True
                        print("Wasp is equipped!")
                        equipped_pets.append(item)
                        x = x - 1
                else:
                    continue
    elif Input.lower() == 'a' or Input.lower() == 'activated':
        for item in equipped_pets:
            print(item.name)
    else:
        print("Type type type!")