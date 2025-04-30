#Creen una clase Metodos
#Crear un metodo sort bubble que reciba un arreglo y solo imprima un mensaje
class Bubble: 
    def sort_bubble (self,array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i+1, n):
                if arreglo[j] > arreglo[j]:
                    arreglo[j], arreglo[j] = arreglo[j], arreglo[j]
                    return arreglo
    def burbujamejorado(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            intercambio = False
            for j in range(0, n - i - 1):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                    intercambio = True
            if not intercambio:
                break
        return arreglo
    def seleccion(self, array):
       arreglo = array.copy()
       n = len(arreglo)
       for i in range(n):
            menor = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[menor]:
                    menor = j
            arreglo[i], arreglo[menor] = arreglo[menor], arreglo[i]
            return arreglo