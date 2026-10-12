# Ber brukeren skrive inn antall poeng fra 0-100.
poeng = int(input("Hvor mange poeng fikk du (0-100)? "))

# if/elif/else-kjede som rkiver ut riktig karakter basert på poengsummen. A-F

# Hvis poengsummen er mindre enn 0 eller større enn 100, gis det feilmelding.
if poeng < 0 or poeng > 100:
    print("Ugyldig poengsum. Skriv inn et tall mellom 0 og 100.")
# Hvis poengsummen er gyldig, sjekkes kjeden videre.
elif poeng >= 90:
    print("Karakter: A")
elif poeng >= 80:
    print("Karakter: B")

elif poeng >= 80:
    print("Karakter: B")

elif poeng >= 60:
    print("Karakter: C")

elif poeng >= 50:
    print("Karakter: D")

elif poeng >= 40:
    print("Karakter: E")

else:
    print("Karakter: F")

# Tror 95 gir A, 72 gir C, 40 gir E og 12 gir F.
# Tester programmet med 95,72,40 og 12. Det var som forventet. 

# Snudde rekkefølgen til A-E. Da tror jeg 95 vil gi E fordi den sjekkes først. Vil gi True siden 95 er større enn 40. 

# Byttet ut elif med if, programmet skrev ut A,B,C,D,E. 

# Utvidelse:
# Skrives 150 eller -10 gis det feilmelding. Lagt inn en sjekker som gir en feilmelding hvis tallet er mindre enn 0 eller større enn 100.
#Sjekkeren må stå først som if, eller så vil ikke resten av kjeden kjøre.

# --- Refleksjon ---
# 95 poeng ga karakter E fordi porgrammet sjekket om poengene var 40 eller høyere først. Siden det var True, hoppet python over resten av kjeden.
# Skrev vel ut flere karakterer siden if ble sjekket alene, alle sammen var sanne. Pythons toppet ikke opp på første. Hvis if og elif brukes stopper python ved første true.
# Fordi python allerede har sjekka om poengene er høyere enn 90 eller lik 90. Den hopper videre siden python da vet at den er lavere enn 90.
# Else kjøres vel til slutt hvis ingen av if eller elif er True. I denne oppgaven kjøres den når brukeren skriver inn 0-39. De andre verdiene er allerede sjekket og ga false.