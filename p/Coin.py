import random

class Coin: 
    def __init(self, sideup = "Heads"):
        self.sideup_ = sideup
    def toss(self):
        if(random.randint(0, 1) == 1):
            self.sideup_ = "Heads"
        else:
            self.sideup_ = "Tails"
        return self.sideup_
    
class Bottle:
    def __init(self):
        self.type_ = "waterbottle"
        self.size_ = 0
    def get_type(self):
        return self.type_
    
    def size(self, n):
        self.size_ = n
        return self.size_
