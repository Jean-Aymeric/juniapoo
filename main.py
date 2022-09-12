from random import randint

from Boxer import Boxer
from Human import Human
from Sock import Sock

jad = Human("Jean-Aymeric")
bob = Human("Bob")


jad.wear(Boxer(randint(0, 1000000)))
jad.wear(Sock(randint(0, 1000000)))
jad.wear(Sock(randint(0, 1000000)))
jad.show()
bob.show()