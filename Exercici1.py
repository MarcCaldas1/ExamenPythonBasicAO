def llegir_llista():
    l = []
    a = "a"
    while a != ".":
        a = input("Introdueix un nombre: ")
        if a !=".":
            l.append(int(a))
    return l

#Programa principal
llegir_llista()