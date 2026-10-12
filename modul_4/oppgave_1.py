# 1
navn = input("Hva heter du? ")

# 2
print("Hei,", navn)

# 3
print(f"Hei, {navn}!")

# 4
alder = input("Hvor gammel er du? ")

# 5
print(type(alder))

# 6
alder = int(alder)

# 7
print(type(alder))

# 8
print(f"Neste år blir du {alder + 1} år!")


# Utvidelse
høyde = input("Hvor høy er du i meter? ")
høyde = float(høyde)
print(f"Du er {høyde} meter høy!")


# --- Refleksjon ---
# Python svarte "str". Det er fordi input alltid leser det som skrives inn som tekst selv om det er et tall.
# Python ga "TypeError" fordi jeg prøvde å legge sammen teskt og et heltall. Jeg måtte gjøre om alderen til "int".
# Jeg syntes f-strengen er lettest å lese fordi jeg kan sette varbiabelen direkte inn i teksten. Vanlig print() og komma legger python automatisk inn et mellomrom. Med f-strenger kan ejg skrive mellomrom hvor jeg vil ha dem.
# Får nok en "ValueError". Er fordi int(alder) ikke klarer å gjøre om ordet "tretti" til heltall.