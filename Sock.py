from Clothe import Clothe


class Sock(Clothe):
    def __init__(self, ref: int):
        Clothe.__init__(self, "Chaussette", ref)
