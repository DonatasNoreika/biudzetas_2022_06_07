from models.irasas import Irasas


class PajamuIrasas(Irasas):
    def __str__(self):
        return f"Pajamos: {self.suma}"
