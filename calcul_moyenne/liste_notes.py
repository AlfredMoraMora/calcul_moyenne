list_notes = [68, 76, 87 ,92]
# Moyenne sans utiliser les fonctions sum et len
counter = 0
sum = 0
# for i in list_notes:
#     sum = sum + i
#     counter += 1
# print(f"Moyenne : {sum/counter}")

for i in range(0, len(list_notes), 1):
    sum = sum + i
    counter += 1
print(f"Moyenne : {sum / counter}")

def sum(val1: int, val2: int) -> int:
    """
    Permet d'additionner deu nombres
    param val1: 1ere valeur
    param val2: 2ere valeur
    return: Le résultat de l'addition
    """
    return val1 + val2