from Organ import Organ


class Heart(Organ):
    def __init__(self, ref: int):
        Organ.__init__(self, "Coeur", ref)
