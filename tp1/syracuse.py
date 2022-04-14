a=int(input("Entrer le nombre désiré :"))
b=0

while (a!= 1):

    if(a%2)==0:
        print("Le nombre suivant selon la conjecture de Syracuse est de : ")
        a=a/2
        print(a)
        b=b+1
    else:
        a=3*a+1
        print("Le nombre suivant selon la conjecture de Syracuse est de : ")
        print(a)
        b=b+1

if b<2 :
    print("Pour arriver à 1, il y a eu",b,"iteration")

if b>1 :
    print("Pour arriver à 1, il y a eu",b,"iterations")
