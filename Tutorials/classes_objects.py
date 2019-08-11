# Enemy attack game

class Enemy:
    life = 3

    def attack(self):
        print("Enemy says - Ouch !!")
        self.life -= 1          # to access variables inside the class itself

    def checklife(self):
        if self.life <= 0:
            print("Enemy says - I'm dead")
        else:
            print(str(self.life) + " life left")

# now to access anything that's inside this class, we need to create an object

enemy1 = Enemy()        # Object initialisation
#objects are basically the copies of a class
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()                    # basically the functions on enemy 1 doesnt affect enemy 2
enemy1.checklife()

enemy2.checklife()

# so by writing just once, we can create 2 instances to run the class twice 'parallelly and independently'

