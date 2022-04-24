# Jeu du morpion

def print_morpion():
    print(f"{l[0]} | {l[1]} | {l[2]}")
    print("--+---+--")
    print(f"{l[3]} | {l[4]} | {l[5]}")
    print("--+---+--")
    print(f"{l[6]} | {l[7]} | {l[8]}")


def ask_check_input():
    while True:
        try:
            _case = input(f"Tour {tour} Entrez un nombre en 1 et 9 : ")
            _case = int(_case)
            if _case < 1 or _case > 9:
                print("Le nombre n'est pas entre 1 et 9")
            elif l[_case - 1] != " ":
                print(f'La case {_case} est déjà prise !')
            else:
                return _case
        except:
            print(f'{_case} n\'est pas jouable !')


if __name__ == '__main__':
    l = [" " for x in range(9)]
    tour = 0
    while tour < 9:
        tour += 1
        _input = ask_check_input()
        if tour % 2 == 0:
            l[_input - 1] = "X"
        else:
            l[_input - 1] = "O"

        if l[0] == l[4] == l[8] != " " \
            or l[0] == l[1] == l[2] != " " \
            or l[3] == l[4] == l[5] != " " \
            or l[6] == l[7] == l[8] != " " \
            or l[2] == l[4] == l[6] != " " \
            or l[0] == l[3] == l[6] != " " \
            or l[2] == l[5] == l[8] != " " \
            or l[1] == l[4] == l[7] != " ":
            print(f'le joueur {l[_input - 1]} a gagné !')
            break
        print_morpion()
    else:
        print("Match nul :")
print_morpion()
