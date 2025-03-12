# main.py
import tkinter as tk
from src.Triangulo import Triangulo

class VentanaTriangulo(tk.Tk):
    def __init__(self, triangulo):
        super().__init__()
        self.title("Triángulo Visual")
        self.geometry("400x400")
        
        # Crear un Canvas para dibujar el triángulo
        self.canvas = tk.Canvas(self, width=400, height=400, bg="white")
        self.canvas.pack()

        # Dibujar el triángulo en el canvas
        self.dibujar_triangulo(triangulo)

    def dibujar_triangulo(self, triangulo):
        # Usamos las coordenadas del vértice superior izquierdo y las dimensiones para crear el triángulo
        x1 = triangulo.coordenada_x
        y1 = triangulo.coordenada_y
        x2 = triangulo.coordenada_x + triangulo.base
        y2 = triangulo.coordenada_y
        x3 = triangulo.coordenada_x + triangulo.base / 2
        y3 = triangulo.coordenada_y - triangulo.altura
        
        # Crear el triángulo usando create_polygon
        self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, outline="black", fill="red", width=2)

# Crear una instancia de Triangulo
triangulo = Triangulo(100, 300, 200, 150)

# Crear la ventana y dibujar el triángulo
ventana = VentanaTriangulo(triangulo)
ventana.mainloop()

