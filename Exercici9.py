def majors_edat(edat1,edat2):
    if edat1 >= 18:
        print("La persona 1 és major d'edat")
    
    elif edat1 <18 :
        print("La persona 1 no és major d'edat")

    if edat2>=18:
        print("La persona 2 és major d'edat")

    elif edat2<18:
        print("La persona 2 no és major d'edat")

#Programa principal
edat1= int(input("Introdueix la teva edat: "))
edat2= int(input("Introdueix una altre edat: "))
a=majors_edat(edat1,edat2)