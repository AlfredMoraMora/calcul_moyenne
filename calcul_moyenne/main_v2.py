def calc_average(grades):
    # This function calculates the average of the grades and returns the average
    if len(grades) == 0:
        raise ValueError("Cannot calculate the average of an empty list.")
    return sum(grades) / len(grades)

def input_grades():
    # This function creates the list of grades and returns this list
    grades = []
    n = 4  # Quantity of grades to enter.
    print("Entrez 4 notes d'un étudiant: ")
    while len(grades) < n:
        try:
            ele = int(input(f"Note {len(grades) + 1}: "))
            grades.append(ele)
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")
    return grades

def question_check(average):
    # This function checks if the average is greater than 60%
    return average > 60

def main():
    try:
        grades = input_grades()
        average = calc_average(grades)
        print(f"The average is {average}% ")
        print()
        print("Est-ce que l'étudiant a une moyenne supérieur à 60% ? ")
        if question_check(average):
            print("YES")
        else:
            print("NO")
    except ValueError as e:
        print(f"Erreur: {e}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
