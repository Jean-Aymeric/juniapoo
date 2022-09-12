class Clothe:
    __name: str
    __ref:int

    def __init__(self, name: str, ref: int):
        self.__name = name
        self.__ref = ref

    def getName(self) -> str:
        return self.__name

    def getRef(self) -> int:
        return self.__ref
