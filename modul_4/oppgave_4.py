# # Del 1:

# # Tre variabler med alder og student-/medlemsstatus
# alder = 25
# er_student = True
# har_medlemskort = False

# #Tror svaret blir False siden alderen er verken under 12 eller over 67.
# print(alder < 12 or alder > 67)

# # Tror svaret blir True siden begge påstandene er sanne. "and" er bare sann hvis begge sidene er sanne. Det er dem her.
# print(er_student and alder < 30)

# # Tror svaret blir True siden "not" snur False til True.
# print(not har_medlemskort)

# # Tror svaret blir False siden "and" krever at begge sidene er sanne. har_medlemskort er ikke sann.
# print(er_student and har_medlemskort)

# # Tror svaret blir True. "or" trenger at minst en av sidene er sanne. er_student er sann her.
# print(er_student or har_medlemskort)

# # Tror svaret blir True siden "not er_student" blir til False, mens alderen er mindre enn 30, det er True. "or" trenger at minst en av sidene er sanne.
# print(not er_student or alder < 30)

# # Del 2:

# Ber brukeren skrive inn alder, int() gjør om til heltall siden input() vil gi en string
alder = int(input("Hvor gammel er du? "))

# Spør om brukeren er student eller ikke. "==" gir true eller false. hvis svaret er "ja" blir variabelen True. Noe annet vil gi False
er_student = input("Er du student? (ja/nei) ").lower() == "ja"

# Barn under 12 eller personer over 67 får gratis billett. "or" vil si at minst en av sidene er True.
if alder < 12 or alder > 67:
    pris = 0

# Studenter under 30 får billett til 50 kr. "and" da må begge sidene være True.
elif er_student and alder < 30:
    pris = 50

# Alle andre må betale full pris
else:
    pris = 120

# Skriver ut prisen med en f-streng
print(f"Billetten koster {pris} kr.")

# Gir et tips dersom brukeren ikke er student. "not" snur verdien til er_student.
if not er_student:
    print("Tips: Studenter under 30 år får rabatt!")


# 8 år ikke student, vil gi 0 kr.
# 70 år og ikke student vil gi 0 kr.
# 22 år og student vil gi 50 kr.
# 35 år og student vil gi 120 kr.
# 25 år og ikke student vil gi 120 kr, men får ett tips om at studenter under 30 får billigere pris.

# Utvidelse:
# Hvis "ja" skriver med stor "J" vil det gi False siden Python skiller melloms store og små bokstaver.
# .lower() gjør alle bokstavene små, så da vil det gi True hvis det skrives inn med stor "J".

# --- Refleksjon ---
# "and" krever at begge sidene er True. "or" krever at minst en av sidene er sanne.
# Personen måtte betale 120kr fordi studentrabatten bare gjelder for studenter under 30 år.
# "not" snur en boolsk verdi fra True til False eller motsatt. Jeg kunne ha skrevet "if er_student == False:" for å få samme resultat uten "not".
# 70 åringen får gratis billett fordi personen er over 67 år. Rekkefølgen har vel en betydning i en if/elif-kjede, men personen får gratis billett uansett som studentregelen sjekkes fordi den bare gjelder for personer under 30.