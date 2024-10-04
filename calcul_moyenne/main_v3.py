def calc_average(grades: list) -> float:
    # Cette fonction calcule la moyenne des notes et retourne la moyenne
    if len(grades) == 0:
        raise ValueError("Ne peut pas calculer la moyenne d'une liste vide.")
    return sum(grades) / len(grades)

def input_grades():
    # Cette fonction crée la liste de notes et retourne cette liste
    grades = []
    print("Entrez les notes d'un étudiant (ou tapez 'stop' pour terminer): ")
    while True:
        user_input = input(f"Note {len(grades) + 1}: ")
        if user_input.lower() == 'stop':
            break
        try:
            ele = int(user_input)
            if ele < 0:
                raise ValueError
            elif ele > 100:
                raise ValueError
            grades.append(ele)
        except ValueError:
            print("** Veuillez entrer un nombre entier valide ou 'stop' pour terminer. **")
    return grades

def question_check(average):
    # Cette fonction verifie si la moyenne est supérieur à 60%
    return average > 60

def main():
    try:
        grades = input_grades()
        average = calc_average(grades)
        print()
        print(f"The average is {average:.2f}% ")
        print()
        print("Est-ce que l'étudiant a une moyenne supérieure à 60% ? ")
        if question_check(average):
            print("YES")
        else:
            print("NO")
    except ValueError as e:
        print(f"Erreur: {e}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
