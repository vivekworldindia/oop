class Vault:
    def __init__(self,galleons=0,sickles=0,khuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.khuts = khuts
        
    def __str__(self):
        return f"{self.galleons} Galleons,{self.sickles} Sickles,{self.khuts} Khuts"
    
    def __add__(self,other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        khuts = self.khuts + other.khuts
        return Vault(galleons,sickles,khuts)
        
        
potter = Vault(100,50,25)
weasley = Vault(25,30,90)

total = potter + weasley
print(total)