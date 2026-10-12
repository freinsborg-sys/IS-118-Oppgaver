# Lager en variabel for aldersgrensen
aldersgrense = 18

# Spør brukeren om alderen. Bruker int for å gjøre om til heltall fordi input() alltid returnerer en streng.
alder = int(input("Hvor gammel er du? "))

# Test av program med alder 17,18 og 19. Tror 17 returnerer "ikke gammel nok", 18 returnerer "gammel nok" og 19 returnerer "gammel nok".
if alder >= aldersgrense:
    print(f"Du er {alder} år, og gammel nok.")
else:
    print(f"Du er {alder} år, og ikke gammel nok.")

# Fjernet innrykket foran den første print-linjen. Fikk IndentationError
# Fjernet kolonet etter if-linjen. Fikk SyntaxError

print("Takk for at du sjekket!")


# Utvidelse
# Byttet ut >= med > og testet med alderen 18. Fikk "ikke gammel nok" fordi 18 ikke er større enn 18. > betyr større enn, >= betyr større enn eller lik.


# --- Refleksjon ---
# Da jeg fjernet innrykket, fikk jeg en IndentationError. Da jeg fjernet kolonet, fikk jeg en SyntaxError. Innrykket forteller Python hvilken kode som tilhører if eller else, mens kolonet viser at en ny kodeblokk starter.
# Fordi linjen ikke har innrykk og ligger utenfor if og else. Python kjører den linjen uansett
# Uttrykket gir en boolsk verdi. Hvis resultatet er True, kjører Python koden under if. Hvis resultatet er False, kjører Python koden under else.
# >= er riktig fordi personer som er 18 år også skal være gamle nok. Det er lett å bruke > ved en feil og glemme at aldersgrensen også inkluderer personer som er nøyaktig 18 år.