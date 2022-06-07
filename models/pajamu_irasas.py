from models.irasas import Irasas


class PajamuIrasas(Irasas):
    def __init__(self, suma, info, moketojas, tipas):
        super().__init__(suma, info)
        self.moketojas = moketojas
        self.tipas = tipas

    def __str__(self):
        return f"Pajamos: {self.suma}, info: {self.info}, mokėtojas: {self.moketojas}, tipas: {self.tipas}"
