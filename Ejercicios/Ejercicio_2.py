import math

if __name__ =="__main__":

    class Punto:


        def __init__(self, x:int, y:int):
            self.x:int = x
            self.y:int = y


        def mostrar_coordenadas(self):
            return print(f"({self.x} , {self.y})")


        def mover_punto(self, dx:int, dy:int):
            self.x:int = self.x + dx
            self.y:int = self.y + dy

        def calcular_distancia(self, otro_punto):
            calcular =math.sqrt(((otro_punto.x-self.x)**2)+(otro_punto.y-self.y)**2)
            return calcular




    punto_1:Punto= Punto(2,2)
    punto_2:Punto= Punto(5,5)

    print(punto_1.calcular_distancia(punto_2))






