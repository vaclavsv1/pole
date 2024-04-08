zbozi = ["CPU", "GPU", "RAM", "HDD", "SSD", "Motherboard", "Vodní chlazení", "Zdroj", "Case"]
kosik =[]

def vypis_zbozi():
    print("---------------------------")
    print(" ")
    print("Zde je zboží")
    print(" ")
    print("---------------------------")

def vypis_kosik():
    print("---------------------------")
    print(" ")
    print("Zde je Váš košík")
    print(" ")
    print("---------------------------")

def vypis_pole(prvek):  
    for x in range(len(prvek)): 
        print(f"Komponent s číslem {x+1}: {prvek[x]}")
    print(" ")
    print("---------------------------")


while(True):
    vypis_zbozi()
    vypis_pole(zbozi)

    print("Pokud chcete ukončit nákup, vyšší číslo, než je ve výběru")
    vyber = int(input("Zde zadejte Vaší volbu produktu podle čísla: "))

    if 0>vyber<=len(zbozi):
        kosik.append(zbozi[vyber-1])
        vypis_kosik()
        vypis_pole(kosik)
        zbozi.pop(vyber-1)
    else:
        print("Děkujeme za nákup, můžete ke kase:")
        break