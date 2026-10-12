poeng = 0

# Jeg tror poeng blir: 10
poeng = poeng + 10
print(poeng)

# Jeg tror poeng blir: 35
poeng += 25
print(poeng)

# Jeg tror poeng blir: 30
poeng -= 5
print(poeng)

# Jeg tror poeng blir: 60
poeng *= 2
print(poeng)

# Jeg tror poeng blir: 15
poeng /= 4
print(poeng)

# Refleksjon til oppgave 4:
# Alle forutsigelsene mine stemte. Jeg fikk resultatene jeg forventet etter hver utregning.
# Datatypen endret seg fra int til float. Dette skjedde fordi jeg brukte divisjon (/), som alltid gir et desimaltall i Python.
# Ja, begge ga samme resultat. += gjør koden kortere og enklere å lese. Man slipper å skrive variabelnavnet to ganger.