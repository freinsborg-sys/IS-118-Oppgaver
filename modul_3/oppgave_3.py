# Variabler

brus = 24.90
smørbrød = 45
banan = 8.50

# Lager nye variabler
totalsum = brus + smørbrød + banan
pris_per_person = totalsum / 4

# Printer ut totalsummen for alle tre varene, og totalsummen med moms.
print(totalsum, "er totalsummen for alle tre varene.")
print(totalsum * 1.25, "er totalsummen for alle tre varene inkludert moms.")
print(pris_per_person, "er prisen per person for alle tre varene.")

# Refleksjon til oppgave 3:
# Svaret ble en float fordi Python gir et desimaltall når vi legger sammen int og en float.
# Datatypen ble en float. Vanlig divisjon i Python gir et desimaltall, selv om svaret er et helt tall. Det var litt overraskende at Python alltid gjør dette ved vanlig divisjon.
# Det gjør koden enklere å lese og endre. Hvis prisen endrer seg, trenger jeg bare å endre verdien til varbiablene ett sted.