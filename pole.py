cislo = int(1) 
cislo_float = float(3.23)
text = str("String je sada znaků, například pro text")
Boolean = True

#Datový typ - pole, kde můžeme mít víc prvků. Závorky píšeme pravý alt + d/f
#V poli se začíná na pozici 0. Ačkoliv je délka pole 6, poslední prvek je na pozici 5

            #0      #1       #2     #3     #4         #5
arrays = ["Ford","Porsche","Audi","BMW","Mercedes","Škoda"]

for x in arrays:
   print(x)

for x in range (len(arrays)):
   print(f"{x+1}: {arrays[x]}")