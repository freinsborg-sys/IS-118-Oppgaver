alder = 31
aldersgrense = 18
navn = "Michael"
antall_studenter = 30

# Jeg tror svaret blir: True
print(alder > aldersgrense)

# Jeg tror svaret blir: True
print(alder == 31)

# Jeg tror svaret blir: True
print(alder != aldersgrense)

# Jeg tror svaret blir: False
print(alder <= aldersgrense)

# Jeg tror svaret blir: True
print(navn == "Michael")

# Jeg tror svaret blir: False
print(navn == "michael")

# Jeg tror svaret blir: True
print(antall_studenter >= 30)

# Jeg tror svaret blir: True
print(alder + 5 > antall_studenter)

# Refleksjon til oppgave 5:
# Python skiller mellom store og små bokstaver. Derfor er "Michael" og "michael" to forskjellige tekstverdier.
# = brukes til å gi en variabel en verdi, mens == brukes til å sammenligne to verdier for å se om de er like.
# Python utfører først alder + 5, som blir 36. Deretter sammenlignes 36 med antall_studenter, som er 30. 
# True eller False er nyttige når et program skal ta valg basert på bestemte betingelser. For eksempel kan et program sjekke om en person er gammel nok til å kjøpe en vare.