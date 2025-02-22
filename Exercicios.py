DDD = {61:"Brasília", 11:"São paulo", 71:"Salvador"}
oDDD = int(input("Insira seu DDD: "))
if oDDD in DDD:
    print(DDD[oDDD])
else:
    print("Não existe.")