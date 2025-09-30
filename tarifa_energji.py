kwh = int(input("kWh: "))

if kwh < 0:
    print("Gabim: vlerë negative.")
else:
    if kwh <= 100:
        tarifa = 8
    elif kwh <= 300:
        tarifa = 12
    else:
        tarifa = 15

    energjia = tarifa * kwh
    taksa = 120
    totali = energjia + taksa

    print(f"Energjia (Lek): {tarifa} * {kwh} = {energjia}")
    print(f"Taksa fikse: {taksa}")
    print(f"Totali: {totali}")

    if totali > 5000:
        print("Etiketa: Konsum i lartë")
