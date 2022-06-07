from models.irasas import Irasas


class IslaiduIrasas(Irasas):
    def __init__(self, suma, info, paskirtis, pinigai="Kortele"):
        super().__init__(suma, info)
        self.paskirtis = paskirtis
        self.pinigai = pinigai

    def __str__(self):
        return f"Išlaidos: {self.suma} info: {self.info}, paskirtis: {self.paskirtis}, pinigai: {self.pinigai}"
