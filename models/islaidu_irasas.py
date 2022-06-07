
from models.irasas import Irasas

class IslaiduIrasas(Irasas):
    def __str__(self):
        return f"Išlaidos: {self.suma}"
