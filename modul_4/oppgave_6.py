# To variabler for rikgit brukernavn og passord

riktig_brukernavn = "michael"
riktig_passord = "python123"

# Brukeren skal skrive inn brukernavn og passord
brukernavn = input("Skriv inn brukernavn: ")
passord = input("Skriv inn passord: ")

# Legger til alderssjekk. Legges først fordi en under 13 med riktig info vil bli logget inn fordi python stopper ved den første True.
alder = int(input("Hvor gammel er du? "))

# Sjekker om både brukernavn og passord stemmer
if brukernavn == riktig_brukernavn and passord == riktig_passord and alder < 13:
    print(f"Velkommen, {brukernavn}!")

# Hvis brukernavnet stemmer, men passordet er feil.
elif brukernavn == riktig_brukernavn and passord != riktig_passord:
    print("Feil passord.")

# Else kjøres hvis brukernavnet er feil.
else:
    print("Ukjent bruker.")

# Test av alle fire kombinasjonene
# michael / python vil gi Velkommen, michael!
# michael / feil123 vil gi Feil passord.
# fredrik / python123 vil gi Ukjent bruker.
# fredrik / feil123 vil gi Ukjent bruker.


# --- Refleksjon ---
# Jeg brukte if, elif og else, med and. Brukte det for å sjekke om begge sider var True. Oppgaven kan også løses med if statements.
# Jeg sjekka først om brukernavn og passord var riktig. Så sjekka jeg om bare brukernavnet var riktig.
# Hvis jeg sjekker brukernavnet først kan scriptet gi feil resultat siden python stopper ved første True i en if/elif-kjede.
# Det er for å gjøre innlogginga tryggere. Fult mulig å gjette pasord med riktig brukernavn hvis nettsiden sier det. 
# Lurt å sjekke alle kombinasjonene for å kontrollere at det gis riktig beskjed ved alle sjekkene. 
# Kan være andre feil hvis man bare sjekker med brukernavn og passord som er riktig.