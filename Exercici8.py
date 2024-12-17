def comparar_llistes(llista1, llista2):
    resultat = []  
    for i in range(5):  
        if llista2[i] not in llista1:  
            resultat.append(0)
        elif llista2[i] == llista1[i]:  
            resultat.append(2)
        else:  
            resultat.append(1)
    return resultat

# Programa principal 
def llegir_llista_5_elements():
    llista = []
    print("Introdueix 5 nombres per a la llista:")
    while len(llista) < 5:
        nombre = int(input("Introdueix el nombre {}: ".format(len(llista) + 1)))
        llista.append(nombre)
    return llista
print("Llista 1:")
llista1 = llegir_llista_5_elements()
print("Llista 2:")
llista2 = llegir_llista_5_elements()
resultat = comparar_llistes(llista1, llista2)
print("Llista 1:", llista1)
print("Llista 2:", llista2)
print("Resultat de la comparació:", resultat)