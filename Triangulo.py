# src/Triangulo.py
from src.Geometria2D import Geometria2D

class Triangulo(Geometria2D):
    def __init__(self, coordenada_x, coordenada_y, base, altura):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.base = base
        self.altura = altura

    # Implementación del método abstracto calcular_area
    def calcular_area(self):
        return (self.base * self.altura) / 2
    
    # Implementación del método abstracto calcular_perimetro
    def calcular_perimetro(self):
        # Asumimos que es un triángulo rectángulo isósceles
        hipotenusa = (self.base**2 + self.altura**2)**0.5
        return self.base + 2 * hipotenusa

