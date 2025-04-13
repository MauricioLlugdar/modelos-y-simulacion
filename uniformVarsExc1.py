from numpy import random

def amNumbAddExc1(n:int)->int:
    amountOfUni:int=0
    sumUni:float=0
    totalOfUni:int=0
    uniVar:float=random.uniform(0,1)
    for _ in range(1,n):
        if(sumUni<=1):
            sumUni += uniVar
            totalOfUni +=1
            uniVar =random.uniform(0,1)
        else:
            sumUni=0
            amountOfUni +=1 #How many times sumUni exceeds 1

    return (totalOfUni/amountOfUni)

if __name__ == "__main__":
    print(amNumbAddExc1(100000))