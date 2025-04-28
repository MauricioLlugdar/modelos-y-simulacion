from numpy import random
import math

def integralExam(x:float)->float:
    #Escribo la funcion a integrar
    return (math.sqrt(x+math.sqrt(x)))

def monte_carlo(n:int)->float:
    b =7 # parametro b del intervalo en la integral
    a =1 # parametro b del intervalo en la integral
    sumatoria: float = 0
    for _ in range(1, n+1):
        sumatoria += integralExam(a + (b-a)*random.uniform(0,1))*(b-a) # sumo la funcion evaluada luego del cambio de variable x
    value:float = (1/n) * sumatoria # calculo el promedio para obtener el valor aproximado de la integral
    return value # devuelvo value pero solo con 6 decimales

def juego() -> int:
    sumatory: float = 0
    count: int = 0
    while sumatory <= 1: # si es mayor que 1 la suma de numeros uniformes aleatorios termino
        uniNum: float = random.uniform(0,1) # numero uniforme aleatorio
        sumatory += uniNum 
        count += 1
    return count # devuelvo la cantidad de numeros uni. al. que se necesitaron para sumar más de 1

def pares(nSim: int) -> float: # funcion que calcula la probabilidad que el resultado de juego() sea impar
    impar:int = 0
    for _ in range (1, nSim+1): # calculo n simulaciones
        if (juego() % 2 != 0): # veo si la resolución fue impar
            impar += 1 # tenemos 1 impar más
    return (impar/nSim) # retorno la probabilidad de que sea impar gracias a nSim cada vez mas grande la probabilidad será mas precisa

if __name__ == "__main__":
    for nSim in [1000, 10000, 100000]: # simulo con numero de simulaciones 1000, 10000 y 100000
        print(f"Monte carlo en {nSim} da de resultado= {monte_carlo(nSim)}")
        
    for nSim in [100, 1000, 10000]: # simulo con numero de simulaciones 100, 1000 y 10000
        print(f"Estimamos probabilidad p de que el numero total de sumandos para conseguir el acierto sea impar en {nSim} simulaciones \
        p = {pares(nSim)}")
    
    