from clicker import Pet
import time as t
print("***********************************************************************************************")
print("Hello, in this game, you get coins every time you type.Your aim is to get the most coins, and you need to buy more pets or multipliers in order to do so. The pets are able to give you more coins: the higher the multiplier of the pet, the more coins you get, and the more expensive it costs. The multipliers multiply your total money outcome every second by a fixed amount, they cost money.")
print("To get to the shop, press 's'\nto find out your coins, press 'c'\nto see your pets, press 'p'\nto see activated/equipped pets, press 'a'\nto see income, press 'i'\nto buy pets, press 'b', and then type the name when asked to do so.")
coins = 0
pets_list = ["Wasp", "Bunny", "Rabbit", "Mole", "Fox", "Penguin", "Cat", "Dog", "Fast_Bunny", "Fast_Rabbit", "Fast_Mole", "Fast_Fox", "Fast_Cat", "Fast_Dog", "Elephant", "Leopard", "Tiger", "Alligator", "Scorpion", "Rhinoceros", "Wasps", "Elephants", "Leopards", "Tigers", "Alligators", "Scorpions", "Rhinoceroses"]
for item in pets_list:
    print("{}_list = []".format(item))
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
pet_stats = [Wasp, Bunny, Rabbit, Mole, Fox, Penguin, Cat, Dog, Fast_Bunny, Fast_Rabbit, Fast_Mole, Fast_Fox, Fast_Dog, Elephant, Leopard, Tiger, Alligator, Scorpion, Rhinoceros, Wasps, Elephants, Leopards, Tigers, Alligators, Scorpions, Rhinoceroses]


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
    coins =+ 1
    Input = input("")
    if Input.lower() == 'b' or Input.lower() == 'buy':
        Input = input("Please type the name of the pet you would like to buy: ")
        number_of_pets = input("Please type in the number of that pet which you would like to buy: ")
        x = int(number_of_pets)
        for item in pets_list:
            if Input.lower() == item.lower():
                    while x > 0:
                        if pets_list.index(item) == 0 and coins >= Wasp.cost:
                            pet = Wasp("pet")
                            Wasp_list.append(pet)
                            x = x - 1
                        elif pets_list.index(item) == 1 and coins >= Bunny.cost:
                            pet = Bunny("pet")
                            Bunny_list.append(pet)
                            x = x - 1                       
                        elif pets_list.index(item) == 2 and coins >= Rabbit.cost:
                            pet = Rabbit("pet")
                            Rabbit_list.append(pet)
                            x = x - 1                                              
                        elif pets_list.index(item) == 3 and coins >= Mole.cost:
                            pet = Mole("pet")
                            Mole_list.append(pet)
                            x = x - 1                       
                        elif pets_list.index(item) == 4 and coins >= Fox.cost:
                            pet = Fox("pet")
                            Fox_list.append(pet)
                            x = x - 1                       
                        elif pets_list.index(item) == 5 and coins >= Penguin.cost:
                            pet = Penguin("pet")
                            Penguin_list.append(pet)
                            x = x - 1                      
                        elif pets_list.index(item) == 6 and coins >= Cat.cost:
                            pet = Cat("pet")
                            Cat_list.append(pet)
                            x = x - 1
                        elif pets_list.index(item) == 7 and coins >= Dog.cost:
                            pet = Dog("pet")
                            Dog_list.append(pet)
                            x = x - 1                       
                        elif pets_list.index(item) == 8 and coins >= Fast_Bunny.cost:
                            pet = Fast_Bunny("pet")
                            Fast_Bunny_list.append(pet)
                            x = x - 1                       
                        elif pets_list.index(item) == 9 and coins >= Fast_Rabbit.cost:
                            pet = Fast_Rabbit("pet")
                            Fast_Rabbit_list.append(pet)
                            x = x - 1                       
                        elif pets_list.index(item) == 10 and coins >= Fast_Mole.cost:
                            pet = Fast_Mole("pet")
                            Fast_Mole_list.append(pet)
                            x = x - 1                       
                        elif pets_list.index(item) == 11 and coins >= Fast_Fox.cost:
                            pet = Fast_Fox("pet")
                            Fast_Fox_list.append(pet)
                            x = x - 1                       
                        elif pets_list.index(item) == 12 and coins >= Fast_Cat.cost:
                            pet = Fast_Cat("pet")
                            Fast_Cat_list.append(pet)
                            x = x - 1                       
                        elif pets_list.index(item) == 13 and coins >= Fast_Dog.cost:
                            pet = Fast_Dog("pet")
                            Fast_Dog_list.append(pet)
                            x = x - 1                       
                        elif pets_list.index(item) == 14 and coins >= Elephant.cost:
                            pet = Elephant("pet")
                            Elephant_list.append(pet)
                            x = x - 1                       
                        elif pets_list.index(item) == 15 and coins >= Leopard.cost:
                            pet = Leopard("pet")
                            Leopard_list.append(pet)
                            x = x - 1            
                        elif pets_list.index(item) == 16 and coins >= Tiger.cost:
                            pet = Tiger("pet")
                            Tiger_list.append(pet)
                            x = x - 1
                        elif pets_list.index(item) == 17 and coins >= Alligator.cost:
                            pet = Alligator("pet")
                            Alligator_list.append(pet)
                            x = x - 1
                        elif pets_list.index(item) == 18 and coins >= Scorpion.cost:
                            pet = Scorpion("pet")
                            Scorpion_list.append(pet)
                            x = x - 1
                        elif pets_list.index(item) == 19 and coins >= Rhinoceros.cost:
                            pet = Rhinoceros("pet")
                            Rhinoceros_list.append(pet)
                            x = x - 1
                        elif pets_list.index(item) == 20 and coins >= Wasps.cost:
                            pet = Wasps("pet")
                            Wasps_list.append(pet)
                            x = x - 1
                        elif pets_list.index(item) == 21 and coins >= Elephants.cost:
                            pet = Elephants("pet")
                            Elephants_list.append(pet)
                            x = x - 1
                        elif pets_list.index(item) == 22 and coins >= Leopards.cost:
                            pet = Leopards("pet")
                            Leopards_list.append(pet)
                            x = x - 1
                        elif pets_list.index(item) == 23 and coins >= Tigers.cost:
                            pet = Tigers("pet")
                            Tigers.append(pet)
                            x = x - 1
                        elif pets_list.index(item) == 24 and coins >= Alligators.cost:
                            pet = Alligators(pet)
                            Alligators_list.append(pet)
                            x = x - 1
                        elif pets_list.index(item) == 25 and coins >= Scorpions.cost:
                            pet = Scorpions("pet")
                            Scorpions_list.append(pet)
                            x = x - 1
                        elif pets_list.index(item) == 26 and coins >= Rhinoceroses.cost:
                            pet = Rhinoceroses("pet")
                            Rhinoceroses_list.append(pet)
                            x = x - 1
                        else:
                            print("ERROR")
            else:
                print("ERROR")
    elif Input == 's' or Input == 'shop':
        print(pet_stats)
                
    elif Input.lower() == 'c' or Input.lower() == 'coins':
        print(coins)
    else:
        print("Please type in something suitable.")