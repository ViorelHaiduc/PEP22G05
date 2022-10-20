cappucino = 4
espresso = 3.5

print( f"1. cappucino...{cappucino} lei")
print( f"2. Espresso... {espresso} lei")
optiune = int(input("ce optiuni alegeti? [1,2]").strip())
rezultat = input('select 1 to 2')
while not (1<= optiune <=2):
    optiune = int(input('select 1 or 2, valid options'))

bancnota = int(input("introduceti o bancnota [5 lei, 10 lei]"))
#print(optiune)

if optiune == "1":
    rezultat = bancnota - cappucino
elif optiune == "2":
    rezultat = bancnota - espresso
else:
    rezultat = bancnota
print(f"vei primi restul de {rezultat}")



