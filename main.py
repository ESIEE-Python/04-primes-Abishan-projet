""""Calculer le nombre premier"""

from math import sqrt


#### Fonction secondaire


def isprime(p):
    """"Fonction pour calculer le nombre premier"""
    # votre code ici
    p=int(p)

    if p<2:
        return False
    for d in range(2,int(sqrt(p))+1):
        if p%d==0:
            print(f"{p}  =  {d} x {int(p/d)}  : False")
            break
    else:
        return True

    return False


#### Fonction principale


def main():
    """"Fonction pour calculer le nombre premier"""
    # vos appels à la fonction secondaire ici
    isprime(731)

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
