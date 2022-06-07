
from models.pajamu_irasas import PajamuIrasas
from models.islaidu_irasas import IslaiduIrasas
import pickle

def gauti_zurnala():
    try:
        with open("zurnalas.pkl", 'rb') as file:
            zurnalas = pickle.load(file)
    except:
        zurnalas = []
    return zurnalas


def irasyti_zurnala(zurnalas):
    try:
        with open("zurnalas.pkl", 'wb') as file:
            pickle.dump(zurnalas, file)
    except:
        print("Nepavyko įrašyti failo")


while True:
    zurnalas = gauti_zurnala()
    pasirinkimas = int(input("Pasirinkite:\n1 - įvesti pajamas\n2 - įvesti išlaidas\n3 - peržiūrėti visus įrašus\n4 - parodyti balansą\n5 - išeiti iš programos\n"))
    if pasirinkimas == 1:
        suma = float(input("Įveskite pajamų sumą"))
        info = input("Įveskite informaciją")
        moketojas = input("Įveskite moketoją")
        tipas = input("Įveskite tipą")
        irasas = PajamuIrasas(suma, info, moketojas, tipas)
        zurnalas.append(irasas)
        irasyti_zurnala(zurnalas)
    if pasirinkimas == 2:
        suma = float(input("Įveskite išlaidų sumą"))
        info = input("Įveskite informaciją")
        paskirtis = input("Įveskite paskirtį")
        pinigai = input("Įveskite pinigų tipą")
        irasas = IslaiduIrasas(suma, info, paskirtis, pinigai)
        zurnalas.append(irasas)
        irasyti_zurnala(zurnalas)
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