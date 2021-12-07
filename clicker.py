class Pet:

    def __init__(self, name, multiplier):
        self.name = name
        self.active = False
        self.owned = False
        self.multiplier = multiplier
            
    def buy(self):
        self.owned = True
        
    def use_pet(self):
        if self.owned:
            self.active = True
        else:
            print("This pet is not owned.")
            
            