def llegir_llista():
    llista = []
    a = "a"
    while a != ".":
        a = input("Introdueix un nombre (o '.' per acabar): ")
        if a != ".":
            llista.append(int(a))
    return llista

def cercar_numero_llista(llista, numero):
    if numero in llista:  
        return llista.index(numero)  
    else:
        return -1  

# Programa principal
a = llegir_llista()  
num = int(input("Introdueix el número que vols cercar: "))  
posicio = cercar_numero_llista(a, num)  
if posicio != -1:
    print("El número {} es troba a la posició {}.".format(num,posicio))
else:
    print("El número {} no es troba a la llista.".format(num))