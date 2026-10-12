# Variabel for hovedstaden i Norge

riktig_svar = "Oslo"

svar = input("Hva er hovedstaden i Norge? ")

# Bruker ==. = gir en verdi, mens == sammenligner
# : må stå på slutten av if statementen. : markerer starten på kodeblokken. 
if svar == riktig_svar:
    print("Riktig!")

# else kjøres hvis svaret ikke stemmer. print må ha innrykk for å tilhøre else
else:
    print("Feil, svaret var", riktig_svar)

# Input() gir en string. Må bruke int() gjør om svaret fra tekst til heltall.
alder = int(input("Hvor gammel er du? "))

if alder == 18:
    print("Du er akkurat myndig!")
else:
    print("Du er ikke 18.")

# Hvis jeg kjører med 18 som alder får jeg at "Du er ikke 18". Det er fordi input() gir en string. Må bruke int() for å gjøre om til heltall.
# "18" som string vil gi False siden det ikke er "likt" 18 som en int. 
# Testet programmet med 18 etter fire feilrettinger. Det kjører som det skal.



# --- Refleksjon ---
# Fant toalt fire feil. Var brukt = i stedet for ==. = ga en verdi.
# Manglet kolon etter if. Koden kjører da ikke resten av kjeden.
# Den ene print() linjen manglet innrykk. Ble derfor ikke tatt med i kjeden.
# Siste feilen jeg fant var at alderen ikke ble gjort om til et heltall.
# Fant den fordi jeg har lært at input() gir string verdi. Python klager ikke fordi det er lov å sammenligne tekst med tall selvom det gir False.
# En syntaksfeil gjør at programmet ikke kan kjøre. En logisk feil gjør at programmet kjører, men gir feil resultat. Jeg tror logiske feil er farligere fordi de kan være vanskeligere å oppdage.
# Jeg ville testet med både riktige og feil svar, for eksempel Oslo, Bergen og oslo. For alder ville jeg testet 17, 18 og 19 for å se om programmet gir riktig resultat.