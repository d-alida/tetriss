def hozzaad_pontszam(nev, pontszam):
    with open("pontok.txt", "a") as file:
        file.write(f"{nev}: {pontszam}\n")

def kiir_dicsoseglista():
    with open("pontok.txt", "r") as file:
        dicsoseglista = file.readlines()
        for sor in dicsoseglista:
            print(sor.strip())

# torles
def torol_dicsoseglista():
    with open("pontok.txt", "w") as file:
        pass