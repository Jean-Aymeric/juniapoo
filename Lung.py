from Organ import Organ


class Lung(Organ):
    def __init__(self, ref: int):
        Organ.__init__(self, "Poumon", ref)
