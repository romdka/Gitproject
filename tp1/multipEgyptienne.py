def multiplicationEgyptienne(a, b):
    resultat = 0
    i=0
    while a != 0:
        if a % 2 == 1:
            resultat += b
        a //= 2 
        b = b+b 
        i+=1
    
    print("Le résultat de la multiplication Egyptienne est de : ",resultat)
    if i==0:
        print("Il y a",i,"itération dans ce calcul")
    else:
        print("Il y a",i,"itérations dans ce calcul")
    
    return resultat
 

a=int(input("Entrer votre premier nombre :"))
b=int(input("Entrer votre second nombre :"))

multiplicationEgyptienne(a,b)
