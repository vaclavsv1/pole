zbozi = ["CPU", "GPU", "RAM", "HDD", "SSD", "Motherboard", "Vodní chlazení"]
kosik =[]

for x in range (len(zbozi)):
        print(f"číslo {x+1}: {zbozi[x]}")

def vypis_pole(prvek):
    for x in range (len(prvek)):
        print(f"číslo {x+1}: (prvek)[x]")

prvek_plus = input("Jakou položku chceš vložit do košíku ? ")
zbozi.remove(prvek_plus)
vypis_pole(zbozi)

kosik.append(prvek_plus)

print("Váš košík: ")
print(kosik)
