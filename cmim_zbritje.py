baze = float(input("Cmimi bazë: "))
zb = float(input("Zbritja (%): "))

if baze < 0 or zb < 0 or zb > 100:
    print("Gabim: vlera të pavlefshme.")
else:
    pas = baze * (1 - zb / 100)
    final = pas * 1.15
    print(f"Pas zbritjes: {round(pas, 2)}")
    print(f"Me TVSH (15%): {round(final, 2)}")
