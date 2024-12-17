def llegir_llista():
    l = []
    a = "a"
    while a != ".":
        a = input("Introdueix un nombre: ")
        if a !=".":
            l.append(int(a))
    return l

def sumar_parells_llista(llista):
    suma = sum(filter(lambda x: x % 2 == 0, llista))
    print("La suma dels nombres és {}".format(suma))

#Programa principal
a=llegir_llista()
sumar_parells=sumar_parells_llista(a)