import math

def areadocirculo(raio):
    return math.pi * (raio **2)

def perimetrocirculo(raio):
    return 2 * math.pi * raio

def arearetangulo(base, altura):
    return base * altura

def perimetroretangulo(base, altura):
    return 2 * (base * altura)

def areatriangulo(base, altura):
    return (base * altura) / 2

def perimetrotriangulo(l1, l2, l3):
    return l1 + l2 + l3

def areacilindro(raio, haltura):
    return (2 * math.pi * raio * haltura) + (2 * math.pi * (raio ** 2))
