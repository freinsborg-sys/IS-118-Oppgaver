# Lager fem forskjellige variabler. En av hver datatype
navn = "Fredrik"
alder = 24
høyde = 1.82
er_student = "ja"
hobbyer = ["styrkeløft", "dataspill", "sykling"]

print("Navn:", navn)
print("Alder:", alder)
print("Høyde:", høyde)
print("Student:", er_student)
print("Hobbyer:", hobbyer)

# Skriver ut i motsatt rekkefølge
print("Hobbyer:", hobbyer[::-1])
print("Student:", er_student)
print("Høyde:", høyde)
print("Alder:", alder)
print("Navn:", navn)

# Legger til typeen til hver variabel
print(type(navn))
print(type(alder))
print(type(høyde))
print(type(er_student))
print(type(hobbyer))

# Refleksjon til oppgave 1:
# Nei, jeg trengte ikke å flytte på variablene. Jeg trenger kun å endre rekkefølgen på print-funksjonenene. Python skriver ut informasjonen i riktig rekkefølge print-funksjonene står i.
# Ja, det stemte med datatypene vi har lært om i forelesningen.
# Python må vite datatypen for å forstå hvordan verdien skal behandles. Python kan regne med tall, mens tekst behandles annerledes. Datatypen bestemmer hvile operasjoner som kan utføres på variablen.