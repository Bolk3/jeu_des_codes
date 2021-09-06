from random import randint

def setup():
    print ("combien de nombre ?\n1 - 100\n2 - 200\n3 - 300")
    condition = False
    while condition != True:
        choix = int(input())
        if choix == 1:
            return randint(0, 100)
            condition = True
        elif choix == 2:
            return randint(0, 200)
            condition = True
        elif choix == 3:
            return randint(0, 300)
            condition =True
        else:
            print("vous n'avez choisis une option valable")

def verification(nombre_al, nombre_int):
    if nombre_al == nombre_int:
        return True
    else:
        return False

def jeu(nb_al):
    vies = 3
    jeux_fini = False
    while jeux_fini != True or vie == 0:
        print(f'il vous reste {vies}')
        nombre = input("quel est le nombre ?")
        if verification(nb_al, nombre) == True:
            print(f'felicitaion le chiffe etait {nb_al}')
            jeux_fini = True
        else:
            print("faux vous avez perdu une vie")
            vies -= 1

def main():
    nub = setup()
    jeu(nub)


if __name__ == '__main__':
    main()        
    input("pressez entree pour continuer ...")