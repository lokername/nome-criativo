def velocityMedia(T,D):
    Sec = T * 360
    return D / Sec
distancia = float(input("Insira a distancia: "))
tempo = float(input("Insira o tempo: "))
print(velocityMedia(tempo,distancia))