import geometria as g

def menu():
    print("\ncalculadora geometrica 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    print("1 - área do circulo")
    print("2 - perimetro do circulo")
    print("3 - área do retângulo")
    print("4 - perimetro do retânfulo")
    print("5 - área do triangulo")
    print("6 - perimetro do triangulo")
    print("7 - área do cilindo")
    print("0 - sair 😜😜😜😜😜😜😜 \n")

while True:
    menu()
    escolha = int(input("selecione o calculo: "))
    if escolha == 1:
        r = float(input("Raio: "))
        print(f"Área: {g.areadocirculo(r)}")
    elif escolha == 2:
        r = float(input("Raio: "))
        print(f"Perimetro: {g.perimetrocirculo(r)}")
    elif escolha == 3:
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print(f"Área: {g.arearetangulo(base, altura)}")
    elif escolha == 4:
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print(f"Perimetro: {g.perimetroretangulo(base, altura)}")
    elif escolha == 5:
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print(f"Área: {g.areatriangulo(base, altura)}")
    elif escolha == 6:
        l1 = float(input("Lado1: "))
        l2 = float(input("Lado2: "))
        l3 = float(input("Lado3: "))
        print(f"Perimetro: {g.perimetrotriangulo(l1, l2, l3)}")
    elif escolha == 7:
        r = float(input("Raio: "))
        h = float(input("Haltura: "))
        print(f"Área: {g.areacilindro(r, h)}")
    elif escolha == 0:
        print("Saindo...")
        break
    else:
        print("Isso não existe")
        
    
