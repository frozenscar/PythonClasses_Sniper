class sniper(object):
    def __init__(self,shootRange,power,bullets):
        self.shootRange = shootRange
        self.power = power
        self.bullets = bullets
    def shoot(self):
        if (self.bullets>0):
            self.bullets -=1
        else :print("out of ammo!")
        
        


M24 = sniper(600,85,7)
Kar98k = sniper(900,70,5)
print(M24.shootRange,M24.bullets)
M24.shoot()
M24.shoot()
print(M24.shootRange,M24.bullets)
print(Kar98k.shootRange)