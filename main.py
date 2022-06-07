
from models.pajamu_irasas import PajamuIrasas
from models.islaidu_irasas import IslaiduIrasas

zurnalas = []


while True:
    pasirinkimas = int(input("Pasirinkite:\n1 - įvesti pajamas\n2 - įvesti išlaidas\n3 - peržiūrėti visus įrašus\n4 - parodyti balansą\n5 - išeiti iš programos\n"))
    if pasirinkimas == 1:
        suma = float(input("Įveskite pajamų sumą"))
        irasas = PajamuIrasas(suma)
        zurnalas.append(irasas)
    if pasirinkimas == 2:
        suma = float(input("Įveskite išlaidų sumą"))
        irasas = IslaiduIrasas(suma)
        zurnalas.append(irasas)
    if pasirinkimas == 3:
        for irasas in zurnalas:
            print(irasas)
    if pasirinkimas == 4:
        suma = 0
        for irasas in zurnalas:
            if type(irasas) is PajamuIrasas:
                suma += irasas.suma
            if type(irasas) is IslaiduIrasas:
                suma -= irasas.suma
        print("Balansas:", suma)
    if pasirinkimas == 5:
        print("Viso gero")
        break