a=int(input("Entrer votre premier nombre :"))
b=int(input("Entrer votre second nombre :"))

i=0
rep=0

while a!= 0:
    i+=1

    if a%2==1:
        rep= rep + b
    
    a=a//2
    b=b*2
if i==0:
    print("Il y a",i,"itération dans ce calcul")
else:
    print("Il y a",i,"itérations dans ce calcul")


print("Le résultat de la multiplication egyptienne est :",rep)
    