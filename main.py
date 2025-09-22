
"""
Module pour tester et afficher les nombres premiers jusqu'à 100.
"""


def isprime(p):
    """Retourne True si p est un nombre premier, False sinon."""
    if p in (0, 1):
        return False
    for d in range(2, p):
        if p % d == 0:
            return False
    return True
print (isprime(20))


#### Fonction principale

def main():
    """Affiche les nombres premiers de 0 à 99."""
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()


if __name__ == "__main__":
    main()
