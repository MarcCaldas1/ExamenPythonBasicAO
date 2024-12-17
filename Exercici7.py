import random

def crear_llista_num_aleatoris():
    l=[]
    for i in range (5):
        l.append(random.randint(0,5))
    print("Els nombres aleatoris són {}".format(l))

#Programa principal
crear_llista_num_aleatoris()