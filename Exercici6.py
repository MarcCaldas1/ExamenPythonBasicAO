def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un nom: ")
        if a!=".":
            l.append(a)
    return l

def crear_paraula_llista(l):
    for e in l:
        print(e[0])


#Programa principal
a=llegir_llista()
b=crear_paraula_llista(a)