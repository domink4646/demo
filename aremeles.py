ar = int(input("Az alkatrész jelenlegi ára: "))
aremeles = float(input("Áremelés (százalékban): "))

print(f"Az alkatrész új ára: {ar * (1 + aremeles / 100)}")