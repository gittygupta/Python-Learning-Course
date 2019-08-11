class Mario():
    def move(self):
        print('I am moving')

class Shroom():
    def eat_shroom(self):
        print('i am eating')

# All the functions get basically copied
class BigMario(Mario, Shroom):           # it can inherit from both the above classes, basically combines the above 2 into 1
    pass                                # this command just ends the class/function. Basically useless, just to skip syntax errors

bm = BigMario()
bm.move()
bm.eat_shroom()