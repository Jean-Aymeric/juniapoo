from random import randint

from Clothe import Clothe
from Heart import Heart
from Lung import Lung
from Organ import Organ


class Human:
    __organs: [Organ]
    __clothes: [Clothe]
    __name: str

    def __init__(self, name: str):
        self.__name = name
        self.__organs = []
        self.__clothes = []
        self.__organs.append(Heart(randint(0, 1000000)))
        self.__organs.append(Lung(randint(0, 1000000)))
        self.__organs.append(Lung(randint(0, 1000000)))

    def showOrgans(self):
        for i in range(len(self.__organs)):
            print("\t",self.__organs[i].getName() + "(" + str(self.__organs[i].getRef()) + ")")
        for i in range(len(self.__clothes)):
            print("\t",self.__clothes[i].getName() + "(" + str(self.__clothes[i].getRef()) + ")")

    def show(self):
        print (self.getName(), ":")
        self.showOrgans()

    def getName(self) -> str:
        return self.__name

    def wear(self, clothe: Clothe):
        self.__clothes.append(clothe)