# src/Geometria2D.py
from abc import ABC, abstractmethod

class Geometria2D(ABC):
    # Método abstracto para calcular el área
    @abstractmethod
    def calcular_area(self):
        pass
    
    # Método abstracto para calcular el perímetro
    @abstractmethod
    def calcular_perimetro(self):
        pass

