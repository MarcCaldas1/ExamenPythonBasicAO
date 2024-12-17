def llegir_llista():
    llista = []
    a = "a"
    while a != ".":
        a = input("Introdueix un nombre: ")
        if a !=".":
            llista.append(int(a))
    return llista



def senars_llista(llista):
    l=[]
    p=list(filter(lambda x:x%2!=0,llista))
    print("Els nombres senars són {}".format(p))


#Programa principal
a=llegir_llista()
b=senars_llista(a)