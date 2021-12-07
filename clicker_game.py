from clicker import Pet
import time as t
print("Hello, in this game, you get coins every second, and to get more coins, you need to buy more pets or multipliers. The pets are able to multiply your coins/second and the higher the multiplier of the pet, the more expensive it costs. The multipliers, multiply your total money outcome every second by a fixed amount, they cost money.")
print("To get to the shop, type 'shop'; to find out your earnings, type 'coins'; to buy pets, type 'buy pet', and then type the number when asked to.")
coins = 0
Wasp = Pet("Wasp", 2.5)
Bunny = Pet("Rabbit", 5)
Rabbit = Pet("Rabbit", 7.5)
Mole = Pet("Rabbit", 10)
Fox = Pet("Fox", 12.5)
Penguin = Pet("Penguin", 15)
Cat = Pet("Cat", 17.5)
Dog = Pet("Dog", 20)
Fast_Bunny = Pet ("Fast Bunny", 50)
Fast_Rabbit = Pet("Fast Rabbit", 75)
Fast_Mole = Pet("Fast Mole", 100)
Fast_Fox = Pet("Fast Fox", 125)
Fast_Penguin = Pet("Fast Penguin", 150)
Fast_Cat = Pet("Fast Cat", 175)
Fast_Dog = Pet("Fast Dog", 200)
Elephant = Pet("Elephant", 50)
Leopard = Pet("Leopard", 60)
Tiger = Pet("Tiger", 70)
Alligator = Pet("Alligator", 80)
Scorpion = Pet("Scorpion", 90)
Rhinoceros = Pet("Rhinoceros", 100)
Wasps = Pet("Swarm of Wasps", 2500)
Elephants = Pet("Herd of Elephants", 50000)
Leopards = Pet("Leap of Leopards", 60000)
Tigers = Pet("Streak of Tigers", 70000)
Alligators = Pet("Congregation of Alligator", 80000)
Scorpions = Pet("Bed of Scorpions", 90000)
Rhinoceroses = Pet("Crash of Rhinoceroses", 100000)
pets_list = (Wasp, Bunny, Rabbit, Mole, Fox, Penguin, Cat, Dog, Fast_Bunny, Fast_Rabbit, Fast_Mole, Fast_Fox, Fast_Dog, Elephant, Leopard, Tiger, Alligator, Scorpion, Rhinoceros, Wasps, Elephants, Leopards, Tigers, Alligators, Scorpions, Rhinoceroses)
#pets_dictionary = (1:Wasp, 2:Bunny, 3:Rabbit, 4:Mole, 5:Fox, 6:Penguin, 7:Cat, 8:Dog, 9:Fast_Bunny, 10:Fast_Rabbit, 11:Fast_Mole, 12:Fast_Fox, 13:Fast_Dog, 14:Elephant, 15:Leopard, 16:Tiger, 17:Alligator, 18:Scorpion, 19:Rhinoceros, 20:Wasps, 21:Elephants, 22:Leopards, 23:Tigers, 24:Alligators, 25:Scorpions, 26:Rhinoceroses)
while True:
    t.sleep(1)
    for pet in pets_list:
        if pet.active == True:
            coins = coins + 1 * pet.multiplier
        else:
            coin = coins + 1