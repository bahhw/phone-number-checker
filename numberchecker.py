# Phone Number Checker

import phonenumbers
from phonenumbers import carrier, geocoder

def numChecker(phoneNumber):
    info = []
    phone = phonenumbers.parse(phoneNumber)
    info.append(geocoder.description_for_number(phone,"es"))
    info.append(carrier.name_for_number(phone,"es"))
    return info

phoneNumber = input("Introduce un Numero de Telefono: ")
print(numChecker(phoneNumber))
