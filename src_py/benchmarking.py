import random
import time
from src_py.ordenamiento import Bubble  

class Benchmarking:
    def __init__(self):
        print("Benchmarking ")
        
        self.bubble = Bubble()
        arreglo = self.build_arreglo(1000)

        tarea = lambda: self.bubble.sort_bubble(arreglo) 

        tiempoM = self.contartimemilles(tarea)
        print(f"Tiempo en milisegundos: {tiempoM} ms")

        tiempoN = self.contarnanotime(tarea)
        print(f"Tiempo en nanosegundos: {tiempoN} ns")
        
        tarea_mejorada = lambda: self.bubble.burbujamejorado(arreglo)
        tiempoN_mejorada = self.contarnanotime(tarea_mejorada)
        print(f"Tiempo en nanosegundos (mejorado): {tiempoN_mejorada} ns")
        
        tarea_seleccion = lambda: self.bubble.seleccion(arreglo)
        tiempoN_seleccion = self.contarnanotime(tarea_seleccion)
        print(f"Tiempo en nanosegundos (selección): {tiempoN_seleccion} ns")
    
    def build_arreglo(self, tamano):
        arreglo = []
        for _ in range(tamano):  
            numero = random.randint(0, 99999)
            arreglo.append(numero)
        return arreglo

    def contartimemilles(self, tarea):
        start_time = time.time()
        tarea()
        end_time = time.time()
        return (end_time - start_time)

    def contarnanotime(self, tarea):
        start_time = time.time()
        tarea()
        end_time = time.time()
        return (end_time - start_time) * 1_000_000_000
