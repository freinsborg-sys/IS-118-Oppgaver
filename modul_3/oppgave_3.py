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

