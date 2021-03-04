#Miguel Rodriguez
#CSS 225
#Lab Activity 6

import random
import math


def ran():
    for side in range(10):
       print(random.randrange(25,35))

#ran()



def randomlist(m):
    return random.choice(m)
xlist = ["a",1,3,2.5,"Butts"]
#print(randomlist(xlist))





def rand():
    return random.randrange(1,100,2)
#print(rand())



def sqrt(a,b):
    c=math.sqrt(math.pow(a,2) + math.pow(b,2))
    return c
#print(sqrt(4,6))
